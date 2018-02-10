#------------------------------------------------------------------------------#
import numpy as np 
def absolute_efficiency(Recorded,Emitted):
    return Recorded/Emitted 

def intrinsic_efficiency(Recorded,):
    
def Souce_activity(Ao,half_life,time):
    """Place Half life and time in same units"""
    return exp(-np.log(2)*time/half_life)
    
def Emitted(Activity,time):
    """Put Activity in Bq and time in seconds"""
    Emitted=Activity*time 

def 