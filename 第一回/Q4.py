# maximum subarray problem

def max(a):
    max_sum = 0
    for i in range(len(a)):
        for j in range(i,len(a)+1):
            if sum(a[i:j]) >= max_sum:
                max_sum = sum(a[i:j])
    return max_sum

def test():
    a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(max(a) == 43)

test()
