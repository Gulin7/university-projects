bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; SIGNED
    a db 14
    b db 5
    c dw -8
    e dd 416
    x dq 3000
    
; our code starts here
segment code use32 class=code
    start:
        ; (a-2)/(b+c)+a*c+e-x; a,b-byte; c-word; e-doubleword; x-qword
        ; a=14, b=5,c=-8, e=416, x=3000
        ; 12/(-3) + 14*(-8)+406 -3000 = -4-112+416- 3000 = 300-3000=-2700
        mov al,[b]
        cbw ; ax=b
        add ax,[c]
        mov bx,ax ; bx=(b+c)
        mov al,[a]
        sub al,2
        cbw
        cwd ; dx:ax=a-2 
        idiv bx ; dx:ax= ()/()
        mov bx,ax ; bx= ()/()
        mov al,[a]
        cbw
        imul word[c] ; dx:ax = a*c
                    ; bx=()/()
        push dx
        push ax
        pop ecx ;ecx=a*c
        mov ax,bx
        cwde ; eax=()/()
        add eax, ecx ; eax=()/()+a*c
        cdq
        mov ebx, eax
        mov ecx, edx
        mov eax, [e]
        cdq
        add eax, ebx
        adc edx, ecx
        ;final result on edx:eax
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
