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
# ----- just for test and doesn't need run ----- #

from . import install as app
from .install import Bin

class All(Bin):
    STAT = "package/STATUS"
    SYSTEM = open
    OPERATOR = '__STR__'
    def __init__(self,command,move=None, query=STAT):
        self.move = move
        self.command = command
        self.query = self.app_rather(query, move)
    def __del__(self):
        self.query.close()
    def run(self):
        app.start(self.req)
    def check(self):
        # check
        return self.query.read()

    
    