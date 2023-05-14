"""
가장 뛰어난 논리오류 탐색 방법: '디버깅'

 1. 변수 초기화 오류
 2. 인덱스 오류
 3.변수 사용 오류

 
배열과 리스트


파이썬에서 형 변환

bool형 변환의 경우 int, float에서 변환시 데이터가 0인지아닌지(0 => false), chr와 str에서 변환시에는 값이 비어있는지 아닌지에따라(비어있어면 => flase) true, false로 변환


합배열
만드는 공식 : S[i] = S[i-1] A[i]

    구간 합을 구하는 공식
    S[j] - S[i-1] : i에서 j까지 구간의 합

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

#백준 11660

