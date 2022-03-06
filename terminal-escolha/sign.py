import os

# Limpar a tela
os.system("clear")

# Cabeçalho do sistema
print("=" * 104, "\n")
print("Assinatura da cédula de votação".upper().center(104), "\n")
print("=" * 104, "\n")

# Calcular a hash
os.system("sha512sum pendrive/voto-secreto.bin > pendrive/voto-secreto.hash")

# Assinar a cédula
chave = input("Insira a sua chave privada para assinar a sua cédula: ")
prompt = "openssl dgst -sha512 -sign pendrive/%s -out pendrive/voto-secreto.sign pendrive/voto-secreto.hash" % chave
os.system(prompt)

print("Sua cédula esta assinada com sucesso.")
print("Dirija-se ao mesário para dar prosseguimento ao processo.")