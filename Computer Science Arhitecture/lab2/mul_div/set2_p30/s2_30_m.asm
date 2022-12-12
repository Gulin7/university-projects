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
    a db 5
    e dw 20
    h dw 19

; our code starts here
segment code use32 class=code
    start:
        ; mul/div set2 30: 100/(e+h-3*a)
        ; a=5, e=20, h=19 the result is 100/(40-15)=100/24=4,remainder 4 
        ; so AX=4, DX=4
        mov AL,3
        mov bl,byte[a]
        mul bl ; in AX we have 3*a 
        mov BX, word[e]
        add BX, word[h]
        sub BX,AX
        mov CX,BX ; we move BX to CX so we can divide
        mov DX,0
        mov AX,100
        div CX
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
