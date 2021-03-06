from __future__ import with_statement
from fabric.api import *


def staging():
    projectname = 'cireg'
    basepath = '/srv/cireg.brueck.io/%s'
    env.hosts = ['{0}@{0}.brueck.io'.format(projectname)]
    env.path = basepath % projectname
    env.virtualenv_path = basepath % (projectname + 'env')
    env.push_branch = 'staging'
    env.push_remote = 'origin'
    env.reload_cmd = 'supervisorctl restart {0}'.format(projectname)
    env.after_deploy_url = 'http://%s.brueck.io' % projectname


def production():
    projectname = 'cireg'
    basepath = '/webservice/%s'
    env.user = 'django'
    env.hosts = ['django@cireg.pik-potsdam.de']
    env.path = basepath % projectname
    env.virtualenv_path = basepath % (projectname + 'env')
    env.push_branch = 'master'
    env.push_remote = 'origin'
    env.after_deploy_url = 'http://cireg.pik-potsdam.de'
    env.reload_cmd = 'sudo /bin/systemctl restart gunicorn-cireg.pik-potsdam.de.service'


def reload_webserver():
    run("%(reload_cmd)s" % env)


def migrate():
    with cd(env.path):
        run("pipenv run ./manage.py migrate --settings=config.settings.production")


def ping():
    run("echo %(after_deploy_url)s returned:  \>\>\>  $(curl --write-out %%{http_code} --silent --output /dev/null %(after_deploy_url)s)" % env)


def deploy():
    with cd(env.path):
        run("git pull %(push_remote)s %(push_branch)s" % env)
        run("pipenv run ./manage.py collectstatic --noinput --settings=config.settings.production")
    migrate()
    reload_webserver()
    ping()


def pip():
    with cd(env.path):
        run("git pull %(push_remote)s %(push_branch)s" % env)
        run("pip install -Ur requirements/production.txt")

    reload_webserver()


def soft_deploy():
    with cd(env.path):
        run("git pull %(push_remote)s %(push_branch)s" % env)
    reload_webserver()
    ping()
