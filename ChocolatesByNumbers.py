def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def solution(N, M):
    # n 과 m의 공통 배수 => 최소공배수
    # 최소 공배수를 M으로 나눈 값

    # N * M // gcd(N, M)
    # gcd() 최대 공약수

    result = (N * M) // gcd(N, M)

    return result // M