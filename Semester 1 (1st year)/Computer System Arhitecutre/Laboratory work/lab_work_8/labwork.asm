bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
extern printf
import printf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    format db "%d", 0
; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov EAX, 69
        push EAX
        push format
        call [printf]
        add ESP, 4*2
        push 0
        ;mov ECX, 1
        ;repeat:
        ;push ECX
        ;push fr
        ;push filename
        ;call [fopen]
        ;add ESP, 4*2
        ;pop ECX
        ; EAX
        ;loop repeat
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
