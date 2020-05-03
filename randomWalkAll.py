import random
import matplotlib.pyplot as plt

def calculateDegree(n,ne,e,s,se,w,sw,nw,step,totalPerulangan):
    nPercentage = (n/(step*totalPerulangan))*100
    nePercentage = (ne/(step*totalPerulangan))*100
    ePercentage = (e/(step*totalPerulangan))*100
    sPercentage = (s/(step*totalPerulangan))*100
    sePercentage = (se/(step*totalPerulangan))*100
    wPercentage = (w/(step*totalPerulangan))*100
    swPercentage = (sw/(step*totalPerulangan))*100
    nwPercentage = (nw/(step*totalPerulangan))*100
    mostWalk = max(nPercentage,nePercentage,ePercentage,sPercentage,sePercentage,wPercentage,swPercentage,nwPercentage)
    print("Arah ke N : ",nPercentage)
    print("Arah ke NE : ",nePercentage)
    print("Arah ke E: ",ePercentage)
    print("Arah ke S : ",sPercentage)
    print("Arah ke SE : ",sePercentage)
    print("Arah ke W : ",wPercentage)
    print("Arah ke SW : ",swPercentage)
    print("Arah ke NW : ",nwPercentage)
    if(mostWalk == nPercentage):
        print("Arah Terbanyak N = ",mostWalk)
    elif(mostWalk == nePercentage):
        print("Arah Terbanyak NE = ",mostWalk)
    elif(mostWalk == ePercentage):
        print("Arah Terbanyak E = ",mostWalk)
    elif(mostWalk == sPercentage):
        print("Arah Terbanyak S = ",mostWalk)
    elif(mostWalk == sePercentage):
        print("Arah Terbanyak SE = ",mostWalk)
    elif(mostWalk == wPercentage):
        print("Arah Terbanyak W = ",mostWalk)
    elif(mostWalk == swPercentage):
        print("Arah Terbanyak SW = ",mostWalk)
    else:
        print("Arah Terbanyak NW = ",mostWalk)
    print("SELESAI")

def main():
    x = 0
    y = 0
    i = 0
    step = 100
    totalPerulangan = 10
    listLoopinganX = [[0 for i in range(step)] for j in range(totalPerulangan)]
    listLoopinganY = [[0 for i in range(step)] for j in range(totalPerulangan)]
    n = 0
    nCoordinate =0
    neCoordinate = 0
    eCoordinate = 0
    sCoordinate = 0
    seCoordinate = 0
    wCoordinate = 0
    swCoordinate = 0
    nwCoordinate = 0
    cek = True
    for n in range(totalPerulangan) :
        cek = True
        for i in range(step):
            if(i == 0): 
                x = 0
                y = 0
                listLoopinganX[n][i] = x
                listLoopinganY[n][i] = y
                print('(x,y) = (',x,',',y,')')
            else:
                r = random.randint(0,100)
                if((r>=0) and (r<=19)):
                    y += 1 
                    nCoordinate += 1
                    listLoopinganX[n][i] = x
                    listLoopinganY[n][i] = y
                    print('(x,y) = (',x,',',y,')')    
                elif((r>19) and (r<=43)):
                    x += 1
                    y += 1
                    neCoordinate += 1
                    listLoopinganX[n][i] = x
                    listLoopinganY[n][i] = y
                    print('(x,y) = (',x,',',y,')')   
                elif((r>43) and (r<=60)):
                    x += 1
                    eCoordinate += 1
                    listLoopinganX[n][i] = x
                    listLoopinganY[n][i] = y
                    print('(x,y) = (',x,',',y,')')   
                elif((r>60) and (r<=70)):
                    x += 1
                    y -= 1
                    seCoordinate += 1
                    listLoopinganX[n][i] = x
                    listLoopinganY[n][i] = y
                    print('(x,y) = (',x,',',y,')')   
                elif((r>70) and (r<=72)):
                    y -= 1
                    sCoordinate += 1
                    listLoopinganX[n][i] = x
                    listLoopinganY[n][i] = y
                    print('(x,y) = (',x,',',y,')')   
                elif((r>72) and (r<=75)):
                    x -= 1
                    y -= 1
                    swCoordinate += 1
                    listLoopinganX[n][i] = x
                    listLoopinganY[n][i] = y
                    print('(x,y) = (',x,',',y,')')   
                elif((r>75) and (r<=85)):
                    x -= 1
                    wCoordinate += 1
                    listLoopinganX[n][i] = x
                    listLoopinganY[n][i] = y
                    print('(x,y) = (',x,',',y,')')   
                elif((r>85) and (r<=100)):
                    x -= 1
                    y += 1
                    nwCoordinate += 1
                    listLoopinganX[n][i] = x
                    listLoopinganY[n][i] = y
                    print('(x,y) = (',x,',',y,')')   
                else :
                    print('Error')
                    cek = False
                    break           
        if(not(cek)):
            break        
    x = 0
    plt.title('Blind Hiker Route')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    while x<=n:
        plt.plot(listLoopinganX[x],listLoopinganY[x])
        x+=1
    plt.show()
    calculateDegree(nCoordinate,neCoordinate,eCoordinate,sCoordinate,seCoordinate,wCoordinate,swCoordinate,nwCoordinate,step,totalPerulangan)
   
    
if __name__ == '__main__':
    main()
    
    

