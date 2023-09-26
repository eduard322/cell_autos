from array import array
import argparse
# import matplotlib.pyplot as plt
import cell_class






if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                    prog='cell automats',
                    description='visualising cell automats')
    
    parser.add_argument('-n', dest = 'N', default = None, required = False)    # option that takes a value
    parser.add_argument('-v', dest = 'vis', type = int)
    parser.add_argument('-x', dest = 'X', type = list, default = None, required = False)
    parser.add_argument('-N', dest = 'Niter', type = int)
    parser.add_argument('-s', dest = 'func', type = str)
    parser.add_argument('-m', dest = 'vis_mech', type = str)

    args = parser.parse_args()
    # N = [0 for _ in range(40)] + [1] + [0 for _ in range(40)]
    # N += N + N + N
    if args.N is None and args.X:
        X = list(args.X)
    else:
        X = int(args.N)
        
    cell = cell_class.Cell(dimension = 1, 
                           N = X,
                           dtype = "int", 
                           Niter = args.Niter, 
                           func_name = args.func, 
                           vis = args.vis,
                           vis_mech= args.vis_mech)
    cell.start_sim()


