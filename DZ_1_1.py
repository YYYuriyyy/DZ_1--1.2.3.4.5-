n1 = input("Введіть число: ")
n2 = input("Введіть число: ")
n3 = input("Введіть число: ")
sum_nambers = n1 + n2 + n3

print(sum_nambers)



input("Введіть число:")
a = 1
b = 2
c = 3
d = 4

print(a,"*",b,"*",c,"*",d,"=", a*b*c*d)



m=int(input("Довжина в метрах: "))

print(f"={m}м, ={100*m}cm, ={10*m}дм, ={1000*m}мм, ={0.0006213*m}милі")



p = float(input("Основа трикутника А: "))
p1 = float(input("Висота трикутника Б: "))

sumNamber = (p*p1)/2
print("Площа трикутника: ",(sumNamber),'см2')



n = input("Введіть число: ")[::-1]

print(n)