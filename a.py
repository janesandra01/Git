def auto():
    for i in range(1,10):
        for j in range(1,i+1):
                print("%dx%d=%-3d"%(j,i,i*j),end='')
        print()
auto()
print("九九乘法表")

