def prior(process):
    process.sort(key = lambda x :x[1])
    bts = {}
    for i in process:
        bts[i[0]] = i[2]
    tat , wt = {} , {}
    ct = 0
    ready_queue = []
    already_sent = []
    while True:
        for i in process:
            if ct  == i[1] and i[0] not in already_sent :
                ready_queue.append(i)    
        if len(ready_queue) != 0:
            ready_queue.sort(key = lambda x :x[3])
            running = ready_queue [0]
            

            running[2] -= 1
            ct += 1
            if running[2] == 0:
               
                already_sent.append(running[0])
                ready_queue.pop(0)
                tat[running[0]] = ct - running[1]
                print(running[1],running[0])
                wt[running[0]] = ct - running[1] - bts[running[0]]
            else:
                ready_queue[0] = running
        else:
            ct += 1
        print(ct)
        if len(list(tat.keys())) == len(process):
            print(tat)
            return tat, wt , bts

proess  = [[1,3,5,3],[2,4,6,1],[3,5,8,2]]
prior(proess)
