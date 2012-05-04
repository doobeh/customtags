activate_this = '/home/graceway/production/customTags/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
os.chdir(abspath)
from app import app as application