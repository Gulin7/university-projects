cmake_minimum_required(VERSION 3.24)
project(a23_3rd C)

set(CMAKE_C_STANDARD 11)

add_executable(a23_3rd main.c tests.c dynamicArray.c medicine.c operation.c repository.c service.c ui.c)
