import numpy as np
from xcover import covers_bool
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
        return None  # si la pièce ne rentre pas
    else : 
        T = tableau 
        T[case[0]:case[0]+n,case[1]:case[1]+p]=shape
    return T


tableau = np.zeros((12,5))
Dicotableaux={}
for key in Dicosymrot:
    Dicotableaux[key]=[]
    for shape in Dicosymrot[key]:
        for i in range (12):
            for j in range (5):
                c =configuration (shape, [i,j] , tableau )
                if isinstance(c,np.ndarray):
                 Dicotableaux[key].append(c)

#print(Dicotableaux)


######

diconum= {  "F": 1,
    "I": 2,
    "L": 3,
    "N": 4,
    "P": 5,
    "T": 6,
    "U": 7,
    "V": 8,
    "W": 9,
    "X": 10,
    "Y": 11,
    "Z": 12,
}


def liste ( piece , tableau ):
    L=diconum[piece]
    n,p = tableau .shape
    for i in range (n):
        for j in range (p):
            L.append(tableau[i,j])
    return L
# retourne la liste correcte d'une pièce et d'un tableau associé
Liste_config =[]

# for key in dicotableaux:
#     for tableau in dicotableaux[key]:
#         Liste_config.append(liste ( key , tableau ))

####
def Transform(piece,T,dico):
    k = len(dico)
    t2=T.reshape((1,-1))[0]
    t1= np.zeros(k)
    t2= [i for i in t2 if i != 2]
    t1[list(dico).index(piece)]=1
    return np.concatenate((t1,t2),axis=None)
    

def BigT(dico):
    Input=[]
    for key, value in dico.items():
        for t in value:
         Input.append(Transform(key, t, dico))
    return np.array(Input)

solutions = covers_bool(BigT(Dicotableaux))


print(next(solutions))


        

    
    


