import os, time
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

# Limpa a tela
os.system("clear")

# Valida o voto
os.system("sha512sum pendrive/voto-secreto.bin > validacao")

# Valida a assinatura
chave = input("Informe a chave pública do mesário que assinou a cédula: ")
os.system("wget http://192.168.67.150/~aluno/%s" % chave)
prompt = "openssl dgst -sha512 -verify %s -signature pendrive/voto-secreto.sign validacao" % chave
os.system(prompt)

# Ler o voto
os.system("openssl aes-256-cbc -pbkdf2 -d -kfile cabine-urna.bin -in pendrive/voto-secreto.bin > voto")

f = open("voto", "r")
voto = f.read()
voto = voto.strip()

text= "Você escolheu o candidato %s." % voto
print(text)

# Guardar o voto

bdb = BigchainDB('http://127.0.0.1:9984')
elector = generate_keypair()
tx = bdb.transactions.prepare(
    operation='CREATE',
    signers=elector.public_key,
    asset={'data': {'voto': voto}})
signed_tx = bdb.transactions.fulfill(
    tx,
    private_keys=elector.private_key)
bdb.transactions.send_commit(signed_tx)

# Voto depositado
os.system("clear")
print("=" * 132, "\n")
print("Votaçao finalizada".upper().center(132), "\n")
print("=" * 132, "\n")

# Encerrar o programa
time.sleep(1)
print("\nO seu processo de votação foi encerrado.\n")
