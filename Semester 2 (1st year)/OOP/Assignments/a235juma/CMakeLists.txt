cmake_minimum_required(VERSION 3.24)
project(a235juma C)

set(CMAKE_C_STANDARD 11)

add_executable(a235juma main.c domain/domain.c domain/domain.h dynamicArray/dynamicArray.c dynamicArray/dynamicArray.h operationStack/operation_stack.c operationStack/operation_stack.h repository/repository.c repository/repository.h tests/tests.c tests/tests.h ui/ui.c ui/ui.h services/service.c services/service.h)
