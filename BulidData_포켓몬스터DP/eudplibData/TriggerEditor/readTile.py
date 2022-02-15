from eudplib import *

mapSizeX = 256
mapSizeY = 256
tilesetInfo = EUDVArray(mapSizeX*mapSizeY)()
checkList = [
    [1231,0],   #1 풀
    [1118,0],   #2 언덕풀
    [8,2],      #3 내려갈 수 있는 언덕
    [9,0],      #4 파도타기 위치 (파도타기는 파도타기 위치에서만 가능하며 끝낼때도 방향에 해당 지형이 있어야 한다)
    [6,0],      #5 물 (파도타기 이동가능한 지형)
    [126,4],    #6 폭포오르기
    [1225,1],   #7 풀베기 지형
    [1493,1],   #8 락클라임
    [1377,1],   #9 자전거도로 (자전거를 탄 상태에서만 지나갈 수 있는 도로)
]


def TilesetInit():
    def tileset(x,y):
        a,b = divmod((16*x)+y,256)
        return b, a

    checkX, checkY = [], []
    for i in range(0, len(checkList)):
        tempX,tempY = tileset(checkList[i][0], checkList[i][1])
        checkX.append(tempX)
        checkY.append(tempY)
    print("checkX :",checkX, "checkY :",checkY)
    chkt = GetChkTokenized()
    MTXM = bytearray(chkt.getsection("MTXM"))
    print("MapSize:",mapSizeX,"x",mapSizeY)
    total = [0 for _ in range(len(checkList))]
    for i in range(0,mapSizeX):
        for j in range(0,mapSizeY):
            index = mapSizeX*j + i
            l = index*2
            for k in range(0, len(checkList)):
                if(MTXM[l] == checkX[k] and MTXM[l+1] == checkY[k]):
                    tilesetInfo[index] = k+1
                    total[k] += 1
                    break
    print("풀때기 :", total[0], "언덕 :", total[1])