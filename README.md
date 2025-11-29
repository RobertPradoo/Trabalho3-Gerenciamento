# Trabalho Avaliativo Gerência da Configuração
## Integrantes:
- Bruno Martins
- Luana Reginato Bassanesi
- Robert Prado
- Alisson Colombo
- Nathália Menegol Teles

>  **Universidade de Caxias do Sul, Gerência da Configuração**

>  ***Caxias do Sul, 2025***

---

## Sobre o Projeto
Este projeto é a continuação do trabalho de gestão de configuração. Nesta etapa, o foco é a implementação de pipelines de CI/CD, ambientes distintos de deploy e gerenciamento de banco de dados via migrações automatizadas.

O sistema consiste em uma página HTML disponibilizada via deploy automático e um banco de dados relacional atualizado via pipelines.

## Ferramentas Utilizadas
* **Controle de versão de código:** Git
* **Gerenciamento do repositório:** GitHub
* **Automação e Pipelines:** GitHub Actions
* **Banco de Dados:** [inserir banco de dados]
* **Hospedagem (Web):** Vercel
* **Linguagem/Framework:** Python (Django)

## Infraestrutura e Ambientes
Para atender aos requisitos de entrega contínua, a infraestrutura foi dividida em três ambientes isolados. Cada branch corresponde a um ambiente de deploy com sua própria instância de banco de dados e URL da página web.

| Ambiente | Branch | Trigger (Gatilho da Pipeline) | Descrição |
| :--- | :--- | :--- | :--- |
| **Desenvolvimento** | `dev` | **Manual** | Ambiente para testes iniciais e validação de features pelos desenvolvedores. |
| **Pré-Produção** | `preprod` | **Agendado (Cron)** e **Manual** | Ambiente de homologação. A pipeline roda automaticamente todos os dias às 00:00 UTC e permite execução manual. |
| **Produção** | `main` | **Push/Commit** e **Pull Request** | Ambiente final. Atualizado sempre que há uma nova versão estável mergeada na branch principal. |

## Documentação das Pipelines

As pipelines foram configuradas no diretório `.github/workflows`. Cada arquivo YAML (`dev.yml`, `preprod.yml`, `main.yml`) é responsável por gerenciar um ambiente específico.

### O que a pipeline faz?
Independentemente do ambiente, o fluxo de execução segue os seguintes passos automatizados:

1.  **Checkout:** O código fonte da branch correspondente (main, preprod ou dev) é baixado no servidor de automação (Ubuntu Latest).
2.  **Configuração do Ambiente de Deploy:**
    * Utiliza a action setup-node para preparar o ambiente.
    * Instala o pacote global do Vercel CLI via npm (npm i -g vercel).
3.  **Deploy na Vercel:**
    * Autentica-se utilizando o token seguro (VERCEL_TOKEN).
    * Executa o comando de deploy (npx vercel --prod), que envia os arquivos estáticos e o código para os servidores da Vercel, vinculando-os ao projeto e organização configurados.

---

## Estrutura de Banco de Dados
[preencher]

---

## Como usar o projeto

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

faça uma migração:
```
pyhton3 manage.py migrate
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
faça uma migração:
```
pyhton3 manage.py migrate
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

faça uma migração:
```
pyhton3 manage.py migrate
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

criação de nova migração:

```
python3 manage.py makemigrations
```

aplique uma migração:
```
python3 manage.py migrate
```


## Como contribuir
Crie uma branch nova e aponte um Merge Request para a branch main. Nossos desenvolvedores irão revisar sua sugestão e caso seja aprovado, será adicionado ao código fonte.
