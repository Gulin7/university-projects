cmake_minimum_required(VERSION 3.24)
project(a23pls C)

set(CMAKE_C_STANDARD 17)

add_executable(a23pls main.c operationStack/operation_stack.c dynamicArray/dynamicArray.c domain/domain.c repository/repository.c services/service.c tests/tests.c ui/ui.c)
