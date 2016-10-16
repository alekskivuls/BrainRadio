package com.alekskivuls.BrainRadio;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.concurrent.LinkedBlockingDeque;

import oscP5.OscMessage;
import oscP5.OscP5;

public class MuseOscServer {

	static MuseOscServer museOscServer;
	static LinkedBlockingDeque<MuseMessageAbs> museMsgQueueAbs;

	OscP5 museServer;
	static int recvPort = 5003;

	public static void main(String[] args) throws InterruptedException {
		museMsgQueueAbs = new LinkedBlockingDeque<MuseMessageAbs>();
		museOscServer = new MuseOscServer();
		museOscServer.museServer = new OscP5(museOscServer, recvPort);

		ArrayList<MuseMessageAbs> msgList = new ArrayList<MuseMessageAbs>();
		int msgListEnd = 0;
		
		GUI frame = new GUI("EEG Status");
	    frame.setVisible( true );
		
		while (true) {
			while(museMsgQueueAbs.size() > 0)
				msgList.add(museMsgQueueAbs.pop());
			for(int i = msgListEnd; i < msgList.size(); i++) {
				msgList.get(i).computeRelative();
			}
			msgListEnd = msgList.size();
			System.out.println(msgList.size());
			double[][] result = calcStats(msgList, 1000);
			for(double[] arr : result)
				System.out.println(Arrays.toString(arr));
			Thread.sleep(1000);
		}
	}

	static double[][] calcStats(ArrayList<MuseMessageAbs> msg, int numAveraging) {
		double[][] result = new double[3][5];
		if(msg.size()==0)
			return result;
		int start = msg.size() - numAveraging;
		if (start < 0)
			start = 0;
		//Mean
		for(int i = start; i < msg.size(); i++) {
			result[0][0] += msg.get(i).alphaRel;
			result[0][1] += msg.get(i).betaRel;
			result[0][2] += msg.get(i).deltaRel;
			result[0][3] += msg.get(i).gammaRel;
			result[0][4] += msg.get(i).thetaRel;
		}
		for(int i = 0 ; i < result.length; i++) {
			result[0][i] /= (msg.size()-start);
		}
		//Variance
		for(int i = start; i < msg.size(); i++) {
			result[1][0] += Math.pow(msg.get(i).alphaRel - result[0][0], 2);
			result[1][1] += Math.pow(msg.get(i).betaRel - result[0][1], 2);
			result[1][2] += Math.pow(msg.get(i).deltaRel - result[0][2], 2);
			result[1][3] += Math.pow(msg.get(i).gammaRel - result[0][3], 2);
			result[1][4] += Math.pow(msg.get(i).thetaRel - result[0][4], 2);
		}
		for(int i = 0 ; i < result.length; i++) {
			result[1][i] /= msg.size()-start;
		}
		//Z index
		for(int i = 0 ; i < result.length; i++) {
			result[2][i] = (msg.get(msg.size()-1).alphaRel - result[0][i]) / Math.sqrt(result[1][i]);
			result[2][i] = (msg.get(msg.size()-1).betaRel - result[0][i]) / Math.sqrt(result[1][i]);
			result[2][i] = (msg.get(msg.size()-1).deltaRel - result[0][i]) / Math.sqrt(result[1][i]);
			result[2][i] = (msg.get(msg.size()-1).gammaRel - result[0][i]) / Math.sqrt(result[1][i]);
			result[2][i] = (msg.get(msg.size()-1).thetaRel - result[0][i]) / Math.sqrt(result[1][i]);
		}
		
		
		return result;
	}
	
	void oscEvent(OscMessage msg) {
		// System.out.println("### got a message " + msg);
		if (msg.checkAddrPattern("/muse/eeg") == true) {
			for (int i = 0; i <= 4; i++) {
				// System.out.print("EEG on channel " + i + ": " +
				// msg.get(i).floatValue() + "\n");
			}
		} else if (msg.checkAddrPattern("/muse/elements/alpha_absolute") == true) {
			// MuseMessageAbs test = new MuseMessageAbs();
			// museMsgAbs.add(test);
			museMsgQueueAbs.add(new MuseMessageAbs());
			museMsgQueueAbs.getLast().alphaAbs = msg.get(0).floatValue();
		} else if (msg.checkAddrPattern("/muse/elements/beta_absolute") == true) {
			museMsgQueueAbs.getLast().betaAbs = msg.get(0).floatValue();
		} else if (msg.checkAddrPattern("/muse/elements/delta_absolute") == true) {
			museMsgQueueAbs.getLast().deltaAbs = msg.get(0).floatValue();
		} else if (msg.checkAddrPattern("/muse/elements/gamma_absolute") == true) {
			museMsgQueueAbs.getLast().gammaAbs = msg.get(0).floatValue();
		} else if (msg.checkAddrPattern("/muse/elements/theta_absolute") == true) {
			museMsgQueueAbs.getLast().thetaAbs = msg.get(0).floatValue();
		}
	}
}