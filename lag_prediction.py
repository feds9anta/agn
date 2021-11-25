import numpy as np
'''
Code to evaluate the expected lag spectrum for an AGN, given its physical parameters.
Based on equation 8 of Kammoun+2021 ApH 907, Issue 1, id.20 
( https://ui.adsabs.harvard.edu/abs/2021ApJ...907...20K/abstract )
 
Parameters defined in the code are for Mrk 110

F. Vincentelli 2021
'''
 


# define parameters
h=5#h is the height of the lamp-post in units of 10 Rg
mdot =8#is the accretion rate in units of 5% of the Eddington limit, 
LX=0.027#is the observed, 2−10 keV luminosity in units of the Eddington luminosity,
M= 2#M7 is the BH mass in units of 107M
lambda_ref=1928 # UVW2 REFERENCE BAND  (Angstrom)
lambda0=1950 # NORMALIZATION, fixed  (Angstrom)
spin =1

lag_choice=0 #0 if a single wavelength, 1 if all lag spectrum

lamb_single=0.25 #lambda in Angstrom for which the single lag is computed

wave_inf =0 #lower limit of lag spectrum (Angstrom)
wave_up=10000 #upper limit of lag spectrum  (Angstrom)
wave=np.linspace(wave_inf,wave_up,wave_up*4)

if spin==0:
	A =  0.27 + 0.031*h - 0.0007*h**2 
	B = 1.395 - 0.043*h + 0.0017*h**2
	f1 = 0.636 + 0.4*mdot - 0.059*mdot**2+ 0.0033*mdot**3
	f2 = LX**(-0.763) * (0.5 *(1 + LX**(0.12)))**14.03




if spin==1:
	A = 0.164 + 0.039*h -  0.0012*h**2
	B = 1.346 - 0.037*h + 0.0013*h**2
	f1 = 0.823 + 0.193*mdot - 0.023*mdot**2+ 0.0012*mdot**3
	f2 = LX**(0.025) * (0.5 *(1 + LX**(0.79)))**0.38

	#choice=input("Spin 0 or 1 ?")

if lag_choice==0:
	print(A* (M**0.7 )* f1 *f2 * ((lamb/lambda0) **B - (lambda_ref/lambda0)**B ))
if lag_choice==1:
	for i in range(0,len(wave)) :
		lamb=wave[i]
		print(lamb, A* (M**0.7 )* f1 *f2 * ((lamb/lambda0) **B - (lambda_ref/lambda0)**B ))
 
