def find_mwis(values):
    n = len(values)
    max_weight_values = [0, values[0]]

    for i in range(2, n+1):
        max_weight_values.append(max(max_weight_values[i-1], max_weight_values[i-2] + values[i-1]))

    i = n
    mwis = []
    while i >= 1:
        if max_weight_values[i-1] >= max_weight_values[i-2] + values[i-1]:
            i -= 1
        else:
            mwis.insert(0, values[i-1])
            i -= 2

    return mwis

def main():
    fname = "mwis.txt"
    f = open(fname, 'r')
    line = f.next()
    N = int(line)
    arr = []
    for line in f:
        arr.append(int(line.strip()))
    dic = dict(zip(arr, range(1, 1000+1)))
    S =  map(lambda x: dic[x], find_mwis(arr))
    
    for i in [1, 2, 3, 4, 17, 117, 517, 997]:
        if i in S:
            print "1",
        else:
            print "0",
    


if __name__ == "__main__":
    main()