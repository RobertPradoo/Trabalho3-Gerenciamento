# Trabalho Avaliativo Gerência da Configuração 2
## Integrantes:
- Bruno Martins
- Luana Reginato Bassanesi
- Robert Prado
- Alisson Colombo
- Nathália Menegol Teles

>  **Universidade de Caxias do Sul, Gerência da Configuração**

>  ***Caxias do Sul, 2025***


## Ferramentas
Controle de versão de código: Git
Gerenciamento do repositório: GitLab
Banco de Dados relacional: SQLite e Django (Python)

## Como usar o projeto
Esse projeto foi criado para o estudo da gestão de configuração, trabalhando com ferramentas diferentes das apresentadas em aula, controle de versão de banco de dados e alteração através de mutations.

*Siga os passos da instalação do ambiente e as regras de fluxo de trabalho e contibuição.*

## Instalação e configurações
#### Linux
instale o git na sua máquina:

```
sudo apt-get install git-all
```

verifique se o Python 3 já está instalado na sua máquina:
```
python3 --version
```

caso não, instale:
```
sudo apt install python3.13
```

instale as dependências do projeto:
```
source .venv/bin/activate
pip install -r requirements.txt
```

#### Windows
instal o git na sua máquina a partir do link:

##### [install git](https://git-scm.com/downloads/win)

verifique se o Python 3 já está instalado na sua máquina:
```
python3 --version
```

caso não, instale:

##### [install python3](https://www.python.org/downloads/)

instale as dependências do projeto:
```
source .venv/bin/activate
pip install -r requirements.txt
```

#### MacOS
instale o git na sua máquina a partir do link:

##### [install git](https://git-scm.com/downloads/mac)

instale o Python 3:
```
brew install python
```

instale as dependências do projeto:
```
source .venv/bin/activate
pip install -r requirements.txt
```

## Fluxo de trabalho
#### Nomenclatura de branchs:
- ***main***: branch principal
- ***feat/nome-da-feature***: funcionalidades novas
- ***fix/nome-do-fix***: consertos de bugs

#### Nomenclatura de commits:
- ***feat: descrição da alteração***: funcionalidades novas
- ***fix: descrição da alteração***: consertos de erros
- ***refac: descrição da alteração***: simplificação ou reestruturação do código
- ***chore: descrição da alteração***: demais tarefas cotidianas

#### Fluxo
Trabalhamos com Trunked Based, ou seja, todas as branchs são criadas a partir da **main**, e para enviar as alterações para produção, são criados Pull Requests (Merge Requests no caso do GitLab) das branchs feature/fix para a main novamente. Quando as branches menores são mergeadas, são apagadas do repositório remoto automaticamente.

## Executando comandos

## Como contribuir
Crie uma branch nova e aponte um Merge Request para a branch main. Nossos desenvolvedores irão revisar sua sugestão e caso seja aprovado, será adicionado ao código fonte.