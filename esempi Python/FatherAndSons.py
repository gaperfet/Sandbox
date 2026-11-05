from multiprocessing import Process
import os   #per usare funzione di lettura codici pid
def f0(name):
    print()   # stampa uno spazio, solo per separare visivamente una riga da un altra
    print("-----> function "+name)
    print ("I am still the main process with ID "   #indica che questo print lo lancia il processo padre
           +str(os.getpid())+" my father is ID:"+str(os.getppid()))    #getpid mi da il pid del processo padre
    # il getppid dara il pid padre del padre, o il programma che lancia la run (pycharm  o terminale)
def f1(name):
    print()
    print("-----> function "+name)
    print ("I am the first sub-process with ID "  #stampa i pid del processo figlio e poi padre
           +str(os.getpid())+" my father is ID:"+str(os.getppid()))  #stampa pid figlio e del padre
    f2('two')  #fa partire f2  , non ci sono altri processi figli solo padre e  figlio


def f2(name):
    print()                        # ultima funzione eseguita stamperà gli stessi dati di f1
    print("-----> function "+name)
    print ("I am still the first sub-process with ID "
           +str(os.getpid())+" my father is ID:"+str(os.getppid()))
    print("This is the end f2!")

#MAIN
if __name__=="__main__":
    print ("I am the main process with ID: "+str(os.getpid())) #sarà la prima a stampare , pid del padre
    f0('zero')                          # fa partire la funzione f0 , che stampa pid padre e 'nonno'
    p = Process(target=f1, args=('one',))   #inizializza il nuovo processo figlio ,che eseguira f1
    p.start()                               #inizia il processo
    p.join()                                #indica al padre di aspettare il fine processo figlio
    print("end Father !") #ultimo comando esguito solo dopo che ha finito il processo figlio