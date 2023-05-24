bits 32 
global _check_big_case
extern _printf             

segment data public use32 class=data
    big_case db 1

segment code public use32 class=code
    _check_big_case:
        push ebp
        mov ebp, esp
        mov edi, [ebp+12]
        mov esi, [ebp+8]
        check_loop:
            lodsb
            cmp al, 0
            je done
            cmp al, 'A'
            jb skip
            cmp al, 'Z'
            ja skip
            stosb
            skip:
            jmp check_loop
            
        done:
        mov esp, ebp
        pop ebp
        ret
        
