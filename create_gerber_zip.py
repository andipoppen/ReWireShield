#!/usr/bin/env python2.7

import os
import zipfile

projname = os.getcwd().split(os.sep)[-1]

zf = zipfile.ZipFile("%s.zip" % (projname), "w", zipfile.ZIP_DEFLATED)
zf.write(projname + '.GTL')
zf.write(projname + '.GBL')
zf.write(projname + '.GTS')
zf.write(projname + '.GBS')
zf.write(projname + '.GTO')
zf.write(projname + '.GBO')
zf.write(projname + '.TXT')
zf.write(projname + '.GML')

try:
  zf.write(projname + '.GL2')
  zf.write(projname + '.GL3')
except OSError:
  print "INFO: No Layer 2 or 3 included"

zf.close()

print "Done!"

