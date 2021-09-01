#!/bin/bash

SRC=$1
echo "[+] Compiling $SRC macho64 with yasm..."
yasm -f macho64 -l "$SRC.lst" "$SRC.asm"
echo "[+] Linking $SRC.o ..."
ld -lSystem -o "$SRC" "$SRC.o"
echo "[+] Done"

