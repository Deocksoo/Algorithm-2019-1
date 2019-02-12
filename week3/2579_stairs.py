# 1. 계단 갯수를 받는다
# 2. 계단 점수를 받는다
# 3. 첫번째 계단에 올랐을 때 최대 점수를 계산하고 저장한다
# 4. 두번째 계단에 올랐을 때 최대 점수를 계산하고 저장한다
# 5. n번째 계단까지 올랐을 때 최대 점수를 차례차례 계산하고 저장한다
# 6. n번째 계딴까지 올랐을 때 최대 점수를 출력

N = int(input())
scores = [0] * (N + 1)
max_scores = [0] * (N + 1)

# 각 계단별 점수
for number in range(1, N + 1):
    scores[number] = int(input())

# 첫 번째 계단 점수 계산
max_scores[1] = scores[1]
max_scores[2] = scores[1] + scores[2]
max_scores[3] = max(max_scores[1], max_scores[0] + scores[2]) + scores[3]

# 모든 계단의 optimal sol 을 아래에서부터 하나씩 계산
for stair_number in range(4, N + 1):
    max_scores[stair_number] = max(max_scores[stair_number - 2], max_scores[stair_number - 3] + scores[stair_number - 1]) + scores[stair_number]

print(max_scores[N])