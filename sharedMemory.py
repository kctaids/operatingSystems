import multiprocessing

def square_list(mylist, result, square_sum):
    for idx, num in enumerate(mylist): 
        result[idx] = num * num
    print(f"Result(in process p1): {result[:]}")
    print(f"Sum of squares(in process p1): {square_sum.value}")

if   name   == "__main ": 
    mylist = [1,2,3,4]
    result = multiprocessing.Array('i', 4)
    p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))
    print(f"Result(in main program): {format(result[:]}")
    print(f"Sum of squares(in main program): {(square_sum.value}")
