bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; a,b,c,d-byte, e,f,g,h-word
    a db 7
    b db 24
    c db 6


; our code starts here
segment code use32 class=code
    start:
        ; (a*b)/c
        ; a= 7, b=24, c=6 => 28
        mov al, byte[a]
        mov bl, byte[b]
        imul bl
        ; the result of a*b is stored in AX
        mov BL, byte[c]
        idiv BL ; this divides AX with BL; the final result is stored on AL
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
