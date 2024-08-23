arr = [
    list(map(int, input().strip().split(' '))) for _ in range(4)
]

direc = input()
# direc = 'L'

def rot_90():
    global arr
    tr = list(zip(*arr))
    rot_arr = [list(trow[::-1]) for trow in tr]
    arr = rot_arr


# def rot_90_left():
#     rot_left_arr = [list(row[::-1]) for row in arr]



# 열 0부터 돌면서 밑에서부터 하나씩 올라가고 
# tmp 배열에 넣고, 그거를 복사한다 

def fall_arr():
    # arr 0열부터 시작
    for j in range(4):
        tmp1=[]
        tmp2=[] # sum 이벤트 -> tmp1을 여기로 카피하고, 최상단에 값 더해줌
                # tmp1 다 채우면 순서대로 tmp2에 추가
        for i in range(3, -1, -1):
            cv = arr[i][j]
            if cv == 0:
                continue
            # tmp1이 비어있지 않고, cv가 tmp1의 최상단이랑 같다면 sum 이벤트
            if tmp1 and cv == tmp1[-1]:
                for ctmp in tmp1:
                    tmp2.append(ctmp)
                tmp2[-1]+=cv
                tmp1=[] # tmp1 초기화
            else:
                tmp1.append(cv)
        
        # 다 돌았으면 tmp1 내용 tmp2에 넣기
        for ctmp in tmp1:
            tmp2.append(ctmp)
        
        # tmp2 내용을 arr에 반영
        ## 먼저 0으로 다 바꾸고
        for i in range(3, -1, -1):
            arr[i][j] = 0
        
        ## tmp2를 넣는다
        arr_i_idx=3
        for ctmp2 in tmp2:
            arr[arr_i_idx][j] = ctmp2
            arr_i_idx-=1
        

# rot_arr = rot_90()
if direc == 'R':
    rot_90()
    fall_arr()
    for _ in range(3):
        rot_90()
elif direc == 'D':
    fall_arr()
elif direc == 'L':
    for _ in range(3):
        rot_90()
    fall_arr()
    rot_90()

elif direc == 'U':
    for _ in range(2):
        rot_90()
    fall_arr()
    for _ in range(2):
        rot_90()


for row in arr:
    print(*row)