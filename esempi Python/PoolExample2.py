import multiprocessing as mp
import time
import os
        #La f. riceve un valore da 0 a 9 , stampa quel valore e il pid del processo tra i 4 che lo esegue.
def doingstuff(x):
    print ("Process: "+str(x)+" "+str(os.getpid()))

if __name__=="__main__":
    start=time.time()
    pool = mp.Pool(processes=4)   #inizializza i 4 processi
    results = pool.map(doingstuff,range(1,10))     #parte l'assegno di 10 task tra i 4 processi
    #results =pool.map_async(doingstuff,range(1,10))
    end=time.time()
    print("elapsed time: "+str(end-start))
    print(results)  #le funzioni non hanno output eplicito , per questo trovo None
