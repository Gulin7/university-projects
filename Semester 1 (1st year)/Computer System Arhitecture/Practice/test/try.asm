bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit  , printf, scanf, fread, fwrite, fscanf, fprintf, fopen, fclose             
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf  msvcrt.dll
import fopen  msvcrt.dll
import fclose msvcrt.dll
import fread msvcrt.dll
import fwrite msvcrt.dll
import fscanf msvcrt.dll
import fprintf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; Se citeste de la tastatura un nume de fisier input.txt si un caracter c. Fisierul input.txt contine cuvinte separate prin #. Sa se scrie in fisierul output.txt doar cuvintele in care apare caracterul c citit pe a treia pozitie (adica apare ca a treia litera din cuvant).
    ; input.txt: borcan#ridichi#padurar#para   c: r     output.txt: borcan#para
    input_name resb 100
    output_name db "output.txt", 0
    s_format db "%s", 0
    c_format db "%c", 0
    write_mode db "w", 0
    read_mode db "r", 0
    input_descriptor resd 1
    write_descriptor resd 1
    print_format db "Enter a file name: ", 0
    char_format db "Enter a character: ", 0
    char db 0
    text resb 100
    citit resb 1


; our code starts here
segment code use32 class=code
    start:
        push dword char_format
        call [printf]
        add esp, 4*1

        push dword char
        push dword c_format
        call [scanf]
        add esp, 4*2

        push dword print_format
        call [printf]
        add esp, 4*1

        push dword input_name
        push dword s_format
        call [scanf]
        add esp, 4*2

        ; OPENING THE FILES
        push dword read_mode
        push dword input_name
        call [fopen]
        add esp, 4*2
        mov [input_descriptor], eax
        
        push dword write_mode
        push dword output_name
        call [fopen]
        add esp, 4*2
        mov [write_descriptor], eax
        
        ; PARSING THE FILE
        ;mov edi, text
        ;loop.:
        ;push dword citit
        ;push dword 1
        ;push dword 1
        ;push dword [input_descriptor]
        ;call [fread]
        ;add esp, 4*4
        ;cmp eax, 0
        ;je end
        ;mov al, byte[citit]
        ;stosb
        ;jmp loop.
        ;end:
        
        push dword text
        push dword s_format
        push dword [input_descriptor]
        call [fscanf]
        add esp, 4*3
        
        ;mov al, 0
        ;stosb ; we put '\0' at the end of the text string
        
        push dword text
        push dword s_format
        push dword [write_descriptor]
        call [fprintf]
        add esp, 4*3

        ; CLOSING THE FILES
        push dword [input_descriptor]
        call [fclose]
        add esp, 4*1
        
        push dword [write_descriptor]
        call [fclose]
        add esp, 4*1

        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to 