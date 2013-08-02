import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/vagrant/.virtualenvs/navulsa/lib/python2.6/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/vagrant/django_projects/curso/navulsa')
sys.path.append('/home/vagrant/django_projects/curso/navulsa/navulsa')

os.environ['DJANGO_SETTINGS_MODULE'] = 'navulsa.settings'

# Activate your virtual env
activate_env=os.path.abspath("/home/vagrant/.virtualenvs/navulsa/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()