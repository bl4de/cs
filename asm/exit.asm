;   Program: exit
;
;   compile: yasm -f macho64 -l exit.lst exit.asm
;   link: ld -lSystem -o exit exit.o
;   

    segment .text
    global _main
_main:
    mov eax, 0x2000001
    mov edi, 5
    syscall
    end
    

