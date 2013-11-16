# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, "/var/www/bitcard/") # Make this more flexible

from run import app
from shared.env import Log

application = app.wsgifunc(Log)
