import os

# Limpar a tela
os.system("clear")

# Cabeçalho do sistema
print("=" * 132, "\n")
print("Sistema de sincronização entre a Urna Eletrônica e o Terminal do Mesário".upper().center(132), "\n")
print("=" * 132, "\n")

# Sincronização
print("\nPasso único: Gerar chave global para a comunicação entre as urnas eletrônicas\n")
os.system("openssl genpkey -genparam -algorithm DH -out pendrive/chave-global.pem")

# Encerrar o programa
print("\n")
print("Operação finalizada")