
import numpy as np
import time as t

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
def rangen(dicc):
    
    
    skey = np.random.randint(-3,3,3)
    print(skey)
    A = np.random.randint(-3,3,(4,3))
    print(A)
    tkey = prepT(A*skey)
    print(np.poly1d(tkey))
    restuple = (skey,A,tkey)


#rangen() 
def gens():
    try:
        cont = 0
        st = t.time()
        #1 polinomio s1
        for n in range(-3,4):
            for m in range(-3,4):
                for i in range(-3,4):
                    #2 polinomio s2
                    for j in range(-3,4):
                        for k in range(-3,4):
                            for l in range(-3,4):   
                                #1 polinomio a1
                                for a in range(0,17):
                                    for b in range(0,17):
                                        for c in range(0,17):
                                            #2 polinomio a2
                                            for d in range(0,17):
                                                for e in range(0,17):
                                                    for f in range(0,17):
                                                        a1 = np.array([a,b,c])
                                                        a2 = np.array([d,e,f])
                                                        #a3 = np.array([g,h,x])
                                                        #a4 = np.array([y,z,w])
                                                        A= np.array([a1,a2])
                                                        skey = np.array(([n,m,i],[j,k,l]))
                                                        tkey = prepT(A*skey)
                                                        cont = cont + 1
                                                        print("Iteracion: ",cont,": ")
                                                        print("Polinomios s: ")
                                                        print(np.poly1d(skey[0]))
                                                        print(np.poly1d(skey[1]))
                                                        print("Matriz A: ")
                                                        print(np.poly1d(a1))
                                                        print(np.poly1d(a2))
                                                        print("Polinomio t: ")
                                                        print(np.poly1d(tkey))
                                                        #print(np.poly1d(a3))
                                                        #print(np.poly1d(a4))

   
        end = t.time()
        print("Iteraciones total: ",cont)
        print("Tiempo: ",end-st)
    except Exception as e:
        print("Error: ",e)
gens()

    

"""
                                                        #3 polinomio a3
                                                        for g in range(0,17):
                                                            for h in range(0,17):
                                                                for x in range(0,17):
                                                                    #4 polinomio a4
                                                                    for y in range(0,17):
                                                                        for z in range(0,17):
                                                                            for w in range(0,17):
"""