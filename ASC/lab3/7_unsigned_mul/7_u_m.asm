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
    a db 6
    b db 1
    c dw 3
    e dd 10
    x dq 4029

; our code starts here
segment code use32 class=code
    start:
        ;(a-2)/(b+c)+a*c+e-x; a,b-byte; c-word; e-doubleword; x-qword
        ; 4/4+18+10-4020 = 29-4029=-4000
        mov al,[b]
        cbw ; ax=b
        mov bx,ax ;bx=b
        add bx,[c] ; in bx=b+c
        mov al,[a] ; al=a
        sub al,2 ; al=a-2
        cbw ; ax=a-2
        cwd ; in dx:ax =(a-2)
        div bx ; in dx:ax = (a-2)/(b+c)
        mov cx, ax ; in cx= (a-2)/(b+c)
        mov al,[a] ; al=a
        cbw ;ax=a 
        mul word[c] ; dx:ax = a*c
                    ; cx= ()/()
        push dx
        push ax
        pop ebx ; ebx=a*c
        mov ax,cx
        cwde ; eax=()/()
        add ebx,eax ; ebx=()/()+a*c
        add ebx,[e] ; ebx = ()/()+a*c+e 
        mov eax,ebx
        cdq ; edx:eax = ()/()+ a*c+e-doubleword
        sub eax,[x]
        sbb edx,[x+4]
        
        ; in edx:eax we have the result
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
