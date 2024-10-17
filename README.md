Чуменко Игорь ПИНб-21


## Задача 1 `Неглухой телефон`  [ссылка на задачу](https://acmp.ru/index.asp?main=task&id_task=108&ins=1#solution).
```
N = int(input())
print(N)
```

## Задача 2 `A+B` [ссылка на задачу](https://acmp.ru/index.asp?main=task&id_task=1)
```
a,b = map(int, input().split())
result = a + b
print(result)
```

## Задача 3 `Больше-меньше` [ссылка на задачу](https://acmp.ru/index.asp?main=task&id_task=25&ins=1#solution)
```
A = int(input())
B = int(input())
if A < B:
    print("<")
elif A > B:
    print(">")
else:
    print("=")
```
## Задача 4 `Орешки` [ссылка на задачу](https://acmp.ru/index.asp?main=task&id_task=766)
```
N,M,K = map(int, input().split())
if N * M >= K:
    print("YES")
else:
    print("NO")
```
## Задача 5 `Зарплата` [ссылка на задачу](https://acmp.ru/index.asp?main=task&id_task=21)
```
A,B,C = map(int, input().split())
MinZ = min(A,B,C)
MaxZ = max(A,B,C)
result = MaxZ - MinZ
print(result)
```
## Задача 6 `Сбор земляники` [ссылка на задачу](https://acmp.ru/index.asp?main=task&id_task=755)
```
X,Y,Z = map(int, input().split())
result = X + Y - Z
if result >= 0:
    print(result)
else:
    print("Impossible")
```
## Задача 7 `Время года` [ссылка на задачу](https://acmp.ru/index.asp?main=task&id_task=892&ins=1#solution)
```
A = int(input())
if A in (1,2,12):
    print("Winter")
elif A in(3,4,5):
    print("Spring")
elif A in (6,7,8):
    print("Summer")
elif A in (9,10,11):
    print("Autumn")
else:
    print("Error")
```
## Задача 8 `Три толстяка` [ссылка на задачу](https://acmp.ru/index.asp?main=task&id_task=754)
```
A,B,C = map(int, input().split())
if A > 727 or A < 94 or B > 727 or B < 94 or C > 727 or C < 94:
    print("Error")
else:
    print(max(A,B,C))
```
## Задача 9 `Кондиционер` [ссылка на задачу](https://acmp.ru/index.asp?main=task&id_task=854)
```
A,B = map(int, input().split())
C = input()
if C == "heat":
    print(max(A,B))
elif C == "freeze":
    print(min(A,B))
elif C == "auto":
    print(B)
elif C == "fan":
    print(A)
else:
    print("error")
```
