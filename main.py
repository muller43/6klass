def divisors(x):#делители числа (вывод - отсортированный список)
    d = set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
            x //= i
    return sorted(d)
def prime(x):#определение простоты числа (вывод True или False)
    return x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))
def prime_factorization(x):#разложение на простые множители
    divisor = 2; a = []
    while divisor**2<=x:
        if x%divisor==0:
            a += [divisor]
            x//=divisor
        else:
            divisor += 1
    if x>1: a += [x]
    return a 
def _gcd(a,b):#вывод НОД 2-х чисел (через разложение на простые множители - функцию div(x))
    a = prime_factorization(a); b = prime_factorization(b); ans = []; res = 1
    for i in a:
        if i not in ans:
            for j in b:
                if i==j and a.count(i)>ans.count(i):
                    ans += [i]
    for i in ans:
        res *= i
    return res
print(divisors(15))
print(prime(17),prime(18))
print(prime_factorization(100))
print(_gcd(125,50))

