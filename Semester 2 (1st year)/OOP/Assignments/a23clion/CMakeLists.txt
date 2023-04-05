cmake_minimum_required(VERSION 3.24)
project(a23clion C)

set(CMAKE_C_STANDARD 11)

add_executable(a23clion Medicine.h Medicine.c Operations.h Operations.c Repository.h Service.h Tests.h Ui.h UndoRedo.h UndoRedo.c Ui.c Tests.c Service.c Repository.c start.c)
