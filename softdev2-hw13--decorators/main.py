from time import time
import random

def diagnostic_args(f):
    def run(*args):
        print "%s(%s)" % (f.func_name, args)
        return f(*args)
    return run

def diagnostic_time(f):
    def run(*args):
        t_init = time()
        value = f(*args)
        t_final = time()
        t_delta = t_final - t_init #in milliseconds
        print "execution time: %f seconds" % (t_delta)
        return value
    return run



#using decorators
@diagnostic_args
def fib_r(n):
    if n <= 2:
        return 1
    return fib_r(n-2) + fib_r(n-1)

@diagnostic_time
def bogo_sort(L): #a great consistent fxn to measure runtime
    while L != sorted(L):
        #fisher-yates shuffle
        for i in range(len(L)-1)[::-1]:
            rand = int(round(random.random() * (i+1)))
            tmp = L[rand]
            L[rand] = L[i]
            L[i] = tmp
    return L


# testing apparatus
if __name__ == "__main__":
    
    print "\n\n-=-= Recursive Fxn Call Diagnostics =-=-"
    print "* Function Call: fib_r(5)"
    fib_r(5)

    print "\n\n-=-= Time Diagnostics =-=-"
    print "* Function Call: bogo_sort( [1, 8, 5, 2, 6, 4, 3, 7] )"
    bogo_sort([1, 8, 5, 2, 6, 4, 3, 7])
