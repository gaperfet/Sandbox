from multiprocessing import Process

def f(name):
    print('Hello '+name)  #il + concatena due stringhe, lo spazio sta gia in una delle stringhe

#MAIN
if __name__=="__main__":  # a __name__  viene assegnato un valore allinizio processo nel caso del processo padre
                        # è proprio __main__ allora esegue il blocco . quando parte il proc. figlio il valore
                        # __name__ cambia , allora non esegue il blocco e non avro pro. nipoti indesiderati
    p = Process(target=f, args=('World',)) #crea il nuovo proc. non lo esegue ,nota la ','necessaria dopo world.
    p.start()   #avvia processo figlio , legge il questo file,poi esegue la funzione f. (==main darà False)
    p.join()    # garantisce che la funzione padre aspetti la fine della funzione figlio.
