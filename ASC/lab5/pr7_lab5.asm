bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ;7: Two byte string S1 and S2 are given, having the same length. Obtain the string D by intercalating the elements of the two strings.
    ;S1: 1, 3, 5, 7
    ;S2: 2, 6, 9, 4
    ;D: 1, 2, 3, 6, 5, 9, 7, 4
    s1 db 1,3,5,7
    s2 db 2,6,9,4
    e equ $-s2 ; e is the length of one set
    d resb e*2 ; we reserve enough bytes to store the intercalating sets

; our code starts here
segment code use32 class=code
    start:
        mov ecx, e
        jecxz out ; if no elements -> jump to the end
        mov esi, 0 ; starting the i from 0
        repeat:
        mov edx, s1 ; load the adress of s1 in edx
        mov al, [edx+esi]
        mov edx, s2
        mov bl, [edx+esi]
        mov edx, d ;
        mov [edx+esi*2], al
        mov [edx+esi*2+1], bl
        inc esi
        loop repeat
        out:
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
