import os

# Limpar a tela
os.system("clear")

# Cabeçalho do sistema
print("=" * 132, "\n")
print("Processo de derivação de chaves".upper().center(132), "\n")
print("=" * 132, "\n")

# Processo de derivação das chaves
print("Passo 1: derivação da chave pública da urna escolha", "\n")
os.system("wget http://192.168.67.154/~aluno/chave-publica-cabine.pem")
os.system("openssl pkeyutl -derive -inkey chave-privada-urna.pem -peerkey chave-publica-cabine.pem -out cabine-urna.bin")


print("\n", "Operação finalizada!")