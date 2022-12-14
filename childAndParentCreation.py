import os

def parent_child(): 
    n = os.fork() 
    if n > 0:
        print("Parent process and id is : ", os.getpid()) 
    else:
        print("Child process and id is : ", os.getpid()) 
parent_child()
