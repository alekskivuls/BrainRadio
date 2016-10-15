import argparse
import math

##Modules import currently broken, using workaround
import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')

import rethinkdb as r
from pythonosc import dispatcher
from pythonosc import osc_server

def eeg_handler(unused_addr, args, ch0, ch1, ch2, ch3, ch4):
    #print("EEG (uV) per channel: ", ch0, ch1, ch2, ch3, ch4)
    time = r.now().to_epoch_time();
    with r.connect('localhost', 28015) as conn:
        r.db('EEG').table('raw').insert([{'time':time,'ch0':ch0,'ch1':ch1,'ch2':ch2,'ch3':ch3,'ch4':ch4}]).run(conn)

def acc_handler(unused_addr, args, acc_x, acc_y, acc_z):
	#print ("ACC: ", acc_x, acc_y, acc_z)
    time = r.now().to_epoch_time();
    with r.connect('localhost', 28015) as conn:
        r.db('EEG').table('acc').insert([{'time':time,'acc_x':acc_x,'acc_y':acc_y,'acc_z':acc_z}]).run(conn)

##Absolute##
def delta_absolute_handler(unused_addr, args, val):
	#print ("ThetaAbs: ", val)
    time = r.now().to_epoch_time();
    with r.connect('localhost', 28015) as conn:
        r.db('EEG').table('deltaAbs').insert([{'time':time, 'val':val}]).run(conn)    

def theta_absolute_handler(unused_addr, args, val):
	#print ("ThetaAbs: ", val)
    time = r.now().to_epoch_time();
    with r.connect('localhost', 28015) as conn:
        r.db('EEG').table('thetaAbs').insert([{'time':time, 'val':val}]).run(conn)    

def alpha_absolute_handler(unused_addr, args, val):
	#print ("AlphaAbs: ", val)
    time = r.now().to_epoch_time();
    with r.connect('localhost', 28015) as conn:
        r.db('EEG').table('alphaAbs').insert([{'time':time, 'val':val}]).run(conn)

def beta_absolute_handler(unused_addr, args, val):
	#print ("BetaAbs: ", val)
    time = r.now().to_epoch_time();
    with r.connect('localhost', 28015) as conn:
        r.db('EEG').table('betaAbs').insert([{'time':time, 'val':val}]).run(conn)

def gamma_absolute_handler(unused_addr, args, val):
	#print ("GammaAbs: ", val)
    time = r.now().to_epoch_time();
    with r.connect('localhost', 28015) as conn:
        r.db('EEG').table('gammaAbs').insert([{'time':time, 'val':val}]).run(conn)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=5001,
                        help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/debug", print)
    #Create reading
    dispatcher.map("/muse/eeg", eeg_handler, "EEG")
    dispatcher.map("/muse/acc", acc_handler, "ACC")
    dispatcher.map("/muse/elements/delta_absolute", delta_absolute_handler, "DeltaAbs")
    dispatcher.map("/muse/elements/theta_absolute", theta_absolute_handler, "ThetaAbs")
    dispatcher.map("/muse/elements/alpha_absolute", alpha_absolute_handler, "AlphaAbs")
    dispatcher.map("/muse/elements/beta_absolute", beta_absolute_handler, "BetaAbs")
    dispatcher.map("/muse/elements/gamma_absolute", gamma_absolute_handler, "GammaAbs")

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
