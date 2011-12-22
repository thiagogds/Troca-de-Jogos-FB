Para instalar o Postgres84 no Homero:

###################################
# Instalando Postgres84 no MacOSX #
###################################

$ sudo port install postgresql84-server

Vá beber uma água... após a instalação...

$ sudo port load postgresql84-server

Para criar o arquivo de banco de dados padrão do Postgres:

$ sudo mkdir -p /opt/local/var/db/postgresql84/defaultdb
$ sudo chown postgres:postgres /opt/local/var/db/postgresql84/defaultdb
$ sudo su postgres -c '/opt/local/lib/postgresql84/bin/initdb -D /opt/local/var/db/postgresql84/defaultdb'


###################################
# Instalando Postgres84 no Ubuntu #
###################################

$ sudo /bin/sh -c 'unset LC_ALL; LANG=pt_BR.UTF-8 apt-get install postgresql-8.4'

#########################################
# Configurando o Postgres para o Homero #
#########################################

Crie o usuário do Homero no Postgres:

$ sudo -u postgres psql template1 -c "CREATE USER homero WITH ENCRYPTED PASSWORD 'homero'"

Dê permissão para o usuário homero criar databases. Importante para rodar os testes.

$ sudo -u postgres psql postgres -c "ALTER USER homero CREATEDB;"

Crie o database do Homero no Postgres:

$ sudo -u postgres createdb "homero" -O "homero"

Quase lá! Agora você precisa configurar o settings.devel.py para utilizar este banco:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'homero',       # psql database name
            'USER': 'homero',       # psql user
            'PASSWORD': "homero",   # psql password
            'HOST': 'localhost',    # Set to empty string for localhost.
            'PORT': '',             # Set to empty string for default.
        }
    }


########################################
# Resetando o banco Postgres do Homero #
########################################

python manage.py reset_db --router=default -U postgres

