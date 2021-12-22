
# multiprocessing with shared memeory

import os, multiprocessing

def f(lst, val):
    for i, v in enumerate([2, 4, 6, 8]):
    
    # cannot use append method (why?)
    lst[i] = v
  
    # you need [:] operator to convert it into normal list form
    # you need value method of Value class to access or assign values
    val.value = sum(lst[:])
    print ('lst = ', lst[:])
    print ('sum = ', val.value)
  
def g():
    # lst should hold 4 'i'nteger values 
    lst = multiprocessing.Array('i', 4)

    # val should hold integer value
    val = multiprocessing.Value('i')

    # you can give initial value as
    val = multiprocessing.Value('i', 0)

    # you should give the Array and Value objects as arguments
    proc_1 = multiprocessing.Process(target = f, args = (lst, val))

    proc_1.start()
    # lst = [2, 4, 6, 8]
    # sum = 20

    # changes are reflected in the main process
    print(lst[:]) # [2, 4, 6, 8]
    print(val.value) # 20

def main():
    g()
    
if __name__ == '__main__':
    main()
    

