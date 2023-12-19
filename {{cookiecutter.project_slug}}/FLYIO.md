https://fly.io/blog/deploying-django-to-production/

Requisitos:
- Conta no Fly.io
- Plano que permita 2 apps rodando (django + postgres)
- flyctl instalado (https://fly.io/docs/hands-on/install-flyctl/)
- fazer login via terminal (https://fly.io/docs/hands-on/sign-in/)

fly launch
fly secrets list
fly secrets set ALLOWED_HOSTS="{{cookiecutter.deploy_domain}}"
fly secrets set CSRF_TRUSTED_ORIGINS="https://{{cookiecutter.deploy_domain}}"

update the fly.toml start cmd by:
release_command = "bash -c \"python manage.py migrate --noinput && python manage.py collectstatic --noinput\""

fly deploy
fly open

Para fazer deploy via Github Actions (CD)
- Criar uma API TOKEN no dashboard do app no Fly.io
- Adicionar FLY_API_TOKEN no GitHub Actions Secrets

OTHERS COMMANDS:
fly status
fly ssh console -a {{cookiecutter.project_slug}}
fly logs --debug
 