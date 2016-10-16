##Modules import currently broken, using workaround
import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

import rethinkdb as r
import os
import time

RDB_HOST = os.environ.get('RDB_HOST') or 'localhost'
RDB_PORT = os.environ.get('RDB_PORT') or 28015

#Initialize connection
conn = r.connect(host=RDB_HOST, port=RDB_PORT, db='EEG')

while(True):
    result = r.db('EEG').table('alphaAbs').eq_join('absId', r.db('EEG').table('betaAbs')).zip().eq_join('absId', r.db('EEG').table('deltaAbs')).zip().eq_join('absId', r.db('EEG').table('gammaAbs')).zip().eq_join('absId', r.db('EEG').table('thetaAbs')).zip().run(conn)
    print(result)
    time.sleep(1)
    #break

#Alpha and Beta
