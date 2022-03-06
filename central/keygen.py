import os


class KeyGen:

    def __init__(self, nie):
        self.__nie = nie

    def gen_key_pair(self):
    
        print("\nPasso 1: Gerar chave privada do eleitor\n")
        prompt = "openssl genrsa -aes-256-cbc -out %s 4096" % self.private_key_file()
        os.system(prompt)
        
        print("\n\n")
        
        print("\nPasso 2: Gerar chave pública do eleitor\n")
        prompt = "openssl rsa -in %s -pubout -out %s" % (self.private_key_file(), self.public_key_file())
        os.system(prompt)
        
        print("\nOperação finalizada\n")

    def private_key_file(self):
        return 'pendrive/%s_private.pem' % self.__nie

    def public_key_file(self):
        return 'public_html/%s_public.pem' % self.__nie 


# Limpar a tela
os.system("clear")

# Descrição do sistema
print("=" * 132, "\n")
print("Sistema gerador de par de chaves pública e privada".upper().center(132), "\n")
print("=" * 132, "\n")

# Início do processo de geração de par de chaves
nie = int(input("Informe o Número de Inscrição do Eleitor: "))
chave = KeyGen(nie)
chave.gen_key_pair()