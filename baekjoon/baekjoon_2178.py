import sys
from collections import deque

input = sys.stdin.readline()

n, m = map(int, input().split())
maze = [list(map(int, input().readline())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < n and 0 <= next_y < m and maze[next_x][next_y] == 1:
                maze[next_x][next_y] = maze[x][y] + 1
                queue.append((next_x, next_y))

    return maze[n-1][m-1] # 인덱스가 (0, 0)부터 시작하니까 최종 출력값의 인덱스는 (n-1, m-1)

print(bfs(0, 0))