bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf, fopen, fclose, fscanf, fread
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fscanf msvcrt.dll
import fread msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; A text file is given. Read the content of the file, determine the lowercase letter with the highest frequency and display the letter along with its frequency on the screen. The name of text file is defined in the data segment.
    ; our code starts here
    input_file db 'given_file.txt', 0
    modread db 'r', 0
    handle1 dd -1
    format db '%s', 0
    lowercase_letters times 31 db 0
    letter resb 1
    highest_frequency db 0
    highest_frequency_letter resb 1
    print_format db 'The highest frequency lowercase is: %s , having the frequency %d', 0
    
segment code use32 class=code
    start:
        ; OPEN AN INPUT_FILE WITH READ MODE
        push dword modread
        push dword input_file
        call [fopen]
        add esp, 4*2
        mov [handle1], EAX
        cmp EAX, 0
        je the_end
        ; READ THE CONTENTS OF THE FILE
        repeat1:
        push dword[handle1]
        push dword 1
        push dword 1
        push dword letter
        call [fread]
        add esp, 4*4
        cmp eax, 0
        je error
        ; see if letter is lowercase
        cmp byte[letter], 97
        jb not_lowercase
        cmp byte[letter], 122
        ja not_lowercase
        ; add 1 to letter['actual_letter_in_ascii']
        mov edx, [letter]
        sub edx, 97
        add byte[lowercase_letters+edx], 1
        not_lowercase:
        jmp repeat1
        ;
        error:
        push dword [handle1]
        call [fclose]
        add esp, 4*1
        ;
        ; parse through lowercase_letters
        mov ecx, 31
        mov dl, 31
        parseinput:
        mov al, [highest_frequency]
        cmp byte[ecx+lowercase_letters], al
        jb not_frequent; jump below
        ;mov highest_frequency, byte[ecx+lowercase_letters]
        mov bl, 'a'
        add bl, dl
        mov byte[highest_frequency_letter], bl
        not_frequent:
        sub dl, 1
        loop parseinput
        ;print the highest_frequency_letter
        push dword [highest_frequency]
        push dword [highest_frequency_letter]
        push dword print_format
        call [printf]
        add esp, 4*3
        ;the_end is for errors along the code
        the_end:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
