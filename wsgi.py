import sys
sys.path.insert(0, '/home/pi/automacao')

from app import app as application
application.root_path = '/home/pi/automacao'
