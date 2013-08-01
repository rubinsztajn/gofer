from fabric.api import *
from fabric.colors import green, red, magenta

""" Prepare for deployment """
def test():
    local("python manage.py test metadata")
    
def commit():
    local("git add . && git commit")

def push():
    local("git push private master")

def prepare():
    test()
    commit()
    push()

""" Deploy """
def server():
    env.host_string = '54.214.253.135'
    env.user = 'ubuntu'
    env.key_filename = '/Users/arubinst/.ec2/arubinst.pem'

def deploy():
    path = '/home/ubuntu/gofer'
    
    print(magenta("Beggining deployment"))
    with cd(path):
        print(green("Pulling from master..."))
        run("git pull")
        print(green("Collecting static files..."))
        run("source venv/bin/activate && python manage.py collectstatic --noinput")
        print(green("Migrating the database..."))
        run("source venv/bin/activate && python manage.py migrate metadata")
        print(green("Restarting webserver..."))
        run("sudo /etc/init.d/apache2 restart")
    print(red("DONE!"))
