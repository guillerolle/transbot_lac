
import sympy as smp
import numpy as np
import matplotlib.pyplot as plt

def corner_distance(pi1 = smp.Symbol(r'\pi_1'), pi2 = smp.Symbol(r'\pi_2')):
    # pi1 = W/A
    # pi2 = L/A
    # pi3 = d/A
    """ 
    if type(pi1) is not smp.Symbol:
        assert smp.simplify(pi1>=0) and smp.simplify(pi1<=1), "pi1 out of bounds!"
    if type(pi2) is not smp.Symbol:
        assert smp.simplify(pi2>=0) and smp.simplify(pi2<=smp.sqrt(8)-2*pi1), "pi2 out of bounds!"
    """
    pi3 = smp.simplify(smp.sqrt(2)-pi1-pi2/2).evalf()
    return pi3
    
def bounding_box_bool(pi1 = smp.Symbol(r'\pi_1'), pi2=smp.Symbol(r'\pi_2'), pi3=smp.Symbol(r'\pi_3')):
    # pi1 = W/A 
    # pi2 = L/A 
    # pi3 = S/A
    # output: 1, if valid
    args = (pi1, pi2, pi3)
    boundaries = [
        pi1 >= pi3,
        pi1 <= 1,
        pi2 >= pi3,
        corner_distance(pi1, pi2) >= 0
    ]

    return boundaries, args

if __name__=="__main__":
    
    
    pi3 = np.linspace(0, 1, 6)
    #fig = plt.figure()
    #axs = fig.subplots(2,3)

    bounds, args = bounding_box_bool()
    valid_region = smp.And(*bounds)
    plots = []
    for s in range(len(pi3)):
        vr = valid_region.subs({
            args[2]: pi3[s]
        })
        #ax = plt.sca(axs[(s-s%3)//2 , s%3])
        plots.append(
        smp.plot_implicit(vr,
        #(args[0],0,1), (args[1],0,smp.sqrt(8)),
        show=False)
        )
        # plots[-1].xlim = (0,1)
        # plots[-1].ylim = (0, np.sqrt(8))
        #plots[-1]._backend.ax[0].set_xlim(0, 1)
        #plots[-1]._backend.ax[0].set_ylim(0, float(smp.sqrt(8)))

    smp.plotting.PlotGrid(2,3, *plots)

    plt.show(block=False)

    """
    pi1range = np.linspace(0,1,10)
    pi2range = np.linspace(0,np.sqrt(8), 20)
    
    for s in range(len(pi3)):
        pi1,pi2 = np.meshgrid(pi1range, pi2range)
        valid = np.zeros(pi1.shape)
        for i in range(len(pi1range)):
            for j in range(len(pi2range)):
                valid[j,i] = (all(bounding_box_bool(pi1range[i], pi2range[j], pi3[s]))==True)
        plt.sca(axs[(s-s%3)//2 , s%3])
        plt.contourf(pi1,pi2,valid)
    """
    plt.show()
    
pass