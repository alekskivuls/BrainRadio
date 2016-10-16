package com.alekskivuls.BrainRadio;

public class MuseMessageAbs {
	double alphaAbs, betaAbs, deltaAbs, gammaAbs, thetaAbs;
	double alphaRel, betaRel, deltaRel, gammaRel, thetaRel;

	public MuseMessageAbs() {
	}

	public void computeRelative() {
		double denominator = Math.pow(10, alphaAbs) + Math.pow(10, betaAbs) + Math.pow(10, deltaAbs)
				+ Math.pow(10, gammaAbs) + Math.pow(10, thetaAbs);
		alphaRel = Math.pow(10, alphaAbs) / denominator;
		betaRel = Math.pow(10, betaAbs) / denominator;
		deltaRel = Math.pow(10, deltaAbs) / denominator;
		gammaRel = Math.pow(10, gammaAbs) / denominator;
		thetaRel = Math.pow(10, thetaAbs) / denominator;
	}

}
