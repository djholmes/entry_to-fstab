#!/usr/bin/env python3

import os
import sys
import time
from fstab import Fstab


def fstab_entry():
    os.system('sudo blkid > data.txt')
    hdds = open('data.txt', "r+", )
    y = ""
    finalstring = ""
    for line in hdds:
        if line.startswith("/dev/sda1"):
            if "PIHDD" and "ntfs" in line:
                j = line.find('UUID')
                i = line.find('"', j)
                b = line.find('"', i + 1)
                y = line[i:b].replace('"', '')
                finalstring = "UUID=" + y + " /opt/PIHDD " + "ntfs" + " defaults,nofail,x-systemd.device-timeout=1,noatime 0 0"

            elif "PIHDD" and "ext4" in line:
                j = line.find('UUID')
                i = line.find('"', j)
                b = line.find('"', i + 1)
                y = line[i:b].replace('"', '')
                finalstring = "UUID=" + y + " /opt/PIHDD " + "ext4" + " defaults,nofail,x-systemd.device-timeout=1,noatime 0 0"

    hdds.close()

    if os.path.exists('/opt/PIHDD'):
        pass
    else:
        os.system('sudo mkdir /opt/PIHDD')

    fstab = Fstab()
    other_file = open('data1.txt', 'r+')
    other_file.truncate()

    fs_file = open('/etc/fstab', 'r+')
    fs_file.seek(0)
    t = fs_file.readlines()

    for line in t:
        if "PIHDD" in line:
            pass
        else:
            other_file.write(line)

    fs_file.seek(0)
    fs_file.truncate()
    fs_file.close()
    other_file.close()

    fs_file1 = open('/etc/fstab', 'r+')
    other_files = open('data1.txt', 'r+')

    for x in other_files.readlines():
        fs_file1.write(x)

    fs_file1.write(finalstring)

    other_files.close()
    fs_file1.close()


fstab_entry()