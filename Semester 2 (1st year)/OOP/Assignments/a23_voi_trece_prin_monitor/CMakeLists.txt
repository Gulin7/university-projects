cmake_minimum_required(VERSION 3.24)
project(a23_voi_trece_prin_monitor)

set(CMAKE_CXX_STANDARD 17)

add_executable(a23_voi_trece_prin_monitor main.cpp domain/medicine.c domain/medicine.h dynamic_array/dynamic_array.c dynamic_array/dynamic_array.h repository/repository.c repository/repository.h service/service.c service/service.h test/test.c test/test.h undo_redo/undo_redo.c undo_redo/undo_redo.h)
