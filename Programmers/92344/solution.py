def solution(board, skill):
    answer = 0
    
    h,w = len(board),len(board[-1])
    sum_arr = [[0 for _ in range(w)] for _ in range(h)]
    result_arr = [[0 for _ in range(w)] for _ in range(h)]
    
    for type,r1,c1,r2,c2,degree in skill:
        if type == 1:
            degree *= -1
        sum_arr[r2][c2] += degree
        if c1 > 0: sum_arr[r2][c1-1] -= degree
        if r1 > 0: sum_arr[r1-1][c2] -= degree
        if c1 > 0 and r1 > 0: sum_arr[r1-1][c1-1] += degree

    for r in range(h-1,-1,-1):
        for c in range(w-1,-1,-1):
            result_arr[r][c] = sum_arr[r][c]
            if r < h-1: result_arr[r][c] += result_arr[r+1][c]
            if c < w-1: result_arr[r][c] += result_arr[r][c+1]
            if r < h-1 and c < w-1: result_arr[r][c] -= result_arr[r+1][c+1]
            if board[r][c] + result_arr[r][c] > 0:
                answer += 1

    return answer