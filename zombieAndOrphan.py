import os, sys, time

ttlForParent = 60
for i in range(0, 10): 
    pid_1 = os.fork()
    print("Hello Worlds!!!") 
    if pid_1 == 0:
        sys.exit()

time.sleep(ttlForParent) 
os.wait()


pid = os.fork()

if (pid == 0): 
    time.sleep(1)
    print("I am child having PID %d\n",os.getpid()); 
    print("My parent PID is %d\n",os.getppid())
if (pid > 0):
    print("I am parent having PID %d\n",os.getpid()); 
    print("My child PID is %d\n",os.getppid()); 
    sys.exit()
