https://fly.io/blog/deploying-django-to-production/

fly launch
fly secrets list
fly deploy
fly secrets set ALLOWED_HOSTS="{{cookiecutter.deploy_domain}}.fly.dev"
fly secrets set CSRF_TRUSTED_ORIGINS="https://{{cookiecutter.deploy_domain}}.fly.dev"
fly open

TODO:
github actions para fazer o deploy
