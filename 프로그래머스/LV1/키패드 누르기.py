def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 11
    
    for number in numbers:
        if number%3 == 2:
            if left%3 == 1:
                left_dis = 3
                left_p = left + 1
            else:
                left_dis = 0
                left_p = left
            if right%3 == 0:
                right_dis = 3
                right_p = right - 1
            else:
                right_dis = 0
                right_p = right
            if (abs(left_p - number)+left_dis) < (abs(right_p - number)+right_dis):
                left = number
                answer = answer + 'L'
            elif (abs(left_p - number)+left_dis) > (abs(right_p - number)+right_dis):
                right = number
                answer = answer + 'R'
            else:
                if hand == 'left':
                    left = number
                    answer = answer + 'L'
                else:
                    right = number
                    answer = answer + 'R'
        elif number%3 == 1:
            left = number
            answer = answer + 'L'
        else:
            right = number
            answer = answer + 'R'
    return answer