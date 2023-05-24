bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, fopen, fwrite, fclose, fprintf              ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import fopen msvcrt.dll
import fwrite msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; A file name and a text (defined in the data segment) are given. The text contains lowercase letters, uppercase letters, digits and special characters. Transform all the uppercase letters from the given text in lowercase. Create a file with the given name and write the generated text to file.
    file_name db 'problem44lab8.txt',0
    write_mode db 'w',0
    file_descriptor resd 1
    text db 'sA MA SUGI DE pula nasm 69 fac cu mama ta!', 0 ; 5 uppercase letters, 7 lowercase, 2 digits, 1 special
    text_len equ $-text
    result resb 69

    format_for_file db '%s', 0
    ;'caca'
; our code starts here
segment code use32 class=code
    start:
        ;OPEN FILE
        push dword write_mode
        push dword file_name
        call [fopen]
        add esp, 4*2
        
        mov [file_descriptor], eax
        
        mov esi, text
        mov edi, result
        mov ecx, text_len
        loop.:
            lodsb ; in AL we have the current byte
            cmp al, 'A'
            jb not_good
            cmp al, 'Z'
            ja not_good
            add al, 32
            not_good:
            stosb
            ; we put it in result
        loop loop.
        ;NOW WE WRITE IN FILE
        push dword result
        push dword format_for_file
        push dword [file_descriptor]
        call [fprintf]
        add esp, 4*3
       
        ;CLOSE FILE
        push dword [file_descriptor]
        call [fclose]
        add esp, 4*1
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
