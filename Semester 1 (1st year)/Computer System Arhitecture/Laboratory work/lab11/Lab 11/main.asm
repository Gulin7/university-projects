bits 32

global start      

extern exit, gets, printf, check_big_case, check_small_case
import exit msvcrt.dll    
import printf msvcrt.dll
import gets msvcrt.dll
import printf msvcrt.dll
import read msvcrt.dll

segment data use32 class=data
        format db "%s", 0
        len dd 0
        endline db 10, 0
        sentence resb 100
        big_case resb 100
        small_case resb 100
        
        
segment code use32 class=code
    start:
    ;Read a sentence from the keyboard containing different characters (lowercase letters, big letters, numbers, special ones, etc). Obtain a new string with only the small case letters and another string with only the big case letters. Print both strings on the screen
            mov edi, sentence
            push sentence
            call [gets]
            add esp, 4*2
            mov esi, 0
            mov edi, 0
            push sentence
            call check_big_case
            add esp, 4
            
            push endline
            call [printf]
            add esp, 4
            push sentence
            call check_small_case
            add esp, 4
            
                    
                
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
