# CMakeList.txt : CMake project for Arm64EC.Porting, include source and define
# project specific logic here.
#

# Add source to this project's executable.
add_library (Vectors SHARED "Vectors.cpp" "Vectors.h")

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET Vectors PROPERTY CXX_STANDARD 20)
endif()

# TODO: Add tests and install targets if needed.
