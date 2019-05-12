def auto():
    for i in range(1,10):
        for j in range(1,i+1):
                print("%dx%d=%-3d"%(i,j,i*j),end='')
        print()
auto()
