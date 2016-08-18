#!/usr/bin/env python
from gdrivepublic import Path, isgdrive
from subprocess import call


from argparse import ArgumentParser
p = ArgumentParser()
p.add_argument('rdir',help='root directory to search for active drive-google connections',nargs='?',default='~')
p = p.parse_args()

rdir = Path(p.rdir).expanduser()
#%%
for d in rdir.rglob('.gd'):
    try:
        if isgdrive(d):
            call(['drive','deinit'],cwd=str(d))
    except PermissionError:
        pass