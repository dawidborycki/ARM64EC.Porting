# CMakeList.txt : CMake project for Arm64EC.Porting, include source and define
# project specific logic here.
#

# Add source to this project's executable.
add_library (Filters SHARED "Filters.cpp" "Filters.h")

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET Filters PROPERTY CXX_STANDARD 20)
endif()

# TODO: Add tests and install targets if needed.
