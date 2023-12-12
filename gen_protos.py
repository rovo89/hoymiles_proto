#!/usr/bin/env python3
import os
import re
import shutil

dir = 'hoymiles_proto/message/proto'

# (Re-)create directory.
try:
  shutil.rmtree(dir)
except FileNotFoundError:
  pass
os.mkdir(dir)

# Execute protoc (preferring executable in current directory).
os.environ['PATH'] = '.:' + os.environ['PATH']
if os.system(f'protoc -I=protobuf --python_out={dir} --pyi_out={dir} protobuf/*.proto') != 0: exit(1)

# Create __init__.py.
modules = []
includes = []
for name in sorted(os.listdir(dir)):
  if match := re.search('(.+_pb2).py$', name):
    if name.startswith('_'):
      includes.append(match.group(1))
    else:
      modules.append(match.group(1))

with open(dir + '/__init__.py', 'w') as init:
  print('import sys', file=init)
  for inc in includes:
    print('from . import ' + inc, file=init)
    print(f"sys.modules['{inc}'] = {inc}", file=init)
  for mod in modules:
    print('from . import ' + mod, file=init)
