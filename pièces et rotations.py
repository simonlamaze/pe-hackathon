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



dicopiecesD= {  "F": [N,E,O,N,O],
    "I": [N,N,N,N],
    "L": [O,N,N,N],
    "N": [E,S,E,E],
    "P": [N,E,N,O],
    "T": [N,N,O,E,E],
    "U": [N,E,E,N],
    "V": [N,N,E,E],
    "W": [S,E,S,E],
    "X": [N,O,E,E,O,N],
    "Y": [E,N,S,E,E],
    "Z": [E,S,S,E],
}


RAW_SHAPES = {   
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


PENTOMINOS = [np.array(shape) for shape in RAW_SHAPES.values()]

def demi_tourh(shape): # retourne horizontalement
    S = shape[::-1]
    return S

def demi_tourv(shape): # retourne verticalement en passant par la transposée
    S=np.transpose (shape)
    S = S[::-1]
    return np.transpose(S)

def sym_rot(shape):
    L=[demi_tourh(demi_tourv(shape)),demi_tourv(shape),demi_tourh(shape),shape] # IL manque les transposées
    Liste=[]
    for T in L :
        Liste.append (np.transpose(T))
        Liste.append (T)
    return Liste  # on a potentiellement des répétitions


Dicosymrot={}
for key in RAW_SHAPES :
    Dicosymrot[key]= sym_rot(np.array(RAW_SHAPES[key]))

print(Dicosymrot)


#######

def configuration (shape, case , tableau ): # dim(shape)=2
    n, p =shape.shape
    N,P= tableau.shape
    if case[0]+n > N or case[1]+p > P :
        return none  # si la pièce ne rentre pas
    else : 
        T = tableau 
        T[case[0],case[0]+n:,[case[1],case[1]+p:]=shape
    return T


tableau = np.zeros(12,5)
Dicotableaux={}
for key in Dicosymrot:
    Dicotableaux[key]=[]
    for shape in Dicosymrot[key]:
        for i in range (12):
            for j in range (5):
                Dicotableaux[key].append(configuration (shape, [i,j] , tableau ))

return Dicotableaux
        

    
    


