import numpy as numpy
import exact cover

N = np.array([0,1])
S = np.array([0,-1])
0 = np.array([-1,0])
E = np.array([1,0])

def rot_q_droite (piece):
    .

def rot_180 (piece):

def rot_q_droite (dir):
    if dir==N :
        return O
    elif dir==S :
        return E
    elif dir==O :
        return S
    elif dir==E :
        return N

def rot_180_N (dir):
    if dir==N :
        return N
    elif dir==S :
        return S
    elif dir==O :
        return E
    elif dir==E :
        return O

def rot_180_O (dir):
    if dir==N :
        return S
    elif dir==S :
        return N
    elif dir==O :
        return O
    elif dir==E :
        return E
{   
"F": [[1, 1, 0], [0, 1, 1], [0, 1, 0]],
"I": [[1, 1, 1, 1, 1]],
"L": [[1, 0, 0, 0], [1, 1, 1, 1]],
"N": [[1, 1, 0, 0], [0, 1, 1, 1]],
"P": [[1, 1, 1], [1, 1, 0]],
"T": [[1, 1, 1], [0, 1, 0], [0, 1, 0]],
"U": [[1, 1, 1], [1, 0, 1]],
"V": [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
"W": [[1, 0, 0], [1, 1, 0], [0, 1, 1]],
"X": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
"Y": [[0, 1, 0, 0], [1, 1, 1, 1]],
"Z": [[1, 1, 0], [0, 1, 0], [0, 1, 1]], }

{  "F": [N,E,O,N,O],
    "I": [N,N,N,N],
    "L": [O,N,N,N],
    "N": [E,S,E,E],
    "P": [N,E,N,O],
    "T": [N,N,O,E,E],
    "U": [N,E,E,N],
    "V": [N,N,E,E],
    "W": [S,E,S,E],
    "X": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
    "Y": [[0, 1, 0, 0], [1, 1, 1, 1]],
    "Z": [[1, 1, 0], [0, 1, 0], [0, 1, 1]],
}