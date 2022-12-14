import multiprocessing

def square_list(mylist, result, square_sum):
    for idx, num in enumerate(mylist): 
        result[idx] = num * num
    print("Result(in process p1): {}".format(result[:]))
    print("Sum of squares(in process p1): {}".format(square_sum.value))

if   name   == "__main ": 
    mylist = [1,2,3,4]
    result = multiprocessing.Array('i', 4)
    p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))
    print("Result(in main program): {}".format(result[:]))
    print("Sum of squares(in main program): {}".format(square_sum.value))
