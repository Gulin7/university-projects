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
    a db 3
    b db 3
    c db 3
    d db 3
    e dw 3
    f dw 6
    g dw 6
    h dw 3
    aux dw 1

; our code starts here
segment code use32 class=code
    start:
        ; L2 mul/div set2 21: (f*g-a*b*e)/(h+c*d)
        ; a=b=c=d=e=h=3 f=g=6: (9-27)/(3+9) = -18/12 = -2, remainder= 6
        mov DX,0
        mov AX, word[f]
        mov BX, word[g]
        mul BX
        ; in DX:AX we have the result of f*g
        mov CX, AX
        mov BL, byte[a]
        mov AL, byte[b]
        mul BL ; in AX we now have a*b 
        mov [aux],AX
        mov AX, word[e]
        mov BX,DX
        mul word[aux]
        ; In DX:AX we have a*b*e, while in BX:CX we have f*g 
        sub BX,DX
        SUB CX,AX
        ; we now have the result of (f*g-a*b*e) in BX:CX
        mov DL, byte[d]
        mov AL, byte[c]
        mul DL
        ; ON AX we have c*d
        add AX,word[h]
        ;BX:CX contains (f*g-a*b*e), and AX contains h+c*d
        ;I need to move BX:CX to EAX and AX to DX then to CX
        mov DX, AX
        mov AX,BX
        shl eax,16
        mov ax,cx
        ;we now have (f*g-a*b*e) in EAX and (h+c*d) in DX 
        mov ECX, 0
        mov CX,DX
        mov DX,0
        ;we now divide by ECX
        div ECX
        ; now we hhave 6 in DX and -2 in AX, teoretically
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
