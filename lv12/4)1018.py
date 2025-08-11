## 보드 입력은 이차원 행렬로 받는다.
## 보드가 8*8을 넘어가는 큰 보드 일 경우 -> 보드의 일부분을 발췌하여 사용한다
## 내가 발췌하는 코드를 만들다기 보다는, 특정영역에서 바꿀 count가 제일 적은 부분을 선택하면 되는거 아닐까?
## 이걸 코드적으로 표현하는 방법?

def min_repaints(board, n, m):
    answer = 64  # 8x8 최대 칠하기 수
    for i in range(n - 7):
        for j in range(m - 7):
            cnt = 0  # "시작 B" 패턴 기준 불일치 수
            for r in range(8):
                for c in range(8):
                    cur = board[i + r][j + c]
                    expected = 'B' if (r + c) % 2 == 0 else 'W' ## 하나씩 바꿔갈 생각을 하지 말고 -> 이미 양식은 주어져 있으니까 expected한 값을 기준으로 비교
                    if cur != expected:
                        cnt += 1
            # 시작이 W인 경우는 64 - cnt
            repaints = min(cnt, 64 - cnt)
            if repaints < answer:
                answer = repaints
    return answer

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]
print(min_repaints(board, n, m))