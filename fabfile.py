import os
import pwd

from fabric.api import cd, env, task, require, run, sudo, prefix, shell_env, warn_only
from fabric.contrib.files import exists, upload_template

VIRTUALENV_DIR = 'env'
CODE_DIR = 'mma-dexter'
PROD_HOSTS = ['mma-dexter.code4sa.org']

PACKAGES = [
    'build-essential',
    'python-dev',
    'libxml2-dev',
    'libxslt1-dev',
    'git-core',
    'python-pip',
    'libmysqlclient-dev',
    'libmagickwand-dev',
    'nginx',
    'rabbitmq-server',
    'python-numpy',
    'python-scipy',
    ]

@task
def prod():
    env.deploy_type = 'prod'
    # this must be an absolute directory
    env.deploy_dir = '/home/ubuntu/'
    env.branch = 'master'
    env.hosts = PROD_HOSTS
    env.user = 'ubuntu'

    env.repo_dir = os.path.join(env.deploy_dir, CODE_DIR)
    env.ve_dir = os.path.join(env.deploy_dir, CODE_DIR, VIRTUALENV_DIR)


@task
def provision():
    sudo('apt-get update')
    sudo('apt-get install --yes --no-upgrade %s' % ' '.join(PACKAGES))
    sudo('apt-get build-dep --yes --no-upgrade python-scipy')
    sudo('pip install virtualenv')

    with prefix('. %s/bin/activate' % env.ve_dir):
        # numpy must be installed before requirements.txt, otherwise
        # scikit-learn doesn't process its dependencies correctly
        # and complains that numpy isn't there
        run('pip install numpy==1.9.1')


@task
def deploy():
    require('deploy_type', 'deploy_dir', 'branch', provided_by=[prod])

    if not exists(env.repo_dir):
        with cd(env.deploy_dir):
            run('git clone https://github.com/Code4SA/mma-dexter.git')

    if not exists(env.ve_dir):
        run('virtualenv -p python2.7 --no-site-packages %s' % env.ve_dir)

    with cd(env.repo_dir):
        run('git checkout -B %s' % env.branch)
        run('git pull origin %s' % env.branch)

    with cd(env.repo_dir), prefix('. %s/bin/activate' % env.ve_dir):
        run('pip install -r requirements.txt')

    # make sure logging dir exists and update processes
    log_dir = os.path.join(env.repo_dir, 'log')
    run('mkdir -p %s' % log_dir)

    # log rotation
    sudo('ln -fs %s/resources/logrotate/dexter /etc/logrotate.d/' % env.repo_dir)

    # link in nginx config
    sudo('ln -fs %s/resources/nginx/dexter.conf /etc/nginx/sites-enabled/' % env.repo_dir)
    sudo('service nginx reload')

    # link in upstart config
    sudo('ln -fs %s/resources/upstart/dexter.conf /etc/init/' % env.repo_dir)
    sudo('ln -fs %s/resources/upstart/dexter-celery.conf /etc/init/' % env.repo_dir)
    sudo('initctl reload-configuration')

    restart()

@task
def restart():
    # on first deploy, dexter won't not be running
    sudo("kill -HUP `cat %s/gunicorn.pid` || initctl restart dexter || (initctl stop dexter; initctl start dexter)"\
            % (env.repo_dir))

    # restart dexter-celery
    with warn_only():
        sudo('initctl stop dexter-celery')
    sudo('initctl start dexter-celery')

@task
def migrate():
    require('deploy_type', 'deploy_dir', 'branch', provided_by=[prod])

    with cd(env.repo_dir), prefix('. %s/bin/activate' % env.ve_dir):
        run('python app.py db upgrade head')
