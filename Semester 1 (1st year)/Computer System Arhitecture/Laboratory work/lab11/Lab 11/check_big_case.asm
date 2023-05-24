bits 32 
global check_big_case
extern printf             
import printf msvcrt.dll

segment data use32 class=data
    big_case resb 1

segment code use32 class=code
    check_big_case:
        push ebp
        mov ebp, esp
        mov edi, 0
        mov esi, [ebp+8]
        check_loop:
            mov al, [esi]
            cmp al, 0
            je print
            cmp al, 'A'
            jb skip
            cmp al, 'Z'
            ja skip
            mov [big_case+edi], al
            inc edi
            skip:
            inc esi
            jmp check_loop
            
        print:
        cmp edi, 0
        je final
        push big_case
        call [printf]
        add esp, 4
            
    final:  
        mov esp, ebp
        pop ebp
        ret
        
