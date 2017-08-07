import os
import sys

if sys.platform == 'win32':
    pybabel = 'fenv\\Scripts\\pybabel'
else:
    pybabel = 'fenv/bin/pybabel'

os.system(pybabel + ' compile -d app/translations')

