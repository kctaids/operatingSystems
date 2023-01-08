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
        else:
            pass
        if len(ready_queue) != 0 :
            ready_queue.sort(key = lambda x :x[2])
            running = ready_queue.pop(0)
            ct += running[2]
            print(ct)
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
