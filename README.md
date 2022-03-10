# Sistema eletrônico de votação baseado em blockchain

Este é um sistema utilizado como prova de conceito para um hipotético sistema eletrônico de votação política, baseado em blockchain e com a implementação de assinatura cega, com o objetivo de prover maior segurança da informação ao processo eleitoral. O sistema foi desenvolvido como como parte dos requisitos necessários à obtenção do certificado de Bacharel em Sistemas de Informação, do curso de Graduação em Sistemas de Informação, do Centro Federal de Educação Tecnológica Celso Suckow da Fonseca (CEFET/RJ).

O material de apresentação está disponível em [https://slides.com/lpinto39/deck](https://slides.com/lpinto39/deck)


## Instruções

Para utilizar este sistema serão necessárias 4 máquinas virtuais configuradas com um sistema operacional da distribuição Linux (preferencialmente Ubuntu). Certifique-se de que o [Python 3.6](https://www.openssl.org/source/) (ou uma versão superior) e o [OpenSSL](https://www.openssl.org/source/) estão instalados em suas máquinas por padrão. Caso contrário, instale você mesmo a partir das instruções dos links.

Cada pasta deste repositório representa o conjunto de arquivos que deve ser armazenado em cada máquina virtual:

- Máquina virtual 1: [servidor central da autarquia responsável pela eleição](https://github.com/lpinto39/blockchain-voting/tree/main/central)
- Máquina virtual 2: [terminal do mesário, na seção eleitoral](https://github.com/lpinto39/blockchain-voting/tree/main/terminal-mesario)
- Máquina virtual 3: [terminal de escolha do candidato, na seção eleitoral](https://github.com/lpinto39/blockchain-voting/tree/main/terminal-escolha)
- Máquina virtual 4: [terminal de depósito do voto, na seção eleitoral](https://github.com/lpinto39/blockchain-voting/tree/main/terminal-deposito)

Especialmente na Máquina virtual 4, será necessário instalar o [BigChainDB](https://github.com/bigchaindb/bigchaindb) e o seu [driver para Python](https://github.com/bigchaindb/bigchaindb-driver).
