
# multiprocessing basics

import multiprocessing
import time

def f():
	''' fill this code '''

    pass
    
def do_multiproc():
    # create four processes
    proc_1 = multiprocessing.Process(target = f)
    proc_2 = multiprocessing.Process(target = f)
    proc_3 = multiprocessing.Process(target = f)
    proc_4 = multiprocessing.Process(target = f)

    # start processes
    proc_1.start()
    proc_2.start()
    proc_3.start()
    proc_4.start()
  
    # block the execution of the processes until they terminate 
    proc_1.join()
    proc_2.join()
    proc_3.join()
    proc_4.join()

def main():
    do_multiproc()
  
if __name__ == '__main__':
    main()
  

