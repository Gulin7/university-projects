bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; a,b,c - byte, d - word
    a db 4
    b db 3
    c db 2
    d dw 1

; our code starts here
segment code use32 class=code
    start:
        ; [2*(a+b)-5*c]*(d-3)
        ; a=4, b=3, c=2, d=1 the result is: (2*7-5*2)*(-2)=4*(-2)=-8
        mov BL,byte[a]
        add BL, byte[b]
        mov AL,2 ; we store 2 in AL so we can multiply it with (a+b)
        imul BL ; in AX we will have the result of 2*(a+b) = 2*7=14
        mov BX, AX ; we store 2*(a+b) in BX
        mov AL,5
        mov CL, byte[c]
        imul CL ; in AX we now have 5*c=10
        sub BX,AX ; in BX we will have the result of [2*(a+b)-5*c]
        mov AX,mword[d]
        sub AX,3 ; we put in AX: d-3
        mov DX,0 ; we put 0 in DX so it's empty for the next multiplication that's done with words
        imul BX ; we multiply BX with AX and we have the result on DX:AX
        
    
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
