# 바구니의 개수 N과 공 바꾸기 작업 횟수 M을 입력받습니다.
N, M = map(int, input().split())

# 바구니와 초기 공의 번호를 초기화합니다.
baskets = list(range(1, N + 1))

# M번의 공 바꾸기 작업을 수행합니다.
for _ in range(M):
    a, b = map(int, input().split())
    
    # 바구니 번호를 리스트 인덱스로 변환합니다.
    a -= 1
    b -= 1
    
    # 두 바구니의 공을 교환합니다.
    baskets[a], baskets[b] = baskets[b], baskets[a]

# 결과를 출력합니다.
for ball in baskets:
    print(ball, end=" ")