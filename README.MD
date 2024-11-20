# Projeto Base FastAPI

![Static Badge](https://img.shields.io/badge/Base_FastAPI-Projeto-brightgreen)

Projeto desenvolvido em Python com FastAPI

## Descrição

Projeto Base para aceleração de futuros desenvolvimentos de API usando FastAPI, a base contém:


- [X] Padrão de Projeto (Model,Repository,Router,Schema)

    * Models = Responsável pela estrutra da tabela de dados
    
    * Repositories = Responsável pela maneira de como acessar os dados do banco (consultas)

    * Routers = Responsável pelas Rotas da API

    * Schemas = Define um objeto de retorno tipado para API

- [X] Autenticação JWT
- [X] Proteção de Rotas
- [X] Tabela de Usuário Básica
- [X] Exemplo de Tabelas Relacionadas (User, Anime, Season)


## Uso

Clone o projeto:

```bash
git clone https://github.com/KlebersonCollab/base-fastapi.git
```
Este projeto requer Python 3.8 ou superior.
Como boa prática em python você deve executar a instalação das dependências em um ambiente virtual, crie um pelo comando ``python -m venv venv`` após isso ative o ambiente pelo comando ``venv/scripts/active`` caso esteja usando linux utilize o comando ``source venv/bin/active``


Após clonar o projeto você deve instalar as dependências do mesmo pelo comando:

```bash
pip install -r app\requirements\dev.txt
```

#### Informações úteis:

Caso tenha erro no PKG faça os processos abaixo:

* Delete a pasta venv,

* Execute o comando para criação de um novo ambiente virtual ``python -m venv venv``

* Instale o SetupTools os codigos que precisar estão abaixo.

```bash
pip install --upgrade setuptools
pip uninstall setuptools #Em caso de falha
pip install setuptools
```

## Segurança:

Altere a SECRET_KEY deste projeto pois caso sua chave se torne Pública seu projeto corre risco.

na pasta ``app/config/jwt.py`` 

Para gerar uma nova Secret rode o comando abaixo em um bash

````bash 
openssl rand -hex 32 no terminal
````

## Licença

This project is licensed under the terms of the MIT license. See the [LICENSE](LICENSE) file for details.