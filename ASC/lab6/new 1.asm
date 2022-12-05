bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; A string of doublewords is given. Obtain the list made out of the high bytes of the high words of each doubleword from the given list with the property that these bytes are multiple of 3.
    ;s DD 12345678h, 1A2B3C4Dh, FE98DC76h
    ;d: 12h.
    s dd 12345678h, 1A2B3C4Dh, 0FE98DC7h    
    len equ ($-s)/4
    t db 3
    rez resb len

; our code starts here
segment code use32 class=code
    start:
        ; ...
        mov ecx, len ; we have the length on ecx
        jecxz out ; we jump if ecx is 0
        mov esi, s ; we put s in esi
        mov edi, rez
        cld ; we clear dir flag
        repeat:
            lodsw ; we load the first word on ax
            lodsw ; we load the high word of the doubleword of s on AX, losing the first one
            shr ax, 8 
            mov ah, 0
            mov bl, al
            div byte[t]
            cmp ah, 0
            jnz notmultiple
            mov al, bl
            stosb
            notmultiple:
        loop repeat
        out:
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
