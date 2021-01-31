print("*"*50)
print("-------------------FizzBuzz-------------------")
a=int(input("Bir sayi giriniz: "))
b=int(input("Bir sayi giriniz: "))
if a>b:
    print("ilk sayiyi küçük girdiniz.Tekrar deneyin.......")
while a<b:
    a +=1
    if a%15==0:
        print("FizzBuzz")
    elif a%5==0:
        print("Buzz")
    elif a%3==0:
        print("Fizz")
    else:
        print(a)