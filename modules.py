# A module is a file containing a set of functions to include in an application.
# There are core python modules, modules you install with pip package manager (incl Django), and custom modules.

# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip module
from camelcase import CamelCase

c = CamelCase()
print(c.hump('hello there world'))

# today = datetime.date.today()
today = date.today()
timestamp = time()
print(today)
print(timestamp)
