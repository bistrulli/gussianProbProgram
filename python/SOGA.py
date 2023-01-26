# TODO:
# - add instruction for printing on .csv

import sys
import getopt

from producecfg import *
from libSOGA import *

from time import time

def SOGA():
 
    print('/ ___| / _ \ / ___|  / \\\n\___ \| | | | |  _  / _ \\\n ___) | |_| | |_| |/ ___ \\\n|____/ \___/ \____/_/   \_\\\n')
    argv = sys.argv[1:]
    cov = False
    out_file = None
    var_list = []
    var_idx = []
    out_name = None
    
    try:
        opts, args = getopt.getopt(argv, "f:o:cv:")
    except:
        print("Error")
  
    if opts != []:
        for opt, arg in opts:
            if opt in ['-f']:
                filename = arg
            if opt in ['-o']:
                out_name = arg
            if opt in ['-c']:
                cov = True
            if opt in ['-v']:
                var_list.append(arg)
                
        
      
        cfg_start = time()
        cfg = produce_cfg(filename)
        cfg_end = time()
        print('CFG produced in: ', cfg_end-cfg_start)
    
        comp_start = time()
        output_dist = start_SOGA(cfg)
        comp_end = time()
        print('Computation completed in ', comp_end-comp_start)
        print('\n')
    
        if var_list == []:
            for var, val in zip(output_dist.var_list, output_dist.gm.mean()):
                print('E['+var+']:', round(val,5))
        else:
            for var in var_list:
                i = output_dist.var_list.index(var)
                print('E['+var+']:', round(output_dist.gm.mean()[i],5))
                var_idx.append(i)
        print('\n')
    
        if cov is True:
            if var_list == []:
                print('Covariance:\n', np.around(output_dist.gm.cov(),5))
            else:
                print('Covariance:\n', np.around(output_dist.gm.cov()[var_idx][:,var_idx], 5))
            
        if not out_name is None:
            with open(out_name, 'w') as f:
                sys.stdout = f # Change the standard output to the file we created.
                print('CFG produced in: ', cfg_end-cfg_start)
                print('Computation completed in ', comp_end-comp_start)
                print('\n')
                if var_list == []:
                    for var, val in zip(output_dist.var_list, output_dist.gm.mean()):
                        print('E['+var+']:', round(val,5))
                else:
                    for var in var_list:
                        i = output_dist.var_list.index(var)
                        print('E['+var+']:', round(output_dist.gm.mean()[i],5))
                        var_idx.append(i)
                print('\n')
                if cov is True:
                    if var_list == []:
                        print('Covariance:\n', np.around(output_dist.gm.cov(),5))
                    else:
                        print('Covariance:\n', np.around(output_dist.gm.cov()[var_idx][:,var_idx], 5))
    
    else:
        print('Welcome to SOGA!\n')
        print('Please type one of the following command:')
        print('-f : str, specifies filename')
        print('-c : prints the covariance matrix (default False)')
        print('-v : str, prints the mean of the specified variable (default all variables)')
        print('-o : str, specifies .txt file to print on')
            
SOGA()    