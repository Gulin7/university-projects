bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fclose, fread, fprintf, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
extern fopen, fclose, fread, fprintf, printf
import fopen msvcrt.dll
import fclose msvcrt.dll
import fread msvcrt.dll
import fprintf msvcrt.dll
import printf msvcrt.dll
                          
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; A text file is given. Read the content of the file, count the number of odd digits and display the result on the screen. The name of text file is defined in the data segment.
    file_name db "problem34lab8.txt",0
    access_mode db "r", 0
    file_descriptor resd 1
    no_odd_digits dd 0
    digit db 0
    format db "The number of odd digits is: %d", 0
    format_for_test db "%s", 0

; our code starts here
segment code use32 class=code
    start:
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 4*2
        cmp eax, 0
        ;jne enddd
        ;push dword "It didn't work"
        ;push dword format_for_test
        ;call [printf]
        ;add esp,4*2
        ;enddd:
        
        mov [file_descriptor], eax ; in eax we have the file descriptor
        mov ecx, 1
        
        loop.:
        push dword [file_descriptor]
        push dword 1
        push dword 1
        push dword digit
        call [fread]
        add esp, 4*4
        cmp eax, 0
        je end   
        and byte [digit], 01h
        cmp byte [digit], 0
        je not_odd
        add byte [no_odd_digits], 1
        not_odd:
        loop loop.
        end:
        
        
        push dword [no_odd_digits]
        push dword format
        call [printf]
        add esp, 4*2
        
        mov al, [no_odd_digits]
        
        push dword [file_descriptor]
        call [fclose]
        add esp, 4*1
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
