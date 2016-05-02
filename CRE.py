# -*- coding: utf-8 -*-
"""
Created on Mon May 02 11:05:43 2016

@author: ROHAN
"""

import math 
from numpy import *
from matplotlib.pyplot import *
from scipy import stats

# Variables
#Given
t = [0, 20, 40 ,60, 120 ,180, 300];        # time
C_A = [10 ,8, 6, 5, 3, 2, 1];              # concentration
CAo = 10.;
k = zeros(7)
CA_inv = zeros(7)

# Calculations
#Guesmath.sing 1st order kinetics
for i in range(7):
    k[i] = math.log(CAo/C_A[i]);
    CA_inv[i] = 1/C_A[i];

T = array([18.5,23,35]);
CAo = array([10,5,2]);
CA = zeros(3)
log_Tf = zeros(3)
log_CAo = zeros(3)

for i in range(3):
    CA[i] = 0.8*CAo[i];
    log_Tf[i] = math.log10(T[i]);
    log_CAo[i] = math.log10(CAo[i]);

# Results
plot(log_CAo,log_Tf)
plot(log_CAo,log_Tf,"go")
xlabel("Ln CAO")
ylabel("log r")
#plot(log_Tf,log_CAo)
#coeff1 = linalg.lstsq(log_CAo,log_Tf);
slope, intercept, r_value, p_value, std_err = stats.linregress(log_CAo,log_Tf)
coeff1 = stats.linregress(log_CAo,log_Tf)
n = 1-coeff1[0];
print "From graph we get slope and intercept for calculating rate eqn"
k1 = ((0.8**(1-n))-1)*(10.**(1-n))/(18.5*(n-1));
print " The rate equation is given by %.3f"%(k1),
print "CA**1.4 mol/litre.sec"