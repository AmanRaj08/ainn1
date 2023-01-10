import math

MAX = 1000
MIN = -1000


def alphabeta(depth,idx,maximize,vals,alpha,beta):

    if depth == int(math.log(len(vals), 2)):
        return values[idx]
    if maximize:
        best = MIN
        for i in range (0,2):
            val = alphabeta(depth+1, idx*2+i, False, vals, alpha, beta)
            best = max(val,best)
            if best < beta:
                alpha = max(best,alpha)
        return best
    else:
        best = MAX
        for i in range(0, 2):
            val = alphabeta(depth + 1, idx * 2 + i, True, vals, alpha, beta)
            best = min(val, best)
            if best > alpha:
                beta = min(best, beta)
        return best


if __name__ == "__main__":
    values = [2,3,5,9,0,1,7,5]
    print(f"Result = {alphabeta(0, 0, True, values, MIN, MAX)}")
