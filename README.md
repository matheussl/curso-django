Desenvolvimento web com Python e Django
----------------------------------------

Código-fonte do curso de Python e Django.



### Deploy com Apache2 + wsgi + PostgreSQL

##### Primeiro passo: instalar as dependências!


    $ sudo apt-get install python-pip python-dev build-essential
    $ sudo easy_install --upgrade pip

    $ pip install virtualenv
    $ pip install virtualenvwrapper

Abra o bash_profile

    $ sudo nano ~/.bash_profile

insira as linhas abaixo:

    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh

Carregue o arquivo

    $ source ~/.bash_profile


###### Instalando Apache2 e PostgreSQL

    $ sudo apt-get install apache2 apache2.2-common apache2-mpm-prefork apache2-utils libexpat1 libapache2-mod-wsgi postgresql libpq-dev

    $ sudo service apache2 restart


###### Criando um ambiente virtual pro projeto

$ mkvirtualenv myprojectenv --no-site-packages



Faça o upload do projeto (pode ser com git).

Instale as dependências do projeto

    $ cd /home/django_projects/MyProject/
    $ workon myprojectenv
    $ pip install -r requirements.txt


###### Configurando o PostgreSQL

Mude a senha do usuário

    $ sudo -u postgres psql postgres
    $ \password postgres

Crie a base de dados

    $ sudo -u postgres createdb mydb


##### Configurando o Apache


Crie um virtual host no apache

    $ sudo nano /etc/apache2/sites-available/mydomain.com

E insira o conteúdo a seguir, substituindo os caminhos pro caminho do seu projeto

    <VirtualHost *:80>
        ServerAdmin webmaster@mydomain.com
        ServerName mydomain.com
        ServerAlias www.mydomain.com
        WSGIScriptAlias / var/www/mydomain.com/index.wsgi

        Alias /static/ /var/www/mydomain.com/static/
        <Location "/static/">
            Options -Indexes
        </Location>

        Alias /media/ /var/www/mydomain.com/media/
        <Location "/media/">
            Options -Indexes
        </Location>
    </VirtualHost>



Agora precisamos criar o módulo wsgi que o Apache utilizará.

    $ sudo nano /var/www/mydomain.com/index.wsgi

Adicione o script abaixo:

    import os
    import sys
    import site

    # Add the site-packages of the chosen virtualenv to work with
    site.addsitedir('~/.virtualenvs/myprojectenv/local/lib/python2.7/site-packages')

    # Add the app's directory to the PYTHONPATH
    sys.path.append('~/django_projects/MyProject')
    sys.path.append('~/django_projects/MyProject/myproject')

    os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

    # Activate your virtual env
    activate_env=os.path.expanduser("~/.virtualenvs/myprojectenv/bin/activate_this.py")
    execfile(activate_env, dict(__file__=activate_env))

    import django.core.handlers.wsgi
    application = django.core.handlers.wsgi.WSGIHandler()


Colete arquivos estáticos

    $ python manage.py collectstatic


Restart o apache

    $ sudo service apache2 restart


O deploy está concluído.



#### Observações


* É uma boa prática ter um "settings.py", "wsgi.py" e "requirements.txt" só para produção;
* Existe um projeto chamado "django-fab-deploy" que automatiza todo esse processo;




### Deploy com nginx + gunicorn + wsgi + PostgreSQL

A instalação do PostgreSQL é idêntica ao anterior.


##### Intalando dependências

    $ pip install gunicorn nginx



##### Testando a aplicação
    
    $ gunicorn_django -b 0.0.0.0:8000



##### Configurando

Em produção você pode criar um script pra ativar o ambiente virtual e executar o gunicorn:

    #!/bin/bash
    set -e
    LOGFILE=/var/log/gunicorn/hello.log
    LOGDIR=$(dirname $LOGFILE)
    NUM_WORKERS=3
    # user/group to run as
    USER=your_unix_user
    GROUP=your_unix_group
    cd /path/to/test/hello
    source ../bin/activate
    test -d $LOGDIR || mkdir -p $LOGDIR
    exec ../bin/gunicorn_django -w $NUM_WORKERS \
    --user=$USER --group=$GROUP --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE


Adicione um proxy reverso no Nginx pra poder servir arquivos estáticos

    server {
        listen 80;
        server_name example.org;
        access_log  /var/log/nginx/example.log;

        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }

        # change /static/ to your static folder name
        location /static/ {
            root /path/to/your/django/project;
            autoindex off;
            expires 1M;
        }

        # change /media/ to your media folder name
        location /media/ {
            root /path/to/your/django/project;
            autoindex off;
            expires 1M;
        }
      }


Está feito o deploy.


##### Observações

* Você pode utilizar o supervisor pra iniciar o processo do Gunicorn;
* Tem um projeto chamado django-fagungis que automatiza todo o deploy com Django + Gunicorn + Supervisor + Nginx