import os
import sys
import math
import time
import numpy as np
import h5py

from liblibra_core import *
import util.libutil as comn
from libra_py import units as units
from libra_py import data_conv, data_stat, data_outs, data_read, data_savers

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt

import recipes


def plots(prefix, imdl, X, Y):
    """
    This function produces nice plots of the ground state populations for all calculations
    """

    plt.rc('axes', titlesize=12)      # fontsize of the axes title
    plt.rc('axes', labelsize=12)      # fontsize of the x and y labels
    plt.rc('legend', fontsize=10)     # legend fontsize
    plt.rc('xtick', labelsize=8)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=8)    # fontsize of the tick labels
    plt.rc('figure.subplot', left=0.2)
    plt.rc('figure.subplot', right=0.95)
    plt.rc('figure.subplot', bottom=0.13)
    plt.rc('figure.subplot', top=0.88)
   

    figure = plt.figure(num=imdl, figsize=(3.21, 2.41), dpi=300, edgecolor='black', frameon=True)    

    
    plt.plot(X[imdl, :], Y[imdl, :, 0, 0], color="black", label="reflection on state 0", linewidth=1)
    plt.plot(X[imdl, :], Y[imdl, :, 0, 1], color="blue", label="transmission on state 0", linewidth=1)
    plt.plot(X[imdl, :], Y[imdl, :, 1, 0], color="red", label="reflection on state 1", linewidth=1)
    plt.plot(X[imdl, :], Y[imdl, :, 1, 1], color="green", label="transmission on state 1", linewidth=1)


    
    plt.title("",fontsize=9.5)
    plt.legend(fontsize=6.75, ncol=1, loc='upper left')
    plt.xlabel('Momentum, a.u.',fontsize=10)
    plt.ylabel('Population ',fontsize=10)
    plt.tight_layout()
    plt.savefig(F"{prefix}.png", dpi=300)
    plt.show()                                                                                                            




def get_stats(prefix, mdls, P0, batches, ntraj, methods):

    nmdls = len(mdls)
    npts = len(P0)
    nstates = 2
    nscatt = 2 # scattering channels
  
    X = np.zeros((nmdls, npts), dtype=float)
    Y = np.zeros((nmdls, npts, nstates, nscatt), dtype=float)
    
    cols = list(range(ntraj))

    for method in methods:

        recipe = recipes.recipe_inv_mapping(method)
        rec_name, rec_params = recipes.set_recipe(recipe)
            
        for imdl, mdl in enumerate(mdls): 
        
            for ip0, p0 in enumerate(P0):
        
                X[imdl, ip0] = p0
        
                cnt = 0.0
                for batch in batches:
                    #filename = F"{prefix}{mdl}_{int(p0)}/start_s0_BC_FSSH_batch{batch}"
                    filename = F"{prefix}{mdl}_P0_{p0}_RECIPE_{method}/start_s0_{rec_name}_batch{batch}"
                    states = data_read.get_data_from_file2(F"{filename}/states.txt", cols)
                    coords = data_read.get_data_from_file2(F"{filename}/q.txt", cols)                 
        
                    for itraj in range(ntraj):                
        
                        ist = int(states[itraj][-1])
                        q = coords[itraj][-1]
        
                       
                        if q<-5: # reflection on state ist
                            Y[imdl, ip0, ist, 0 ] += 1 
                            cnt += 1 
        
                        elif q>5: # transmission on state ist
                            Y[imdl, ip0, ist, 1 ] += 1 
                            cnt += 1
        
                print(Y, cnt)
                if cnt > 0:
                    Y[imdl, ip0, :, :] = Y[imdl, ip0, :, :] / cnt
        
                    
            #plots(F"model_{mdl}", imdl, X, Y)
        
            with h5py.File(F"model_{mdl}_method_{method}.hdf", "w") as f:
                #g = f.create_group("data")
                f.create_dataset("X", data = X)
                f.create_dataset("Y", data = Y)


def plot(mdls, methods):

    for method in methods:

        for imdl, mdl in enumerate(mdls):
            with h5py.File(F"model_{mdl}_method_{method}.hdf", "r") as f: 
                print( list(f.keys() ) )
                print(f["X"].shape)
                print(f["Y"].shape)
            
                plots(F"model_{mdl}_method_{method}", imdl, f["X"], f["Y"])
            

def compute_accum_error(model_hdf_filename, exact_hdf_filename, istate=0):
    """
    This function computes the accumulate error between the population of the 
    TSH/Ehrenfest and exact dynamics.
    Args:
        model_hdf_filename (string): The mem_data.hdf file name for (path).
        model_hdf_filename (string): The data.hdf file name (path).
        istate (integer): The initial state in the inital condition.
    Returns:
        acc_error (numpy arary): The average acumulation error.
    """
    # Open and read the model hdf file. This file name is mem_data.hdf but needs
    # the full path to this file.
    F = h5py.File(model_hdf_filename, 'r')
    x1 = np.array(F['sh_pop_adi/data'])
    # Open and read the exact calculations hdf file. This file name is data.hdf but needs
    # the full path to this file.
    F = h5py.File(exact_hdf_filename, 'r')
    x2 = np.array(F['pop_adi/data'])
    # Compute the difference between the population of the 
    # exact and model populations
    x1 = x1[:,istate]
    x2 = x2[:,istate,0].reshape(x1.shape[0])
    diff = x1-x2
    # Compute the square of the diff
    tmp = np.power(np.abs(diff),2)
    # Compute the accumulation sum for the tmp array
    acc_error = np.cumsum(tmp,axis=0)
    # Normalize it with 1/T
    for t in range(acc_error.shape[0]):
        acc_error[t] /= (t+1)

    return x1, x2, acc_error 
    
#p0 = [2.0, 5.0, 7.0, 10.0, 15.0, 18.0, 20.0, 23.0, 25.0, 30.0, 35.0, 40.0]
#ntraj = 100

#get_stats("MDL_", [2,3], p0, [0, 1], ntraj, [90, 94])
#plot([2,3], [90, 94])
    
    
