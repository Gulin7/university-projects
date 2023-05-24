bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fprintf, fclose, fwrite               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import fwrite msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    file_name db 'suciu_te_iubesc_mult.txt', 0
    access_mode db 'w', 0
    text db 'Mint', 0   
    file_descriptor resd 1
    format db '%s', 0
; our code starts here
segment code use32 class=code
    start:
        push dword access_mode
        push dword file_name
        call [fopen]
        add esp, 4*2
        
        mov [file_descriptor], eax
        
        push dword text
        push dword format
        push dword [file_descriptor]
        call [fprintf]
        add esp, 4*3
        
        push dword [file_descriptor]
        call [fclose]
        add esp, 4*1
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
