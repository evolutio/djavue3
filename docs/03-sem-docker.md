# 📦 D-Jà Vue sem Docker

Se quiser saber mais sobre a diferença entre SEM ou COM Docker, [leia mais aqui](./02-iniciando.md#🐋-diferenca-entre-executar-localmente-com-docker-ou-sem-docker-containers)

## 📦 Executando o 🦄 backend sem usar Docker

**Requesitos:**
- Git
- Python +3.9  (para o backend)
- Node JS +14 (para o frontend - em uma etapa seguinte)
- um terminal shell (por ser um terminal linux, um terminal WSL no Windows ou um PowerShell), ⚠️ PowerShell pode ocorrer algumas diferenças nos comandos

::: tip
Você pode usar qualquer versão do Python, contudo, o ideal seria usar localmente a mesma versão do Python que será usada no ambiente de produção. Por este motivo, você pode escolher a versão de Python na instalação. 💡 No arquivo `Dockerfile` é possível verificar a versão de Python que será utilizado no ambiente de produção (inclusive é possível alterar se necessário).


::: code-group

```dockerfile [Dockerfile]
FROM python:3.10-slim
...

```
🌈 DICAS/TRUQUES: Você pode instalar um versão específica de Python para a sua máquina ou usar uma ferramenta como [Pyenv](https://github.com/pyenv/pyenv) ou [asdf](https://github.com/asdf-vm/asdf) para instalar/manusear múltiplas versões de Python uma para cada projeto que você possa trabalhar.

:::

O projeto **twitterclone** foi criado anteriormente, e para dar continuidade é necessário entrar dentro do diretório do projeto. Veja ...

```shell
cd twitterclone/
```

Na sequência vamos criar um ambiente virtual Python para o backend e instalar as dependências: 

::: warning
⚠️ **Não esqueça de ativar** o ambiente (`source .venv/bin/activate`), caso você esqueça de ativar as dependências serão instaladas na sua máquina fora do ambiente virtual do seu projeto.

:::

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

Com o ambiente virtual Python pronto, você pode usar o comando `pip freeze` e verificar se todas as dependências python foram instaladas. Outro ponto importante a ser feito neste momento é executar um formatador de código (`lint`) para garantir que todo o código está correto. 

```shell
black twitterclone/
```
::: info
👉 Lembre-se que o nome `twitterclone/` pode ser diferente baseado no que na resposta que você deu ao nome do projeto (`twitterclone`)

:::
Agora está na hora de rodar as migrações, ou melhor, criar as tabelas iniciais dentro do banco de dados (baseado no aquivo models). Basicamente os modelos que o Django têm, tais como, **Users**, **Sessions** e também o modelo inicial do nosso projeto, no nosso caso a tabela **Tweets**. O comando `migrate` do Django irá ler todas as migrações e criar as tabelas correspondentes. 

::: info
Para este projeto, o banco de dados padrão é o SQLITE caso tenhamos respondido `yes` e também `2` para as seguintes opções:

```shell{2,6}
  ...
  [14/27] use_sqlite_local_env (no): yes
  ...
  [21/27] Select docker_usage
    1 - 🐳 use docker by default
    2 - 📦 use venv npm by default
    Choose from [1/2] (1): 2
  ...
```
👉 Caso precise alterar para o banco Postgres, não esqueça que não será necessário recriar todo o projeto novamente, será necessário apenas mudar o arquivo `.env`
:::

Rodar as migrações para todas as apps Django:

```shell
./manage.py migrate
```
E rapidamente teremos nossa base de dados criada, então podemos criar um novo usuário:

```shell
./manage.py createsuperuser
Usuário: admin
Endereço de email: admin@example.br
Password: ********** 
Password (again): **********
Superuser created successfully.
```
Finalmente podemos rodar o projeto localmente:

```shell
./manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 17, 2023 - 08:39:10
Django version 4.1.7, using settings 'dashboardtarget.dashboardtarget.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
👉 abra seu browser e acesse a url `http://localhost:8000`, a aplicação deve estar em execução

![local-env-without-docker-localhost-8000](./images/local-run-without-docker-localhost-8000.jpg)

**Outra coisa que você pode fazer neste momento:**
- acessar a url `http://localhost:8000/admin` e depois de logar (usando o usuário que criamos antes) abrir o Administrador do Django
- executar o comando `pytest` para passar todos os testes criados no backend
- executar o comando `./manage.py shell_plus --ipython --print-sql` e executar codigos, tais como:
  - `Tweet.objects.all()` ou 
  - `Tweet.objects.create(description="My first post using djavue")`

::: info
👉 Lembre o nome `Tasks` no código `Tasks.objects.all()` é o nome do modelo que você escolheu ou pode ser diferente no seu caso. Caso tenha escolhido outro nome.

:::

- Acesse a url `http://localhost:8000/api/docs` e verifique a documentação da API
- Acesse a url `http://localhost:8000/api/posts/tweets/list` e obtenha a lista de tweets criadas na API de backend
::: info
👉 Novamente os nomes `posts` e `tweets` podem ser diferentes baseado nas suas respostas para app_name and model_name

:::
::: info
👉  Se você obter a receber a mensagem:
`{"detail": "Unauthorized"}` quando acessar a url `http://localhost:8000/api/posts/tweets/list`, você pode acessar a url `http://localhost:8000/admin/login/`  e logar usando o usuário que você criou com o comando `createsuperuser` e fazer uma nova tentativa.
:::


## 📦 Executando o ⚡️ frontend sem usar Docker

**Requisitos:**
- Git
- Node JS +14 (para o frontend)
- um terminal shell (por ser um terminal linux, um terminal WSL no Windows ou um PowerShell), ⚠️ PowerShell pode ocorrer algumas diferenças nos comandos
- O backend em execução

Abra um segundo terminal (no primeiro deverá estar rodando o backend). Navegue dentro do diretório do projeto e na pasta do frontend. 

```shell
cd twitterclone/frontend
```

Use o `npm` para instalar todas as dependências do frontend. Observe que as dependências estão listadas dentro do arquivo `package.json`. Observe também que o ambiente deste projeto, comparado com o diretório .venv que foi criado para armazenar todas as dependências do backend, para projetos de frontend, este diretório é `node_modules` e não precisamos criar ou informar qualquer coisa. Por default este diretório será criado depois de executarmos o seguinte comando.

```shell
npm install 
```
Agora vamos executar o frontend usando vite

```shell
npm run dev
  VITE v4.4.11  ready in 669 ms
  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
  ➜  press h to show help

```

**FEITO!! 🎉🎉** O frontend está rodando

👉 Abra seu browser e acesse a url `http://localhost:3000` (ou o ip de sua máquina + a porta se estiver com --host) para solicitar o aplicativo frontend!
Deveria estar rodando agora.

![local-env-without-docker-localhost-3000](./images/local-run-without-docker-localhost-3000.jpg)

::: info
📱 O template D-Jà Vue tem como objetivo ser 'MOBILE FIRST', ou seja, funcionar bem em dispositivos movéis.
:::

::: tip

🌈 DICAS/TRUQUES: Como uma alternativa podemos usar o comando `npm run dev -- --host`
que disponibilizará o aplicativo para sua rede, desta maneira você pode usar o endereço ip da sua máquina para acessar o aplicativo de qualquer máquina ou telefone celular dentro da mesma rede de WIFI.
:::

::: tip
você pode usar qualquer versão do Node JS, contudo, o ideal seria usar localmente a mesma versão do Node JS que será usada no ambiente de produção. Por este motivo, você pode escolher a versão na instalação. 💡 No arquivo `frontend/Dockerfile` é possível verificar a versão de produção (inclusive é possível alterar se necessário).


::: code-group

```dockerfile [frontend/Dockerfile]
FROM node:16.17-slim
...

```

🌈 DICAS/TRUQUES: você pode instalar um versão específica do node em sua máquina ou usar uma ferramenta como [NVM](https://github.com/nvm-sh/nvm), [nodist](https://github.com/nullivex/nodist) e [asdf](https://github.com/asdf-vm/asdf) para instalar/manusear multiplas versões, para cada projeto use uma versão específica.
:::

**Outra coisa que você pode fazer neste momento:**
- Usar `npm run format` para executar um formatador de código (Prettier) e corrigir alguns possíveis erros na formatação de estilo      
- Usar `npm run lint` para executar o linter e verificar se algum código não está seguindo as regras.
- Usar `npm run test:unit` para executar os testes do frontend
- Usar `npm run build` que irá gerar o diretório `dist` que contém html+css+js final a ser publicado.


