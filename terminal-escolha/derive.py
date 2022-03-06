import os

# Limpar a tela
os.system("clear")

# Cabeçalho do sistema
print("=" * 104, "\n")
print("Processo de derivação de chaves".upper().center(104), "\n")
print("=" * 104, "\n")

# Processo de derivação das chaves
print("Passo 2: derivação da chave pública da urna", "\n")
os.system("wget http://192.168.67.162/~aluno/chave-publica-urna.pem")
os.system("openssl pkeyutl -derive -inkey chave-privada-cabine.pem -peerkey chave-publica-urna.pem -out cabine-urna.bin")

print("\n", "Operação finalizada")