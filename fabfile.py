from fabric.api import env, roles, run, sudo, cd, prefix
from contextlib import contextmanager as _contextmanager

env.roledefs = {
    'web': ['162.243.112.133', ]
}
env.directory = '/var/www/jworld'
env.activate = 'source /home/jovani/.virtualenvs/jworld/bin/activate'
env.ini_file = '/etc/uwsgi/vassals/jworld.ini'
env.user = 'jovani'


@_contextmanager
def virtualenv():
    with cd(env.directory):
        with prefix(env.activate):
            yield


@roles('web')
def deploy():
    with virtualenv():
        # Checkout latest code
        run('git checkout master')
        run('git pull origin master')
        run('pip install -r requirements.txt')

        # Collect static files
        run('./manage.py collectstatic --link --noinput')

        # Run migrations
        # run('./manage.py migrate')

    sudo('touch {}'.format(env.ini_file))

