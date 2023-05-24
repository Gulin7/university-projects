bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ;Two natural numbers a and b (a: dword, b: dword, defined in the data segment) are given. Calculate a/b and display the remainder in the following format: "<a> mod <b> = ;<remainder>". Example: for a = 23, b = 5 it will display: "23 mod 5 = 3".
    ;The values will be displayed in decimal format (base 10) with sign.
    a dd 23
    b dd 5
    result dd 0
    format db '%d mod %d = %d', 0

; our code starts here
segment code use32 class=code
    start:
        mov EAX, dword[a]
        mov EDX, 0
        mov EBX, dword[b]
        div EBX ; in EDX we have the remainder
        ;mov ECX, dword[a]
        ;mov ebx, dword[b]
        ;push dword EDX
        ;push dword EBX
        ;push dword ECX
        ;push format
        ;----------------
        ;PUSH ON REVERSE C ORDER THE PARAMETERS  
        mov [result], edx
        push dword[result]
        push dword[b]
        push dword[a]
        push dword format
        ;CALL THE FUNCTIONS PRINTF
        call [printf]
        add esp, 4*4
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
