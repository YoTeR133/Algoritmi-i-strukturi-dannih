# Отчёт
  - Стек 
  - Очередь 
  - Приоритетная очередь 
---
# Работа программы
1. Стек 

Работа программы:
```
stack = Stack(3)
stack.push('А') 
stack.push('Б')  
stack.push('В')  
```
Результат:

![image](https://github.com/user-attachments/assets/6f81861c-e2fe-449e-98d1-f1c6ef7966ae)

Обработка ошибок:
```
    stack = Stack(2)
    stack.push('А')
    stack.push('Б')
    stack.push('В')
```
Результат:
При попытке добавить больше элементов, чем позволяет размер стека, вызывается ошибка OverflowError.

![image](https://github.com/user-attachments/assets/00695085-0015-4050-b179-6175f278332a)

---
2. Очередь
Работа программы:
```
    queue = Queue(5)
    queue.insert(10)
    queue.insert(20)
    queue.insert(30)
```
Результат:

![image](https://github.com/user-attachments/assets/5e0b3a8a-03da-498d-b2e6-5b085e94a4df)

Обработка ошибок:
```
queue = Queue(3)
queue.remove()  
```
Результат:
При попытке извлечь элемент из пустой очереди возникает ошибка

![image](https://github.com/user-attachments/assets/804a3aba-9e26-4a0a-acd3-17eda91deeff)

---
3. Приоритетная очередь
   
Работа программы:
```
    pq = PriorityQueue(5)
    pq.insert(30)
    pq.insert(10)
    pq.insert(20)
```
Результат:

![image](https://github.com/user-attachments/assets/9b0f4c12-b2bb-47d8-b0f2-db393822d029)

Обработка ошибок:
```
    pq = PriorityQueue(2)
    pq.insert(30)
    pq.insert(10)
    pq.insert(20)
```
Результат:
При попытке добавить больше элементов, чем позволяет размер приоритетной очереди, возникает ошибка

![image](https://github.com/user-attachments/assets/0c578efc-c804-4528-ac84-6e50bc8f4453)

# Проверка на палиндром
Работа программы:
```
    test_string = "12321"
    print(f"Является ли '{test_string}' палиндромом? {is_palindrome(test_string)}")
    test_string = "яблоко"
    print(f"Является ли '{test_string}' палиндромом? {is_palindrome(test_string)}\n")
```
Результат:

![image](https://github.com/user-attachments/assets/fe3acfcc-117e-4876-a87e-40737d7bfe6f)
