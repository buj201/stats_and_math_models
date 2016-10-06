import numpy as np
import matplotlib.pyplot as plt
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def P_N_given_C_and_K(c, k):
    
    domain = range(k,21)
    function_map = {}
    
    if c == .25:
        print c
        denominator_iterable = []
        for i in domain:
            denominator_iterable.append(nCr(i, k)*(.75)**(i-k))
        denominator = math.fsum(denominator_iterable)
        for i in domain:
            function_map[i] = (nCr(i, k)*.75**(i-k))/denominator
            
    elif c == .8:
        print c
        denominator_iterable = []
        for i in domain:
            denominator_iterable.append(nCr(i, k)*(.2)**(i-k))
        denominator = math.fsum(denominator_iterable)
        for i in domain:
            function_map[i] = (nCr(i, k)*.2**(i-k))/denominator
    return function_map

c_1_4_K_1 = P_N_given_C_and_K(.25, 1)
c_1_4_K_10 = P_N_given_C_and_K(.25, 10)
c_1_4_K_19 = P_N_given_C_and_K(.25, 19)

c_4_5_K_1 = P_N_given_C_and_K(.8, 1)
c_4_5_K_10 = P_N_given_C_and_K(.8, 10)
c_4_5_K_19 = P_N_given_C_and_K(.8, 19)

plt.figure(1)
plt.subplot(211)
plt.plot(c_1_4_K_1.keys(),c_1_4_K_1.values(), 'ro', label='K = 1')
plt.plot(c_1_4_K_10.keys(),c_1_4_K_10.values(), 'bo', label='K = 10')
plt.plot(c_1_4_K_19.keys(),c_1_4_K_19.values(), 'go', label='K = 19')
plt.ylabel('P(N = n| C = 1/4, K = k)')
plt.legend(loc=9, numpoints=1)
plt.grid(True)

plt.subplot(212)
plt.plot(c_4_5_K_1.keys(),c_4_5_K_1.values(), 'ro', label='K = 1')
plt.plot(c_4_5_K_10.keys(),c_4_5_K_10.values(), 'bo', label='K = 10')
plt.plot(c_4_5_K_19.keys(),c_4_5_K_19.values(), 'go', label='K = 19')
plt.ylabel('P(N = n| C = 4/5, K = k)')
plt.xlabel('N')
plt.grid(True)
plt.legend(loc=9,numpoints=1)

q2d_fig = plt.gcf()

q2d_fig.savefig('Q2d_fig.png', bbox_inches='tight')
