# Bottom-up sol
def bottom_up_sol():    
    X = int(input())
    op_count = [0]*(X+1)

    for i in range(2,X+1):
        devide_by_3 = X + 1
        devide_by_2 = X + 1
        minus_1 = X + 1

        if i % 3 == 0:
            devide_by_3 = op_count[i//3] + 1
        if i % 2 == 0:
            devide_by_2 = op_count[i//2] + 1
        minus_1 = op_count[i-1] + 1

        op_count[i] = min(devide_by_2, devide_by_3, minus_1)

    print(op_count[X])

# Top down sol
def SearchMinOp(X, op_count):
    if op_count[int(X)] != len(op_count):
        return op_count[int(X)]
    else:    
        devide_by_3 = X + 1
        devide_by_2 = X + 1
        minus_1 = X + 1

        if X % 3 == 0:
            devide_by_3 = SearchMinOp(X/3, op_count) + 1
        if X % 2 == 0:
            devide_by_2 = SearchMinOp(X/2, op_count) + 1
        minus_1 = SearchMinOp(X-1, op_count) + 1
        
        op_count[int(X)] = min(devide_by_2, devide_by_3, minus_1)
        return op_count[int(X)]

def top_down_sol():
    X = int(input())
    op_count = [X+1]*(X+1)
    op_count[1] = 0

    print(SearchMinOp(X, op_count))

if __name__ == "__main__":
    bottom_up_sol()