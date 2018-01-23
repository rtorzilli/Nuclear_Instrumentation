# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 00:11:56 2017
@author: nickq
"""
import os
import numpy as np 
import MCA_1024 as MCA
import matplotlib.pyplot as plt

# Where to look for the file? 
currentDir = os.path.abspath(os.path.dirname(__file__))
path1 = os.path.join(currentDir, "Scintillator\GammaRay\NaI_3by3")
path2 = os.path.join(path1,"Cesium_137_Calibration.Spe")

# Get Data 
DataFrame=MCA.MCA_1024(path2)


plt.figure(1)
plt.plot(DataFrame["Energy [keV]"],DataFrame["Counts"])
plt.rcParams.update({'font.size': 12})
plt.xlabel('Energy [keV]')
plt.ylabel('Counts')
plt.xlim(0,max(DataFrame["Energy [keV]"]))
plt.grid()
plt.savefig(path1+'/Cs_137_Calibration', bbox_inches='tight')

