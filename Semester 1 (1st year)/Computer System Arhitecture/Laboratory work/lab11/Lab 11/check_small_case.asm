bits 32 

global check_small_case        
extern printf             
import printf msvcrt.dll


segment data use32 class=data
    small_case db 1

; our code starts here
segment code use32 class=code
    check_small_case:
        push ebp
        mov ebp, esp
        mov edi, 0
        mov esi, [ebp+8]
        check_loop:
            mov al, [esi]
            cmp al, 0
            je print
            cmp al, 'a'
            jb skip
            cmp al, 'z'
            ja skip
            mov [small_case+edi], al
            inc edi
            skip:
            inc esi
            jmp check_loop
            
            
        print:
        cmp edi, 0
        je final
        push small_case
        call [printf]
        add esp, 4
            
    final:  
        mov esp, ebp
        pop ebp
        ret