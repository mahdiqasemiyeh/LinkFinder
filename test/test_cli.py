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
# ----- just for txest and doesn't need run ----- #

from package.manage import Client
api_id = 12345678910
api_hash = "xxxxxxxxx"

def test_cli():
    app = Client('app',api_id,api_hash,test_mode)
    app.start()