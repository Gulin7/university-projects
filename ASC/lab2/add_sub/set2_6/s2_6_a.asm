bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; a,b,c,d word
    a dw 20
    b dw 5
    c dw 15
    d dw 25

; our code starts here
segment code use32 class=code
    start:
        ; c-(d+a)+(b+c)
        ; for a=20, b=5, c=15, d=25 the result is 15-45+20 = -10
        mov AX, word[c] ; AX=C
        mov BX, word[d]
        add BX, word[a] ; BX=d+a 
        mov CX, word[b]
        add CX,word[c] ; CX=b+c 
        sub AX,BX
        add AX,CX ; We store the final result in AX
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
