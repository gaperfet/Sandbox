import multiprocessing as mp

# define a example function
def hello(pos,name):
    msg="Hello "+name  #varibile stringa che sarà uno degli output iniseme alla pos posizione
    output.put((pos, msg)) #aggiunge pos e msg in coda ai dati da passare

if __name__=="__main__":
    # Define (or create ) an output queue
    output = mp.Queue()
    # Setup a list of processes that we want to run
    processes = [mp.Process(target=hello, args=(x, "Gianluca")) for x in range(4)]

                          # Run processes
    for p in processes:
        p.start()
                          # Exit the completed processes , father process wait all the sons
    for p in processes:
        p.join()
            
    # Get process results from the output queue
    results = [output.get() for p in processes]  #il processo padre estrae tutti i dati in coda
    print(results)   #stampa , notare che a volte alcuni processi finiscono prima di altri
