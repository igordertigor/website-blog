import re
import os
import glob
import subprocess

from doit import create_after

SOURCES = glob.glob('content/*') + glob.glob('content/*/*')


DOIT_CONFIG = {
    'verbosity': 2,
}


def task_build():
    return {
        'targets': ['output'],
        'actions': [
            ['pelican'],
        ]
    }


def get_ftp_user():
    lpass = subprocess.check_output(
        'lpass show 3566222442604292113',
        shell=True).decode()
    m = re.search(r'User:\s(.*)$', lpass, re.MULTILINE)
    return m.group(1)


def write_upload_ftp():
    with open('upload.sftp', 'w') as f:
        f.write('cd webseiten\n')
        f.write('cd main\n')
        for fname in glob.glob('output/*'):
            if os.path.isdir(fname):
                f.write('put -r {}\n'.format(fname))
            else:
                f.write('put {}\n'.format(fname))
        f.write('exit\n')


def list_output_dir():
    return [fname for fname in
            (glob.glob('output/*')
             + glob.glob('output/*/*')
             + glob.glob('output/*/*/*'))
            if not os.path.isdir(fname)]


@create_after('build')
def task_upload():
    files = list_output_dir()
    print(files)
    write_upload_ftp()
    return {
        'file_dep': files,
        'actions': [
            'sftp -b upload.sftp {}@ftp.ingofruend.net'
            .format(get_ftp_user())
        ],
    }
