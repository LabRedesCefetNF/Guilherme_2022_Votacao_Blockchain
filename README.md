# Sistema eletrônico de votação baseado em blockchain

Este é um sistema utilizado como prova de conceito para um hipotético sistema eletrônico de votação política, baseado em blockchain e com a implementação de assinatura cega, com o objetivo de prover maior segurança da informação ao processo eleitoral. O sistema foi desenvolvido como como parte dos requisitos necessários à obtenção do certificado de Bacharel em Sistemas de Informação, do curso de Graduação em Sistemas de Informação, do Centro Federal de Educação Tecnológica Celso Suckow da Fonseca (CEFET/RJ).



## Instruções

Para utilizar este sistema serão necessárias 4 máquinas virtuais configuradas com um sistema operacional da distribuição Linux (preferencialmente Ubuntu). Certifique-se de que o [Python 3.6](https://www.openssl.org/source/) (ou uma versão superior) e o [OpenSSL](https://www.openssl.org/source/) estão instalados em suas máquinas por padrão. Caso contrário, instale você mesmo a partir das instruções dos links.

Cada pasta deste repositório representa o conjunto de arquivos que deve ser armazenado em cada máquina virtual:

- Máquina virtual 1: [servidor central da autarquia responsável pela eleição](central)
- Máquina virtual 2: [terminal do mesário, na seção eleitoral](terminal-mesario)
- Máquina virtual 3: [terminal de escolha do candidato, na seção eleitoral](terminal-escolha)
- Máquina virtual 4: [terminal de depósito do voto, na seção eleitoral](terminal-deposito)

Especialmente na Máquina virtual 4, será necessário instalar o [BigChainDB](https://github.com/bigchaindb/bigchaindb) e o seu [driver para Python](https://github.com/bigchaindb/bigchaindb-driver).

## Recursos adicionais
- Vídeo tutorial de instalação do BigchainDB disponível em: https://www.youtube.com/watch?v=VgtiZ1_6onU
- Texto do TCC disponível em: http://dx.doi.org/10.13140/RG.2.2.11119.41125
- Apresentação do TCC disponível em: https://www.youtube.com/watch?v=ZhFc5z73s8Q



## COPYRIGHT
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>. The licensor cannot revoke these freedoms as long as you follow the license terms:

* __Attribution__ — You must give __appropriate credit__ like below:

GUILHERME, Leonardo Pinto. __Uma proposta de sistema eletrônico de votação com Blockchain__. 2022. 47 f. Trabalho de Conclusão de Curso (Bacharelado em Sistemas de Informação) – Centro Federal de Educação Tecnológica Celso Suckow da Fonseca (CEFET/RJ), Nova Friburgo, 2022. Disponível em: http://dx.doi.org/10.13140/RG.2.2.11119.41125.



```
@phdthesis{guilherme_2022,
	address = {Nova Friburgo},
	type = {Trabalho de {Conclusão} de {Curso} ({Bacharelado} em {Sistemas} de {Informação})},
	title = {Uma proposta de sistema eletrônico de votação com {Blockchain}},
	url = {http://dx.doi.org/10.13140/RG.2.2.11119.41125},
	urldate = {2023-11-16},
	school = {Centro Federal de Educação Tecnológica Celso Suckow da Fonseca (CEFET/RJ)},
	author = {Guilherme, Leonardo Pinto},
	collaborator = {Lazarin, Nilson Mori},
	year = {2022},
}
```
