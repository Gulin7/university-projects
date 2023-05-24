bits 32 

global _check_small_case        
extern _printf             


segment data use32 class=data
    small_case db 1

; our code starts here
segment code use32 class=code
    _check_small_case:
        push ebp
        mov ebp, esp
        mov edi, [ebp+12]
        mov esi, [ebp+8]
        check_loop:
            lodsb
            cmp al, 0
            je done
            cmp al, 'a'
            jb skip
            cmp al, 'z'
            ja skip
            stosb
            skip:
            jmp check_loop
            
            
        done:
        mov esp, ebp
        pop ebp
        ret