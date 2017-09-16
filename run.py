import os
import sys


appdir = os.path.abspath(os.path.dirname(__file__))
os.chdir(appdir)
for d in ((appdir, 'game'), (appdir, 'game', 'data')):
    if d not in sys.path:
        sys.path.insert(0, os.path.join(*d))

import main
main.main()
