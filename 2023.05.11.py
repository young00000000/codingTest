"""
가장 뛰어난 논리오류 탐색 방법: '디버깅'

 1. 변수 초기화 오류
 2. 인덱스 오류
 3.변수 사용 오류

 
배열과 리스트


"""

# 백준 11720

# n값 받기
n= input()

# numbers 변수에 list 함수를 이용하여 숫자를 한 자리씩 나누어 받기
numbers = list(input())

# sum 변수 선언 
sum= 0

#for numbers 탐색: 
for i in numbers:
    sum = sum+int(i)

#sum 출력
print(sum)