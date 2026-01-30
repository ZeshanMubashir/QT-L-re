cmake_minimum_required(VERSION 3.16)

# Set the project name
project(QT-L-re)

# Set C++ standard if you're using C++
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find Qt if you plan to use it
find_package(Qt6 COMPONENTS Core Widgets REQUIRED)

# Add an executable if you have source files
add_executable(${PROJECT_NAME} main.cpp)

# Link Qt libraries if using Qt
target_link_libraries(${PROJECT_NAME} Qt6::Core Qt6::Widgets)