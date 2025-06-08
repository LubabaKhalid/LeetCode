def fun(n):
    if n == 1:
        print('One', end=' ')
    elif n == 2:
        print('Two', end=' ')
    elif n == 3:
        print('Three', end=' ')
    elif n == 4:
        print('Four', end=' ')
    elif n == 5:
        print('Five', end=' ')
    elif n == 6:
        print('Six', end=' ')
    elif n == 7:
        print('Seven', end=' ')
    elif n == 8:
        print('Eight', end=' ')
    elif n == 9:
        print('Nine', end=' ')

def fun2(n):
    if n == 10:
        print('Ten', end=' ')
    elif n == 11:
        print("Eleven", end=' ')
    elif n == 12:
        print("Twelve", end=' ')
    elif n == 13:
        print("Thirteen", end=' ')
    elif n == 14:
        print("Fourteen", end=' ')
    elif n == 15:
        print("Fifteen", end=' ')
    elif n == 16:
        print("Sixteen", end=' ')
    elif n == 17:
        print("Seventeen", end=' ')
    elif n == 18:
        print("Eighteen", end=' ')
    elif n == 19:
        print("Nineteen", end=' ')
    elif n == 20:
        print("Twenty", end=' ')
    elif n == 30:
        print("Thirty", end=' ')
    elif n == 40:
        print("Forty", end=' ')
    elif n == 50:
        print("Fifty", end=' ')
    elif n == 60:
        print("Sixty", end=' ')
    elif n == 70:
        print("Seventy", end=' ')
    elif n == 80:
        print("Eighty", end=' ')
    elif n == 90:
        print("Ninety", end=' ')

def print_two_digits(n):
    if 10 <= n <= 19:
        fun2(n)
    else:
        tens = (n // 10) * 10
        units = n % 10
        if tens:
            fun2(tens)
        if units:
            fun(units)

n = 123456
if n == 0:
    print("Zero")

if n >= 100000000:
    hundreds_of_millions = n // 100000000
    fun(hundreds_of_millions)
    print("Hundred Million", end=' ')
    n = n % 100000000

if n >= 1000000:
    millions = n // 1000000
    print_two_digits(millions)
    print("Million", end=' ')
    n = n % 1000000

if n >= 1000:
    thousands = n // 1000
    print_two_digits(thousands)
    print("Thousand", end=' ')
    n = n % 1000

if n >= 100:
    hundreds = n // 100
    fun(hundreds)
    print("Hundred", end=' ')
    n = n % 100

if n > 0:
    print_two_digits(n)
