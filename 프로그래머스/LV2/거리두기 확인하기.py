def solution(places):
    answer = []

    for place in places:
        result = 1
        for i in range(5):
            if result == 0:
                break
            for j in range(5):
                if result == 0:
                    break
                if place[i][j] == 'P':
                    if i+1 < 5:
                        if place[i+1][j] == 'P':
                            result = 0
                            break
                        if place[i+1][j] == 'O':
                            if i+2 < 5:
                                if place[i+2][j] == 'P':
                                    result = 0
                                    break
                    if j+1 < 5:
                        if place[i][j+1] == 'P':
                            result = 0
                            break
                        if place[i][j+1] == 'O':
                            if j+2 < 5:
                                if place[i][j+2] == 'P':
                                    result = 0
                                    break
                    if i+1 < 5 and j+1 < 5:
                        if place[i+1][j+1] == 'P' and (place[i+1][j] == 'O' or place[i][j+1] == 'O'):
                            result = 0
                            break
                    if i+1 < 5 and j-1 >= 0:
                        if place[i+1][j-1] == 'P' and (place[i+1][j] == 'O' or place[i][j-1] == 'O'):
                            result = 0
                            break
        answer.append(result)
    return answer