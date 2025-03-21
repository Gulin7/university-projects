bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; a,b,c,d byte
    a db 1
    b db 5
    c db 3
    d db 3

; our code starts here
segment code use32 class=code
    start:
        ; (a+b)-(a+d)+(c-a)
        ; For a=1,b=5,c=3,d=3 the result is: (1+5)-(1+3)+(3-1)=6-4+2=4
        mov AL,byte[b]
        add AL,byte[a] ;AL= a+b 
        cbw ; AX =a+b
        mov CX, AX ; CX=a+b
        mov AL,byte[d]
        add AL,byte[a] ;AL=a+d 
        cbw ; AX=a+d
        mov BX,AX
        mov AL, byte[c]
        sub AL, byte[a] ; AL=c-a 
        cbw ; AX=c-a
        sub CX,BX
        ADD CX,AX
        ;in CX we store the final result
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
