#!/usr/bin/env python3

import numpy as np
import scipy as sp
import sympy as smp
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys


def instant_distance(W,L,A,deg=0, *args, **kwargs):
    r = np.radians(deg)
    R = np.array(
            [[np.cos(r),-np.sin(r), 0],
             [np.sin(r), np.cos(r), 0],
             [0, 0, 1]]
        )
    p1 = np.array([A-np.cos(r)*L ,-A, 0]).T
    p2 = np.array([A, -A+np.sin(r)*L, 0]).T
    p3 = p1 + R@np.array([0, W, 0]).T
    p4 = p2 + R@np.array([0, W, 0]).T
    O = np.array([0, 0, 0]) # for completeness. Point to which measure distance

    if L == 0: # if L is 0, the cart is either a point or a line. Minimal distance measured at corner when at 45°
        if deg == 0:
            d = np.inf
        elif deg == 45:
            d = np.sqrt(2)*A - W
        elif deg == 90:
            d = np.inf
        elif deg < 45:
            d = A/np.sin(r) - W
        elif deg > 45:
            d = A/np.cos(r) - W
    else: 
        cross = np.cross(p4-p3, O-p3) # area of parallelogram, to compute distance
        dot = np.dot(p4-p3, O-p3)/np.dot(p4-p3,p4-p3)  # used to compute position of point along line, from 0 to 1
        d = cross[2]/np.linalg.norm(p4-p3)
        if dot < 0 or dot > 1:
            d = np.inf
    
    if 'plot' in kwargs and kwargs['plot']==True:
        ptloop = np.column_stack([p1, p2, p4, p3, p1])
        plt.plot(ptloop[0,:], ptloop[1,:], linewidth=2)
        
        Oline = np.column_stack([O, (p3+dot*(p4-p3))])
        plt.plot(Oline[0,:], Oline[1,:], linewidth=2)

        plt.plot([-A, 0, 0], [0, 0, A], 'k', linewidth=2)
        plt.plot([-A, A, A], [-A, -A, A], 'k', linewidth=2)
        plt.grid(True)
        plt.axis('equal')
        plt.show(block=False)
    return d

def minimal_distance(W, L, A, degvec=np.linspace(0, 90, 91), *args, **kwargs):
    d = []
    for deg in degvec:
        d.append(instant_distance(W,L,A,deg))

    idx_min = np.argmin(d) 

    if 'plot' in kwargs and kwargs['plot']==True: 
        plt.plot(degvec, d, label="min: "+str(d[idx_min])+"@"+str(degvec[idx_min]))
        plt.legend()
        plt.show(block=False)
    return (d[idx_min], degvec[idx_min])

def minimal_distance_adimensional(pi1, pi2, *args, **kwargs):
    A = 1 #force value of A
    W = pi1*A 
    L = pi2*A 
    d, theta = minimal_distance(W,L,A)
    pi3 = d/A
    return pi3, theta

def minimal_distance_adimensional_sweep(pi1range, pi2range):
    pi1mg, pi2mg = np.meshgrid(pi1range, pi2range) 
    pi3mg = np.zeros(pi1mg.shape)
    themg = np.zeros(pi1mg.shape)
    for i in range(len(pi1range)):
        for j in range(len(pi2range)):
            pi3mg[j,i], themg[j,i] = minimal_distance_adimensional(pi1range[i], pi2range[j])
    return pi3mg, pi1mg, pi2mg, themg

def minimal_distance_adimensional_expression(pi1, pi2):
    p00 = np.array((0,0,np.sqrt(2)))
    p10 = np.array((1,0,np.sqrt(2)-1))
    p01 = np.array((0,np.sqrt(8), 0))
    
    dp10 = p10-p00 
    dp01 = p01-p00

    m1 = dp10[2]/dp10[0] 
    m2 = dp01[2]/dp01[1]

    pi3 = p00[2] + pi1*m1 + pi2*m2
    return pi3
    
if __name__=="__main__":
    #(d, ang) = minimal_distance(0.5, 0.5, 1, plot=True)
    (pi3, pi1, pi2, theta) = minimal_distance_adimensional_sweep(pi1range=np.linspace(0,1,50), pi2range=np.linspace(0.0,np.sqrt(8),100))

    fig = plt.figure()
    ax = fig.add_subplot(1,2,1,projection="3d")
    idx = np.where(pi3<0)
    pi3[idx] = np.nan
    ax.plot_surface(pi1, pi2, pi3)
    ax.set_xlabel('pi1: W/A')
    ax.set_ylabel('pi2: L/A')
    ax.set_zlabel('pi3: d/A')

    pi3num = minimal_distance_adimensional_expression(pi1, pi2)
    ax = fig.add_subplot(1,2,2,projection="3d")
    #idx = np.where(pi3<0)
    #theta[idx] = np.nan
    ax.plot_surface(pi1, pi2, pi3num)
    ax.set_xlabel('pi1: W/A')
    ax.set_ylabel('pi2: L/A')
    ax.set_zlabel('pi3: d/A')
    plt.show()
    # input()

