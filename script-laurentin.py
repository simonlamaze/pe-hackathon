import numpy as np
import matplotlib.pyplot as plt
from xcover import covers_bool
n=10
T = np.zeros((n,n))
T[5:,5:]=2
T[-1,-1]=1
def Transform(piece,T,dico):
    k = len(dico)
    l = np.sum(T!=2)
    t1= np.zeros(k)
    t2=T.reshape((1,-1))[0]
    t2= [i for i in t2 if i != 2]
    t1[list(dico).index(piece)]=1
    return np.concatenate((t1,t2))

print(Transform("Z",T,{"U":1,"Z":4}))

def BigT(dico):
    Input = [Transform(key, t, dico) for key, value in dico.items() for t in value]
    return next(covers_bool(Input)


