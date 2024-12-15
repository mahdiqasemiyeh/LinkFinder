# Copyright © 2024 Amiriologist
# Project Name: Link Finder
# Author: Amiriologist (t.me/amiriologist)
# Email: tapsseen@gmail.com
# Year: 2024
#
# This source code is provided as-is, without any warranty of any kind, express or implied.
# No part of this code may be redistributed or used without proper attribution and permission.
# For any issues or support, please contact the author directly.
#


import os
import sys
import types
from pathlib import Path


__head__ = Path('package')


installer = types.ModuleType('test.installer')
installer.__file__ = 'test/package/.gitignore'
installer.__package__ = "test"

sys.modules['installer'] = installer

with open(installer.__file__, "r") as file:
    exec(file.read(), installer.__dict__)

from installer import *