bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ;a - byte, b - word, c - double word, d - qword - Unsigned representation
    a db 7
    b dw 5
    c dd 120
    d dq 20
    r resq 1

; our code starts here
segment code use32 class=code
    start:
        ;c-(d+d+d)+(a-b)
        ;120-(20+20+20)+(7-5) = 120-60+2=62
        mov ebx,0 
        mov bl, [a]
        mov AX, [b]
        sub BX,AX ; BX= a-b
        mov EAX, [d]
        mov EDX, [d+4] ; EDX:EAX=d
        add eax,[d]
        adc edx, [d+4] ; EDX:EAX=d+d
        add eax,[d]
        adc edx, [d+4] ; in EDX:EAX we have d+d+d
        mov CX,BX ; CX = a-b
        mov EBX,0
        mov BX,CX; EBX = a-b
        mov ECX, dword[c] ; ECX=c 
        mov dword[r], 0
        mov dword[r+4], 0
        mov dword[r], ECX ; r=ECX=c
        SUB dword[r],eax
        sbb dword[r+4], edx ; we substract edx:eax from r
        add dword[r], ebx ; we add ebx to r
        ;adc dword[r+4],0 ;not sure if needed; maybe when the result is too big for dword
        mov EAX,[r]
        mov EDX,[r+4] ; we store the final result in edx:eax
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
