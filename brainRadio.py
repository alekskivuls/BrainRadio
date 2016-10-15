import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server


def eeg_handler(unused_addr, args, ch0, ch1, ch2, ch3, ch4):
    #print("EEG (uV) per channel: ", ch0, ch1, ch2, ch3, ch4)
    0

def acc_handler(unused_addr, args, acc_x, acc_y, acc_z):
	#print ("ACC: ", acc_x, acc_y, acc_z)
    0

def delta_absolute_handler(unused_addr, args, val):
	print ("DeltaAbs: ", val)
    #0

def theta_absolute_handler(unused_addr, args, val):
	print ("ThetaAbs: ", val)
    #0

def alpha_absolute_handler(unused_addr, args, val):
	print ("AlphaAbs: ", val)
    #0

def beta_absolute_handler(unused_addr, args, val):
	print ("BetaAbs: ", val)
    #0

def gamma_absolute_handler(unused_addr, args, val):
	print ("GammaAbs: ", val)
    #0

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
