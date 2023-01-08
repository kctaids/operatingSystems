def find(process):
    process.sort(key = lambda x :x[1])
    tat,wt = [], []
    ct = 0
    for i in process:           
        if i[1] <= ct: ct += i[2]
            
        else: ct += ct-i[1] + i[2]
            
        tat.append(ct - i[1])
        wt.append(ct - i[2] -  i[1] )
    return tat, wt

process  = [[1,0,10],[2,0,5],[3,0,8]]
tat, wt = find(process)
print('turn around time of each process' , tat)
print('waiting time of each process' ,wt)
print(f'average waiting time {sum(tat)/len(tat)}, average turn around time {sum(wt)/len(wt)}')
