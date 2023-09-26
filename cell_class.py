import numpy as np
import matplotlib
# matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from copy import deepcopy
from functools import partial


def sum_mod_2(a, b):
    return (a + b) % 2

class Cell:
    def __init__(self, dimension = 1,  N = 1, dtype = "bool", Niter = 1, func_name = None, vis = False, vis_mech = "plt") -> None:
        print("Initializing cells...")
        self.dim = dimension
        self.N = N
        self.type = type(self.N)
        self.dtype = dtype
        self.Niter = Niter
        self.func_name = func_name
        self.vis = vis
        self.vis_mech = vis_mech
        
        if self.type == int:
            if self.dim == 1:
                self.size = self.N
                self.X_0 = np.random.randint(0, 2, size = self.N, dtype = self.dtype)
                self.X = deepcopy(self.X_0)
                self.X_00 = deepcopy(self.X_0)
                self.Z = np.zeros((self.Niter, self.size))
                self.Z[self.Niter - 1] = self.X_0
            else:
                self.X_0 = np.random.randint(0, 2, size = (self.N, self.N), dtype = self.dtype)
                self.X = self.X_0
                
        elif self.type == list:
            if self.dim == 1:
                self.size = len(self.N)
                self.X_0 = np.array(self.N, dtype = self.dtype)
                self.X = deepcopy(self.X_0)
                self.X_00 = deepcopy(self.X_0)
                self.Z = np.zeros((self.Niter, self.size))
                self.Z[self.Niter - 1] = self.X_0
                # z = np.zeros((self.Niter, self.size))
                # z[0] = self.X_0
                # self.Z_0 = 
                # self.Z_0 = 

            else:
                self.X_0 = np.array(self.N, dtype = self.dtype)
                self.X = self.X_0
                
        else:
            print("Enter a number of elements or a list")
            exit()
  
    def jump_func_1(self, i) -> None:
        if i > 0 and i < self.size - 1:
            self.X[i] = self.X_0[i-1] | self.X_0[i] | self.X_0[i+1]
        else:
            self.X[i] = self.X_0[i-1] | self.X_0[i] | self.X_0[i+1 - self.size]
            

    def jump_func_2(self, i) -> None:
        if i > 0 and i < self.size - 1:
            self.X[i] = self.X_0[i-1] | sum_mod_2(self.X_0[i],self.X_0[i+1])
        else:
            self.X[i] = self.X_0[i-1] | sum_mod_2(self.X_0[i],self.X_0[i+1 - self.size])
        

    def jump_func_3(self, i) -> None:
        if i > 0 and i < self.size - 1:
            self.X[i] = sum_mod_2(self.X_0[i-1], sum_mod_2(self.X_0[i],self.X_0[i+1]))
        else:
            self.X[i] = sum_mod_2(self.X_0[i-1], sum_mod_2(self.X_0[i],self.X_0[i+1 - self.size]))
        
        
        
    def make_step(self) -> None:
        for i in range(len(self.X_0)):
            eval(f"self.{self.func_name}({i})")
        # print(any(self.X_0 == self.X))
        self.X_0 = deepcopy(self.X)

            

    def start_sim(self) -> None:
        if self.vis:
            if self.vis_mech == "plt":
                self.ani_plt()
        else:
            for i in range(self.Niter): 
                self.make_step()


    
    
    def print_map(self) -> None:
        print(self.X_0)
        
 

    def vis_map1d_plt(self, i, fig, ax, zer = False):
        if i == 0:
            self.X_0 = deepcopy(self.X_00)
            self.X = deepcopy(self.X_00)
            self.Z = np.zeros((self.Niter, self.size))
        else:
            self.make_step()
        # self.Z[self.Niter - 1 - i] = self.X
        self.Z[i] = self.X
        
        if i == 0:
            self.pl = ax.matshow(self.Z)

            return self.pl,
        # self.pl = ax.pcolormesh(self.Z, edgecolors='k', linewidths=1)
        # self.pl, = ax.plot(self.X)
        # self.pl = ax.scatter(np.nonzero(self.X), [i]*len(self.X[self.X == 1]))
        else:
            self.pl.set_data(self.Z)
            ax.set_title(f"Iteration: {i}")
            return self.pl,

        # return mesh,
        
              
    def vis_shell(self):
        fig, ax = plt.subplots()
        plt.axis('off')
        return fig, ax
    
    def ani_plt(self):
            fig, ax = self.vis_shell()
            self.vis_map1d_plt(i = 0, fig = fig, ax = ax, zer = True)
            ani = animation.FuncAnimation(
                fig, partial(self.vis_map1d_plt, fig = fig, ax = ax, zer = False),
                # init_func=partial(self.vis_map1d_plt, i = 0, fig = fig, ax = ax),
                interval=10, blit=True, frames = self.Niter, repeat=False)
            plt.show()
            # ani.event_source.stop()
            # self.pl.set_animated(False)
            # fig.canvas.draw_idle()
            # ani.event_source.start()
                # init_func=partial(self.vis_map1d_0, fig = fig, ax = ax),)
            
            # ani = animation.TimedAnimation(
            #     fig, partial(self.vis_map1d, fig = fig, ax = ax), repeat=False)
            # writer = animation.PillowWriter(fps=15,
            #                                 metadata=dict(artist='Me'),
            #                                 bitrate=1800)
            # ani.save('Serpinsky.gif', writer=writer)
            # ani.to_jshtml(10)
        

        