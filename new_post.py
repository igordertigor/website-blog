#!/usr/bin/env python3

import os
import sys
from datetime import datetime

TEMPLATE = """
Title: <++>
Date: {date}
Category: <++>
Tags: <++>
Slug: <++>
Authors: Ingo Fruend
Summary: <++>
status: draft
"""

now = datetime.now()

date = now.date()

name = sys.argv[1]

outfile = os.path.join('content', f'{date}-{name}.md')

if os.path.exists(outfile):
    print('File already exists')

with open(outfile, 'w') as f:
    f.write(TEMPLATE.format(date=now.strftime('%Y-%m-%d %H:%M')))
