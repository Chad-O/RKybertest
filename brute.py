import numpy as np
import time as t
#S {-3,-2,-1,0,1,2,3}
def prepT(val):
    val1 = 0
    val2 = 0
    val3 = 0
    for i in range (len(val)):
        val1 += val[i][0]
        val2 += val[i][1]
        val3 +=val[i][2]
    
    res = np.array([val1,val2,val3])
    return res



def gen():

    skey = np.array([1,2,3])
    A = np.array([[1, 2, 3], [-3,-2, -1], [1, 2, 3],[-3,-2,-1]])
    val = A*skey
    print(len(A))
    tkey = prepT(val)
    print(np.poly1d(tkey))
    print(skey)
    restuple = (skey,A,tkey)
    return restuple
    
#gen()

def rangen(dicc):
    
    
    skey = np.random.randint(-3,3,3)
    print(skey)
    A = np.random.randint(-3,3,(4,3))
    print(A)
    tkey = prepT(A*skey)
    print(np.poly1d(tkey))
    restuple = (skey,A,tkey)


#rangen()

def brute(resgen):
    
    dicc = {}
    
    skey = resgen[0]
    A = resgen[1]
    tkey = resgen[2]
    rangen = rangen(dicc)

    while tkey != rangen[2]:
        if tkey not in dicc:
            dicc[skey] = (tkey,A)
        
    print("Collision")
    print(dicc[skey])
    print(skey)
    print(A)
    print(tkey)



