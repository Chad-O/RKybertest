from rich import print as PR
from rich.console import Console
from rich.table import Table
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

    skey = np.array(([-3,-3,-3],[-3,-3,-3]))
    A = np.array([[0,0,0],[0,0,0]])
    #A = np.array([[1, 2, 3], [-3,-2, -1], [1, 2, 3],[-3,-2,-1]])
    val = A*skey
    #print(len(A))
    tkey = prepT(val)
    #print(np.poly1d(tkey))
    #print(skey)
    restuple = (skey,A,tkey)
    return restuple
    
#gen()
def printgen(restuple):
    skey = restuple[0]
    A = restuple[1]
    tkey = restuple[2]
    cont = restuple[3]
    resgen = restuple[4]
    PR("Iteracion: ",cont,": ")
    table  = Table(title="Polinomios")
    table.add_column("Nombre")
    table.add_column("Valor buscado")
    table.add_column("Valor actual")
    
    table.add_row("Matriz A",str(A),str(resgen[1]))
    table.add_row("Llave Privada",str(skey),str(resgen[0]))
    table.add_row("Llave Publica",str(tkey),str(resgen[2]))

    console = Console()
    console.print(table)

#resgen = [skey,A,tkey] de gen
#restuple = [skey,A,tkey,cont,resgen] de gens

def gens(resgen):
    
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
                                for a in range(0,17): #16^12+7^6
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
                                                        restuple = (skey,A,tkey,cont,resgen)
                                                        printgen(restuple)

                                                        #print(np.poly1d(a3))
                                                        #print(np.poly1d(a4))
                                                        if resgen[0].all()==skey.all() and resgen[1].all()==A.all() and resgen[2].all()==tkey.all():
                                                            PR("[bold red]Collision[/bold red]")
                                                            print(skey)
                                                            print(A)
                                                            print(tkey)
                                                            end = t.time()
                                                            print("Iteraciones total: ",cont)
                                                            print("Tiempo: ",end-st)
                                                            return  
        end = t.time()
        print("Iteraciones total: ",cont)
        print("Tiempo: ",end-st)

def brute(resgen):
    dicc = {}
    print(resgen[0])
    skey = resgen[0]
    A = resgen[1]
    tkey = resgen[2]
    gens(resgen)

brute(gen())



