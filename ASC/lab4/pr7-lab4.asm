bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; Given the words A and B, compute the doubleword C:
    ;the bits 0-4 of C have the value 1
    ;the bits 5-11 of C are the same as the bits 0-6 of A
    ;the bits 16-31 of C have the value 0000000001100101b
    ;the bits 12-15 of C are the same as the bits 8-11 of B
    a dw 1023
    b dw 1023
    c dd 0

; our code starts here
segment code use32 class=code
    start:
        mov cl, 11111b
        or [c], cl ; first 5 bits are 1
        mov ax, [a] ; ax=a
        and ax, 1111111b ; ax = 00...00 and the first 7 bits of a
        shl ax, 5 ; we shift the bits  00...7bits.. 00000
        or [c], ax 
        mov cl, 1100101b
        or [c+2], cl
        mov bx, [b] ; same process as with a
        and bx, 111100000000b
        shl bx, 4
        or [c], bx 
        mov EBX, [c]
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
