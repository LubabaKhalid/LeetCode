import heapq

moveTime = [[0, 0, 0], [0, 0, 0]]  # You can change this for testing

n, m = len(moveTime), len(moveTime[0])
heap = [(0, 0, 0)]  # (time, row, col)
visited = [[float('inf')] * m for _ in range(n)]
visited[0][0] = 0

# 4 directions: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while heap:
    time, x, y = heapq.heappop(heap)

    if (x, y) == (n - 1, m - 1):
        print(time)
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            arrive = time + 1

            # Wait if cell isn't open yet
            if arrive < moveTime[nx][ny]:
                arrive = moveTime[nx][ny]

            # Apply the parity waiting rule only when room opens after t=0
            if moveTime[nx][ny] > 0 and (arrive - moveTime[nx][ny]) % 2 == 1:
                arrive += 1

            if arrive < visited[nx][ny]:
                visited[nx][ny] = arrive
                heapq.heappush(heap, (arrive, nx, ny))
