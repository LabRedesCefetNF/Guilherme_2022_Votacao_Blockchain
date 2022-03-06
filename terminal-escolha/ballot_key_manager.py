import os, time

# Limpar a tela
os.system("clear")

# Cabeçalho do sistema
print("=" * 104, "\n")
print("Sistema gerenciador de chaves pública e privada das urnas".upper().center(104), "\n")
print("=" * 104, "\n")

# Geração
print("\nPasso 1: Gerar chave privada do terminal\n")

os.system("openssl genpkey -paramfile pendrive/chave-global.pem -out chave-privada-cabine.pem")
time.sleep(0.5)
print(":::::::::: Chave privada gerada")

# Exportação
print("\nPasso 2: Exportar chave pública do terminal\n")

os.system("openssl pkey -in chave-privada-cabine.pem -pubout -out public_html/chave-publica-cabine.pem")
time.sleep(0.5)
print("--> Chave pública gerada")


# Encerrar o programa
print("\n", "Operação finalizada")