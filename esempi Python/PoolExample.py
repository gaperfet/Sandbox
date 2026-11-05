import multiprocessing as mp
import os 

def cube(x):
    print (str(os.getpid())+" "+str(os.getppid())) #stampa processo figlio e processo padre
    return x**3    # la funzione restituisce x^3


#MAIN
if __name__=="__main__":
    pool = mp.Pool(processes=4) # inizzializza 4 processi
    results = pool.map_async(cube,range(1,7)) # Pool.map fa partire i processi , f restituisce cubi da 1 a 6
    print(results)   # stampa la scatola vuota queue: <multiprocessing.pool.MapResult object at 0x7e7b8a37f230>
    print(results.get(timeout=1))  # stampa i risultati delle funzioni eseguite dai processi figli.

#alternative ai print(resul....)
#output = [p.get() for p in results]
#print(output)
