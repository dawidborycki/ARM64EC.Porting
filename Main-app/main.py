import ctypes, sys, os
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QPainter
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QChartView, QValueAxis

rootPath = os.getcwd() 

vectorsLibName = os.path.join(rootPath, "Dependencies\\Arm64EC-release\\Vectors.dll")
filtersLibName = os.path.join(rootPath, "Dependencies\\Arm64EC-release\\Filters.dll")

class MainWindowWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        # Buttons
        self.buttonVectors = QtWidgets.QPushButton("Vectors")
        self.buttonFilters = QtWidgets.QPushButton("Filters")
        
        # Label
        self.computationTimeLabel = QtWidgets.QLabel("", alignment=QtCore.Qt.AlignTop)

        # Chart
        self.chart = QChart()
        self.chart.legend().hide()                       

        self.chartView = QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)

        # Configure layout
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.computationTimeLabel)
        self.layout.addWidget(self.buttonVectors)
        self.layout.addWidget(self.buttonFilters)
                
        self.layout.addWidget(self.chartView)

        # Configure chart y-axis
        self.axisY = QValueAxis() 
        self.axisY.setRange(-150, 150)

        self.chart.addAxis(self.axisY, QtCore.Qt.AlignLeft)    

        # Signals and slots
        self.buttonVectors.clicked.connect(self.runVectorCalculations)
        self.buttonFilters.clicked.connect(self.runTruncation)

    @QtCore.Slot()
    def runVectorCalculations(self):
        vectorsLib = ctypes.CDLL(vectorsLibName)
        vectorsLib.performCalculations.restype = ctypes.c_double
        
        computationTime = vectorsLib.performCalculations()

        self.computationTimeLabel.setText(f"Computation time: {computationTime:.2f} ms")

    def prepareSeries(self, inputData, length):
        series = QLineSeries()
        for i in range(1, length):
            series.append(i, inputData[i])            
        
        return series
    
    @QtCore.Slot()
    def runTruncation(self):
        # Get DLL
        filtersLib = ctypes.CDLL(filtersLibName)
        
        # Remove all previous series
        self.chart.removeAllSeries()

        # Generate signal
        filtersLib.generateSignal()
        filtersLib.getInputSignal.restype = ctypes.POINTER(ctypes.c_double)        

        # Display signal
        signal = filtersLib.getInputSignal()
        seriesSignal = self.prepareSeries(signal, filtersLib.getSignalLength())        
        self.chart.addSeries(seriesSignal)

        # Run convolution
        filtersLib.truncate()
        filtersLib.getInputSignalAfterFilter.restype = ctypes.POINTER(ctypes.c_double)        

        # Display signal after convolution
        signalAfterFilter = filtersLib.getInputSignalAfterFilter()
        seriesSignalAfterFilter = self.prepareSeries(signalAfterFilter, filtersLib.getSignalLength())                        
        self.chart.addSeries(seriesSignalAfterFilter)        

        # Configure y-axis
        seriesSignal.attachAxis(self.axisY)
        seriesSignalAfterFilter.attachAxis(self.axisY)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindowWidget()
    widget.resize(600, 400)
    widget.show()

    sys.exit(app.exec())