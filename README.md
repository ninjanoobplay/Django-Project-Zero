# Projeto Django

Nesse Projeto Fiz um Sistema de Login/Cadastro - Criação de Agenda De Usuário/Apagar e Consultar Dados Dessa Agenda De Usuário

Eu Adicionei Um Banco De Dados Para Fazer Cadastro/Login,Está funcionando perfeitamente!(Cada um pode fazer sua propria configuração

# Instalações Necessárias:

Recomendo Uma Versão Do Python Compativel com o Django Para Não Ter Nenhum Problema

Eu Estou Utilizando a Versão 3.10.0, Caso Queira Baixar

Basta Clicar no Icone Abaixo Para Ser Redirecionado:

[![Python 3.10.0 Download](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3100/)

Para Testes No Banco De Dados no LocalHost Utilize o padrão do django o db.sqlite3

Caso Queira usar outro banco de dados de sua preferencia recomendo ler a documentação do django sobre banco de dados e dps

Basta Passar as Infomações de Conexão No Arquivo `settings.py`

**Obs:Recomendo Utilizar Um Ambiente Virtual**

Abra o Terminal, Vá Para a Pasta Do Seu Projeto e Digite:

Para Windows:
```
python -m venv venv
```
Para Linux:
```
python3 -m venv venv
```

Pronto Agora Para Rodar o Programa Primeiro Vamos Ativar Nosso Ambiente Virtual:
```
venv\Scripts\activate
```
Caso queira sair só digitar:
```
deactivate
```

Obs: `venv` Foi o Nome que escolhemos logo em cima, E Certifique de estar na pasta do projeto!


Logo Em Seguida  Ja Pode Baixar Todas as Dependencias Para Esse Projeto com o Comando:
```
pip install -r requirements.txt
```

E Para Iniciar o Projeto

Para Windows:
```
python manage.py migrate --run-syncdb
```
Ou

```
python manage.py migrate --run-syncdb
```

Para Linux:
```
python3 manage.py migrate --run-syncdb
```

Logo Em Seguida:
```
python manage.py runserver
```
Obs: Alguns Computadores em vez de digitar **python** basta digitar **py** e o resto do comando que vai funcionar


Depois Basta Ir no Seu Navegador e Digitar:
```
localhost:8000
```

## Imagens do Layout Que Estou Utilizando:

### Login:

<img align="center" src="" width="600"/>

### Cadastro:

<img align="center" src="" width="600"/>

### Home:

<img align="center" src="" width="600"/>

### Criar Agenda:

<img align="center" src="" width="600"/>

### Consultar Agenda:

<img align="center" src="" width="600"/>



***É Basicamente Isso,Obrigado!***
