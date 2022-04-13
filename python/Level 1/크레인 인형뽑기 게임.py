def solution(board, moves):
    answer = 0
    basket = []
    
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] > 0:
                basket.append(board[i][m-1])
                board[i][m-1] = 0
                break
        if len(basket) > 1 and basket[-2] == basket[-1]:
            answer += 2
            basket = basket[:-2] # pop(-1) 2번
        
    return answer