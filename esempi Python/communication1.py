import multiprocessing
# empty list with global scope 
result = [] 
#
def square_list(mylist): 
        global result  #Anche scrivendo globale i processi hanno propria memoria ,non modificano quella in main
        for num in mylist: 
                result.append(num * num) 
        print("Result(in process p1): "+str(result)) 
 
#MAIN
if __name__=="__main__":
    # input list 
    mylist = [1,2,3,4] 
    # creating new process 
    p1 = multiprocessing.Process(target=square_list, args=(mylist,)) 
    # starting process 
    p1.start() 
    # wait until process is finished 
    p1.join() 
        
    # print global result list 
    print("Result(in main program): "+str(result)) #in result del padre , la lista è rimasta vuota.
        
