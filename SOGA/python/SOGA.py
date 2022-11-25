import sys
import getopt

from producecfg import *
from libSOGA import *

from time import time

def SOGA():
 
    print('/ ___| / _ \ / ___|  / \\\n\___ \| | | | |  _  / _ \\\n ___) | |_| | |_| |/ ___ \\\n|____/ \___/ \____/_/   \_\\\n')
    argv = sys.argv[1:]
    Kmax = None
    pruning = None
    cov = False
    var_list = []
    var_idx = []
    
    try:
        opts, args = getopt.getopt(argv, "f:p:c:v:")
    except:
        print("Error")
  
    if opts != []:
        for opt, arg in opts:
            if opt in ['-f']:
                filename = arg
            if opt in ['-p']:
                Kmax = int(arg)
                pruning = 'classic'
            if opt in ['-c']:
                cov = True
            if opt in ['-v']:
                var_list.append(arg)
                
        
      
        start = time()
        cfg = produce_cfg(filename)
        end = time()
        print('CFG produced in: ', np.round(end-start,4), 's')
    
        start = time()
        if not pruning is None:
            print('Pruning to Kmax={} components'.format(Kmax))
        output_dist = start_SOGA(cfg, pruning, Kmax)
        end = time()
        print('Computation completed in ', np.round(end-start,4), 's')
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
                print('Covariance:')
                for i, var in enumerate(output_dist.var_list):
                    row_string = ['{:.3f}'.format(output_dist.gm.cov()[i][j]).center(7) for j in range(output_dist.gm.n_dim())]
                    print(f'{var:>12}', *row_string)
            else:
                print('Covariance:')
                for i in var_idx:
                    row_string = ['{:.3f}'.format(output_dist.gm.cov()[i][j]).center(7) for j in var_idx]
                    print(f'{output_dist.var_list[i]:>12}', *row_string)
            
    else:
        print('Welcome to SOGA!\n')
        print('Please type one of the following command:')
        print('-f : str, specifies filename')
        print('-p : int, specifies Kmax in pruning (default no pruning)')
        print('-c : \'cov\', prints the covariance matrix (default False)')
        print('-v : str, prints the mean of the specified variable (default all variables)')
            
SOGA()    