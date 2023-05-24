cmake_minimum_required(VERSION 3.24)
project(a23)

set(CMAKE_CXX_STANDARD 17)

add_executable(a23 main.c main.c ui/ui.c domain/domain.c dynamicArray/dynamicArray.c repository/repository.c services/service.c tests/tests.h tests/tests.c operationStack/operation_stack.h operationStack/operation_stack.c)
