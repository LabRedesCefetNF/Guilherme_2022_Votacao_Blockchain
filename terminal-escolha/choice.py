#!/usr/bin/python

import os

# Cabeçalho do sistema
os.system("clear")
print("=" * 104, "\n")
print("Urna Eletrônica".upper().center(104))
print("Terminal da Escolha do Eleitor".upper().center(104), "\n")
print("=" * 104, "\n")

# Apresentação de informações da urna
print("Cargo: ", "Presidente da República".upper(), "\n")
print("Opções de candidatos: ", "\n")
print(" " * 5, "90 - Dumzyomu".upper())
print(" " * 5, "91 - Waoenhad".upper())
print(" " * 5, "92 - Dolcaehua".upper())
print(" " * 5, "93 - Grusaldo".upper())
print(" " * 5, "94 - Xiguel".upper())
print(" " * 5, "95 - Nimba".upper())

# Escolha do candidato pelo eleitor
escolha = int(input("\nEscolha um candidato: "))

if escolha >= 90 and escolha <= 95:
    prompt = "openssl aes-256-cbc -e -pbkdf2 -kfile cabine-urna.bin -out pendrive/voto-secreto.bin <<< '%s'" % escolha
    with open('vote.sh', 'w') as f:
        f.write(prompt)
    os.system("bash vote.sh")
    os.system("rm vote.sh")
    os.system("python3 sign.py")
else:
    print("Você invalidou a sua escolha!")
