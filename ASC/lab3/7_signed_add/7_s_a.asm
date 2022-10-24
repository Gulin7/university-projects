bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; a - byte, b - word, c - double word, d - qword - Signed representation
    a db -2
    b dw -42
    c dd 450
    d dq -1004
    
; our code starts here
segment code use32 class=code
    start:
        ; (c+c+c)-b+(d-a)
        ; c=450, b=-42, d=-1004, a=-2 =>1350+42-1002 = 1392-1002=390
        mov EBX,[c]
        add EBX, [c]
        add EBX, [c] ; EBX = c+c+c
        mov ax, [b]
        cwde ; EAX=b 
        sub EBX,EAX ; ebx= (c+c+c)-b 
        mov al, [a]
        cbw ; ax=a
        cwde ;eax=a
        cdq ; in EDX:EAX we have a 
        sub dword[d],eax
        sbb dword[d+4],edx ; in d we have d-a
        mov EAX,EBX
        cdq ; in edx:eax we have c+c+c-b 
        add eax,dword[d]
        adc edx, dword[d+4] ; final result is in edx:eax 
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
