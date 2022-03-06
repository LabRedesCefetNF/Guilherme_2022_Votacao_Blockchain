import os

# Limpar a tela
os.system("clear")

# Cabeçalho do sistema
print("=" * 104, "\n")
print("Assinatura da cédula".upper().center(104), "\n")
print("=" * 104, "\n")

# Validar assinatura da cédula e identificação do eleitor
chave = input("Chave pública do eleitor: ")
os.system("wget http://192.168.67.150/~aluno/%s" % chave)
prompt = "openssl dgst -sha512 -verify %s -signature pendrive/voto-secreto.sign pendrive/voto-secreto.hash" % chave
os.system(prompt)

# Assinar a cédula
chave = input("Chave privada do mesário: ")
prompt = "openssl dgst -sha512 -sign pendrive/%s -out pendrive/voto-secreto.sign pendrive/voto-secreto.hash" % chave
os.system(prompt)

print("Sua cédula esta assinada com sucesso.")
print("O eleitor deve se dirigir para a urna de depósito.")