##Modules import currently broken, using workaround
import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

import rethinkdb as r
import os

RDB_HOST = os.environ.get('RDB_HOST') or 'localhost'
RDB_PORT = os.environ.get('RDB_PORT') or 28015

def dbSetup():
    connection = r.connect(host=RDB_HOST, port=RDB_PORT)
    try:
        r.db_create('EEG').run(connection)
        r.db('EEG').table_create('raw').run(connection)
        r.db('EEG').table_create('acc').run(connection)
        r.db('EEG').table_create('alphaAbs').run(connection)
        r.db('EEG').table_create('betaAbs').run(connection)
        r.db('EEG').table_create('deltaAbs').run(connection)
        r.db('EEG').table_create('gammaAbs').run(connection)
        r.db('EEG').table_create('thetaAbs').run(connection)
        print ('Database setup completed. Now run the app without --setup.')
    except RqlRuntimeError:
        print ('App database already exists. Run the app without --setup.')
    finally:
        connection.close()

dbSetup();
