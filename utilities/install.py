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
from pathlib import Path
from .compiler import All,compile
__package__ = "package"
__abs__ = Path(os.path.abspath(__file__))

# compile
cpl = compile((__abs__.parent.parent / __package__).exists())

#start all packages compile
if cpl:
    os.execv(sys.executable, [sys.executable] + sys.argv)
All(sys.argv,'r').start()