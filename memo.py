def solution(phone_book):
    phone_book.sort()
    
    for i, num in enumerate(phone_book[:len(phone_book)-1]):
        if num == phone_book[i+1][:len(num)]:
            return False
    
    return True

phone_book = ["2", "112", "119","1120", "97674223", "1195524421"]
print(solution(phone_book))