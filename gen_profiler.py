from optparse import OptionParser
import numpy as np
import sys
import os
import subprocess
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="make profile for relative filepath", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

if getattr(options,'filename') is None:
	raise ValueError('No str filename given')
    
with open(options.filename,'r') as f:
	code = f.readlines()
f_target_lst = []
for line in code:
	if '__future__' in line:
		code.remove(line)
		f_target_lst.append(line)

f_target_lst.append('@profile\n')
f_target_lst.append('def main():\n')

for line in code:
	f_target_lst.append('    ' + line)
f_target_lst.append('\n')
f_target_lst.append('main()\n')

with open('target.py','w') as f_tar:
	f_tar.write(''.join(f_target_lst))

if options.verbose:
	print('Starting line profile.')

if sys.version_info[0] == 2:
	subprocess.call(["kernprof","-l","-v","target.py"])
if sys.version_info[0] == 3:
	subprocess.run(["kernprof","-l","-v","target.py"])