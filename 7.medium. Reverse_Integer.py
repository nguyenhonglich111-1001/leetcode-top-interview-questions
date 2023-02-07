def reverse(x: int) -> int:

    coeff = 1
    if x < 0:
        coeff = -1
        x *= -1
    ans = 0

    while x:
        ans = ans*10 + x % 10
        x //= 10

    if -2**31 >= coeff*ans or coeff*ans >= 2**31 -1:
        return 0
    return coeff*ans


if __name__ == '__main__':
    print(reverse(-120))