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
import os
import shutil
from pathlib import Path
from .package import api,errors


if os.path.isdir('package') and not os.path.exists('package/STATUS'):
    with open('package/STATUS',"w") as athom:
        athom.write('NONE')

# start install 

class Bin(api.Bin):
    pass
try:
    from package import api,errors
except ModuleNotFoundError:
    pass
def start(request=None):
    if request:
        api.start()
        errors.start()


def cpp(src, dest):
    src = Path(src)
    dest = Path(dest)

    total_items = 0

    # Count total number of files and directories
    for item in src.rglob('*'):
        if item.is_file() or item.is_dir():
            total_items += 1

    current_progress = 0

    # Perform copying
    for item in src.rglob('*'):
        relative_path = item.relative_to(src)
        dest_path = dest / relative_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        if item.is_file():
            shutil.copy2(item, dest_path)
        elif item.is_dir():
            os.mkdir(dest_path)
        current_progress += 1

        # Manually calculate and print progress
        progress = (current_progress / total_items) * 100
        print(f'loading: {progress:.2f}%')