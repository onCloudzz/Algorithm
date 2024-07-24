from sys import stdin
def changeCntB(chess):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0 and chess[i][j] == 'B':
                cnt += 1
            elif (i+j) % 2 == 1 and chess[i][j] == 'W':
                cnt += 1
    return cnt

def changeCntW(chess):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0 and chess[i][j] == 'W':
                cnt += 1
            elif (i+j) % 2 == 1 and chess[i][j] == 'B':
                cnt += 1
    return cnt

# 보드 크기 읽기
N, M = map(int, stdin.readline().split())

# 보드 읽기
board = [stdin.readline().strip() for _ in range(N)]

# 최소 재도색 횟수 초기화
min_cnt = float('inf')

# 8x8 윈도우를 보드 전체에 슬라이드
for i in range(N - 7):
    for j in range(M - 7):
        # 8x8 서브 보드 추출
        chessboard = [board[x][j:j + 8] for x in range(i, i + 8)]
        
        # 두 가지 시작 패턴에 대한 재도색 횟수 계산
        cnt1 = changeCntB(chessboard)
        cnt2 = changeCntW(chessboard)
        cnt = min(cnt1, cnt2)
        
        # 최소 재도색 횟수 업데이트
        if i == 0 and j == 0:
            min_cnt = cnt
        else:
            min_cnt = min(min_cnt, cnt)

print(min_cnt)