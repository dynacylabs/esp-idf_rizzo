#!/bin/python3

import subprocess
import glob
import os

base_dir = os.getcwd()
elfs_dir = os.path.join(base_dir, "esp-idf_elfs")

os.chdir(elfs_dir)

release_list = ['release_v2.0',
                'release_v2.1',
                'release_v3.0',
                'release_v3.1',
                'release_v3.2',
                'release_v3.3',
                'release_v4.0',
                'release_v4.1',
                'release_v4.3',
                'release_v4.4',
                'release_v5.0',
                'release_v5.1']

for release in release_list:
    num_of_elfs = 0
    num_of_riz = 0
    os.chdir(release)
    elfs_glob = glob.glob("*.elf")
    num_of_elfs = len(elfs_glob)
    os.chdir(base_dir)
    if os.path.exists(os.path.join(base_dir, release)):
        os.chdir(release)
        riz_glob = glob.glob("*.riz")
        num_of_riz = len(riz_glob)
        os.chdir(base_dir)
    if num_of_elfs == num_of_riz:
        done_str = "DONE"
    elif num_of_riz == 0:
        done_str = "WAITING"
    else:
        done_str = "GENERATING"
    print(release + " - elfs: " + str(num_of_elfs) + " - riz: " + str(num_of_riz) + " - " + done_str)
    os.chdir(elfs_dir)
