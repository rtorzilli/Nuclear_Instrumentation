# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:28:30 2018

@author: Robert
"""
# place this code in same directory as excel book
import pandas as pd # for excel
import os # for generalization call
import numpy as np #for math

# Windows path for calls
currentDir = os.path.abspath(os.path.dirname(__file__))

dataLoc = currentDir+"\\300N.xlsx"

# Get data from excel
FourB_data = pd.read_excel(dataLoc, sheetname='4B')
FourC_data = pd.read_excel(dataLoc, sheetname='4C')
FourD_data = pd.read_excel(dataLoc, sheetname='4D')
BG_data = pd.read_excel(dataLoc, sheetname='4D_BackGround')

# Functions for statsitcal analysis

#Sample Variance s^2 = VarSam
def DF_VarSam (givenDF,meanExp):
    N=len(givenDF)
    VarSam_Top = 0
    for i in range(N):
        VarSam_Top += (givenDF['Counts'][i] -meanExp)**2
    VarSam=VarSam_Top/N    
    return VarSam

# Sample Variance using List
def VarSam (givenList,meanExp):
    N=len(givenList)
    VarSam_Top = 0
    for i in range(N):
        VarSam_Top += (givenList[i] -meanExp)**2
    VarSam=VarSam_Top/N    
    return VarSam


# Refine data with 3sigma test
# Compare only keep if within bounds
def refineData (givenDF,meanExp):
    N=len(givenDF)
    # Define bounds
    lowBound=meanExp-3*np.sqrt(meanExp)
    upBound = meanExp+3*np.sqrt(meanExp)
    print('Bounds: '+str(lowBound)+' to '+str(upBound))
    refinedData = []
    for i in range(N):
        if givenDF['Counts'][i]<upBound and givenDF['Counts'][i] > lowBound:
            refinedData.append(givenDF['Counts'][i])
    return refinedData

# Determine amount of counts (measurements) that deviate by the a given sigma test
# Used the refined data since that is what was used by the chi2 test
# sigTest is the multiplaction factor (.67,1,2,ect)
def deviationSig(givenList,expMean,sigTest):
    N=len(givenList)
    # Define bounds
    lowBound=expMean-sigTest*np.sqrt(expMean)
    upBound = expMean+sigTest*np.sqrt(expMean)
    print('Bounds: '+str(lowBound)+' to '+str(upBound))
    refinedData = []
    countsDeviated=0
    for i in range(N):
        if givenList[i]<upBound and givenList[i] > lowBound:
            refinedData.append(givenList[i])
        else:
            countsDeviated+=1
    return refinedData, countsDeviated

# Experimental Mean X
def expMeanPandas (givenDF):
    N=len(givenDF)
    return (givenDF['Counts'].sum())/N

# Chisqaure using refined data, sample vairance, and experimental mean
def chiSquare(givenList,expMean):
    #Need Sample Var
    sS=VarSam(givenList,expMean)
    #Need N'
    N=len(givenList)    
    return ((N-1)*sS)/expMean

# Analysis for data from Procedure 4 B
# Calculate mean, Gaussian Standard Deviation, sample variance
X4B = expMeanPandas(FourB_data)
sigma4B = np.sqrt(X4B)
varSam4B = DF_VarSam(FourB_data,X4B)
print('Experimental Mean: '+str(X4B))    
print('Sample Variance: '+str(varSam4B))
# Standard Deviation for Gauss should be about the same as the the sqrt of Sample Variance
print('Standard Deviation s ~ ' +str(np.sqrt(varSam4B)) + ' Sigma ~ ' +str(sigma4B))

# Refine the data and through out that which doesnt fit the 3sigma test
refined4B = refineData(FourB_data,X4B)   

# Recalculate if need be
if len(refined4B) != len(FourB_data):
    print("Adjust code to recalculate, I'm lazy")
else:
    print("All data is accpeted")

# Apply Chi squared test
chiB = chiSquare(refined4B,X4B)
print("Chis Square Value: "+ str(chiB))


# Craete the Frequency Distribution Function
    
import matplotlib.pyplot as plt

N = len(refined4B)
# method 1
H,X1 = np.histogram( refined4B, bins = 10, normed = True )
dx = X1[1] - X1[0]
F1 = np.cumsum(H)*dx
#method 2
X2 = np.sort(refined4B)
F2 = np.array(range(N))/float(N)

# Frequency Distr
FrD,BinEdge=np.histogram(refined4B,bins = np.amax(refined4B))

# Poisson Distr
from decimal import Decimal
XaxisP1 = np.arange(np.amin(refined4B),np.amax(refined4B)+1,1)
P1=[]
for i in range(np.amax(refined4B)):
    bot = Decimal(np.math.factorial(i))
    top= ((X4B**i)*(np.exp(-X4B)))
    P1.append(250*top/float(bot))

# Gaussian Distr
P2=[]
for i in range(np.amax(refined4B)):
    bot = np.sqrt(2*X4B*np.pi)
    top = np.exp((-(i-X4B)**2)/(2*X4B))
    P2.append(250*top/bot)
# =============================================================================
# plt.plot(X1[1:], F1)
# =============================================================================
fig, ax = plt.subplots()
ax.plot(XaxisP1, P1, label='Pois')
ax.plot(XaxisP1, P2, label='Gauss')
ax.plot(XaxisP1, FrD, label='Freq Dist')
legend = ax.legend(loc='upper right', shadow=True, fontsize='large')
# =============================================================================
# plt.plot(X2, F2)
# =============================================================================
plt.show()
    
# 4C
# Calculate mean, Gaussian Standard Deviation, sample variance
X4C = expMeanPandas(FourC_data)
sigma4B = np.sqrt(X4C)
varSam4C = DF_VarSam(FourC_data,X4C)
print('Experimental Mean: '+str(X4C))    
print('Sample Variance: '+str(varSam4C))
# Standard Deviation for Gauss should be about the same as the the sqrt of Sample Variance
print('Standard Deviation s ~ ' +str(np.sqrt(varSam4C)) + ' Sigma ~ ' +str(varSam4C))

# Refine the data and through out that which doesnt fit the 3sigma test
refined4C = refineData(FourC_data,X4C)      
# Recalculate if need be
if len(refined4C) != len(FourC_data):
    print("Adjust code to recalculate, I'm lazy")
else:
    print("All data is accpeted")
    
# Apply Chi squared test
chiC = chiSquare(refined4C,X4C)
print("Chis Square Value: "+ str(chiC))
print("Reduced Chis Square Value: "+ str(chiC/(len(refined4C)-1)))

_,sig67=deviationSig(refined4C,X4C,.67)
_,sig1=deviationSig(refined4C,X4C,1.0)
_,sig16=deviationSig(refined4C,X4C,1.6)
_,sig2=deviationSig(refined4C,X4C,2.0)
NC=len(refined4C)

# PDF
from scipy.stats import chi2
print(chi2.pdf(chiC,(len(refined4C)-1)))


# Deviated counts for different sgi tests
print('**** Deviated Counts ****')
print('0.67 Sigma had '+ str(sig67)+' deviated results IE: '+str(100*sig67/NC)+' %')
print('1.0 Sigma had '+ str(sig1)+' deviated results IE: '+str(100*sig1/NC)+' %')
print('1.6 Sigma had '+ str(sig16)+' deviated results IE: '+str(100*sig16/NC)+' %')
print('2.0 Sigma had '+ str(sig2)+' deviated results IE: '+str(100*sig2/NC)+' %')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    