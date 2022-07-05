def solution(phone_book):
    phone_book.sort()
    
    for i, num in enumerate(phone_book[:len(phone_book)-1]):
        if num == phone_book[i+1][:len(num)]:
            return False
    
    return True