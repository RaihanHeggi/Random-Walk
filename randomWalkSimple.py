import random
import matplotlib.pyplot as plt

def main():
    x = 0
    y = 0
    i = 0
    step = 100
    listLoopinganX = []
    listLoopinganY = []
    listLoopinganX.append(x)
    listLoopinganY.append(y)
    print('(x,y) = (',x,',',y,')')
    cek = True
    while (cek):
        r = random.randint(0,100)
        if((r >0) and (r<=19)):
            y += 1 
        elif((r>19) and (r<=43)):
            x += 1
            y += 1
        elif((r>43) and (r<=60)):
            x += 1
        elif((r>60) and (r<=70)):
            x += 1
            y -= 1
        elif((r>70) and (r<=72)):
            y -= 1
        elif((r>72) and (r<=75)):
            x -= 1
            y -= 1
        elif((r>75) and (r<=85)):
            x -= 1
        elif((r>85) and (r<=100)):
            x -= 1
            y += 1
        else : 
            print('Error')
            cek = False
        if(i == step):
            cek = False
        else :
            listLoopinganX.append(x)
            listLoopinganY.append(y)
            print('(x,y) = (',x,',',y,')')
            i+= 1               

    plt.figure()
    plt.title('Blind Hiker Route')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.plot(listLoopinganX,listLoopinganY)
    plt.show()
    print(step)
    print('Selesai')

   
    
if __name__ == '__main__':
    main()
    
    

