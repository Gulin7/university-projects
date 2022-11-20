bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; UNSIGNED!!!
    a db 34
    b db 2
    c dw 6
    e dd 4000
    x dq 4098

; our code starts here
segment code use32 class=code
    start:
        ;(a-2)/(b+c)+a*c+e-x; a,b-byte; c-word; e-doubleword; x-qword
        ; 32/8+34*6+10-4098 = 110
        mov al,[b]
        cbw ; ax=b
        mov bx,ax ;bx=b
        add bx,[c] ; in bx=b+c
        mov al,[a] ; al=a
        sub al,2 ; al=a-2
        mov ah, 0; ax=a-2
        mov dx, 0 ; in dx:ax =(a-2)
        div bx ; in dx:ax = (a-2)/(b+c)
        mov cx, ax ; in cx= (a-2)/(b+c)
        mov al,[a] ; al=a
        mov ah, 0 ;ax=a 
        mul word[c] ; dx:ax = a*c
                    ; cx= ()/()
        push dx
        push ax
        pop ebx ; ebx=a*c
        mov eax, 0
        mov ax,cx ; eax=()/()
        add ebx,eax ; ebx=()/()+a*c
        add ebx,[e] ; ebx = ()/()+a*c+e 
        mov eax,ebx
        mov edx, 0 ; edx:eax = ()/()+ a*c+e-doubleword
        sub eax,[x]
        sbb edx,[x+4]
        ; in edx:eax we have the result
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
