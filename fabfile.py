import os
import pwd

from fabric.api import cd, env, task, require, run, sudo, prefix, shell_env
from fabric.contrib.files import exists, upload_template

VIRTUALENV_DIR = 'env'
CODE_DIR = 'mma-dexter'
PROD_HOSTS = ['wazimap.co.za']

@task
def prod():
    env.deploy_type = 'prod'
    env.deploy_dir = '/home/mma/mma-dexter/'
    env.branch = 'master'
    env.hosts = PROD_HOSTS
    env.user = 'mma'


@task
def deploy():
    require('deploy_type', 'deploy_dir', 'branch', provided_by=[prod])

    repo_dir = os.path.join(env.deploy_dir, CODE_DIR)
    ve_dir = os.path.join(env.deploy_dir, VIRTUALENV_DIR)

    if not exists(repo_dir):
        with cd(env.deploy_dir):
            run('git clone https://github.com/Code4SA/mma-dexter.git')

    if not exists(ve_dir):
        run('virtualenv -p python2.7 --no-site-packages %s' % ve_dir)

    with cd(repo_dir):
        run('git checkout -B %s' % env.branch)
        run('git pull origin %s' % env.branch)

    with cd(repo_dir), prefix('. %s/bin/activate' % ve_dir):
        run('pip install -r requirements.txt')

    # make sure logging dir exists and update processes
    log_dir = os.path.join(env.deploy_dir, 'log')
    run('mkdir -p %s' % log_dir)

    # log rotation
    sudo('ln -fs %s/resources/logrotate/dexter /etc/logrotate.d/' % env.deploy_dir)

    # link in nginx config
    sudo('ln -fs %s/resources/nginx/dexter.conf /etc/nginx/sites-enabled/' % env.deploy_dir)
    sudo('service nginx reload')

    # link in upstart config
    sudo('ln -fs %s/resources/upstart/dexter.conf /etc/init/' % env.deploy_dir)
    sudo('initctl reload-configuration')

    # restart dexter
    sudo('service dexter restart')
