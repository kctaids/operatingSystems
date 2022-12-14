# sjf ---------------------------------------- #
#non pre emptive ------------------------------#

def sjf(process):
    process.sort(key = lambda x: x[1])
    tat , wt = {}, {}
    ct = 0
    already_sent = []
    ready_queue = []
    while True :
        for i in process:
            if i[1] <= ct and i not in already_sent :
                ready_queue.append(i)
                already_sent.append(i)
        if len(ready_queue) != 0 :
            ready_queue.sort(key = lambda x :x[2])
            running = ready_queue.pop(0)
            ct += running[2]
            tat[running[0]] = ct - running[1]
            wt[running[0]] = ct - running[2] - running[1]
        else:
            ct += 1
        if len(list(tat.keys())) == len(process):
            return tat , wt

        

process = [[1,6,1],[2,8,1],[3,7,2],[4,3,3]]
tat , wt = sjf(process)
print(tat)
print(wt)
tat = [value for key , value in tat.items()]
wt = [value for key , value in wt.items()]

print(f'avg tat {sum(tat)/len(tat)}')
print(f'avg wt {sum(wt)/len(wt)}')


# preemptive ------------------------- #

def sjfp(process):
    process.sort(key = lambda x :x[1])
    bts = {}
    for i in process:
        bts[i[0]] = i[2]
    tat , wt = {}, {}
    ct = 0 
    already_sent = []
    ready_queue = []
    while True:
        for i in process:
            if i[1] == ct and i[0] not in already_sent:
                
                ready_queue.append(i)
        if len(ready_queue) != 0:
            ready_queue.sort(key = lambda x : x[1])
            running = ready_queue[0]
            index = ready_queue.index(running)
            running[2] -= 1
            ct += 1
            if running[2] ==0 :
                already_sent.append(running[0])
                ready_queue.pop(0)
                tat[running[0]] = ct - running[1]
                wt[running[0]] = ct - running[1] - bts[running[0]]  
            else:
                ready_queue[index] = running
        else:
            ct += 1
        if len(list(tat.keys())) ==  len(process):
            return tat , wt 

process =[[1,6,1],[2,8,1],[3,7,2],[4,3,3]]
tat , wt = sjfp(process)
print(tat, wt)
