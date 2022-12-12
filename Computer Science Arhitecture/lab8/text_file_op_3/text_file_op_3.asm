bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
extern fopen, fclose, printf, fscanf
import fopen msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll
import fscanf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; A text file is given. Read the content of the file, count the number of even digits and display the result on the screen. The name of text file is defined in the data segment.
    input_file db "input.txt", 0
    modread db "r", 0
    f dd 0
    format db "%d", 0
    total dd 0
    n resd 1
    print_format db 'The total number of even numbers is %d', 0

; our code starts here
segment code use32 class=code
    start:
        ; ...
        push dword modread
        push dword input_file
        call [fopen]
        add esp, 4*2
        cmp eax, 0
        je out
        mov [f], eax
        repeat:
            ; read a number
            push dword n
            push dword format
            push dword[f]
            call [fscanf]
            add esp, 4*3
            ; compare eax to 0
            cmp eax, 0
            je error ; jump if eax == 0 cause that means it didnt read a nuber
            mov ebx, [n] 
            test ebx, 1
            jnz odd
            add dword[total], 1
            odd:
        jmp repeat
        error:
        mov eax, [total]
        ;print the total
        push dword[total]
        push dword format
        call[printf]
        add esp, 4*2
        out:
        ;close the file
        push dword[f]
        call [fclose]
        add esp, 4
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
