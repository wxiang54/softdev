def union(A, B):
    return A + [i for i in B if i not in A]

def intersect(A, B):
    return [i for i in A if i in B]

def set_diff(U, A):
    return [i for i in U if i not in A]

def sym_diff(A, B):
    return set_diff( union(A, B), intersect(A, B) )

def cart_product(A, B):
    return [(i, j) for i in A for j in B]



#########################################################
####################   TEST CASES   #####################
#########################################################

def test(case):
    return "{} -> {}".format( case, eval(case) )

if __name__ == "__main__":
    print "\ntesting union..."
    print test("union([1, 2, 3], [2, 3, 4])")
    print test("union([], ['a', 'b'])")

    print "\ntesting intersect..."
    print test("intersect([1, 2, 3], [2, 3, 4])")
    print test("intersect(['a', 'b'], ['c', 'd'])")

    print "\ntesting set_diff..."
    print test("set_diff([1, 2, 3], [2, 3, 4])")
    print test("set_diff(['a', 'b', 'c'], ['b'])")

    print "\ntesting sym_diff..."
    print test("sym_diff([1, 2, 3], [2, 3, 4])")
    print test("sym_diff(['a', 'b'], ['c', 'd'])")
    
    print "\ntesting cart_product..."
    print test("cart_product([1, 2], ['red', 'white'])")
