
# Zadanie 1
# int
a, b=1, 2
# float
c, d=1.1, 2.2
# complex
e, f=1+1j, 2+2j
# string
str1, str2="string1", "string2"

print(a, b, c, d, e, f, str1, str2)
del a, b, c, d, e, f, str1, str2

# Zadanie 2
a = 1
b = 2
dodawanie = a+b
odejmowanie = a-b
dzielenie = a/b
mnozenie = a*b
potegowanie = a**b
pierwiastkowanie = a**(1/b)
print(dodawanie, odejmowanie, dzielenie, mnozenie, potegowanie, pierwiastkowanie)
del a, b, dodawanie, odejmowanie, dzielenie, mnozenie, potegowanie, pierwiastkowanie

# Zadanie 3
a = 2
dodawanie, odejmowanie, dzielenie, mnozenie, potegowanie, reszta = 0, 0, 2, 2, 3, 3
dodawanie+=a
odejmowanie-=a
dzielenie /=a
mnozenie *=a
potegowanie **=a
reszta%=a
print(dodawanie, odejmowanie, dzielenie, mnozenie, potegowanie, reszta)
del a, dodawanie, odejmowanie, dzielenie, mnozenie, potegowanie, reszta


