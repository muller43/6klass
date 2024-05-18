def divisors(a):#делители числа (вывод - отсортированный список)
    d = set()
    for i in range(1,int(a**0.5)+1):
        if a%i==0:
            d.add(i)
            d.add(a//i)
            a //= i
    return sorted(d)
def multiple(a):#кратные числу а (от a до 1000)
    ans = []
    for i in range(a,1000+1):
        if i%a==0: ans += [i]
    return ans
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
def _gcd(a,b):#greatest common divisor, НОД 2-х чисел (через разложение на простые множители)
    a = prime_factorization(a); b = prime_factorization(b); ans = []; res = 1
    for i in a:
        if i not in ans:
            for j in b:
                if i==j and a.count(i)>ans.count(i):
                    ans += [i]
    for i in ans:
        res *= i
    return res
def lcm(a,b):#least common multiple наименьшее общее кратное
    a = prime_factorization(a); b = prime_factorization(b); res = 1
    ans = a
    for i in b:
        if i not in a or b.count(i)>a.count(i):
            ans += [i]
    for i in ans:
        res *= i
    return res
print(divisors(15))
print(multiple(8))
print(prime(17),prime(18))
print(prime_factorization(100))
print(_gcd(125,50))
print(lcm(60,75))

