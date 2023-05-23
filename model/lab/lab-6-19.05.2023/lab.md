# Лабораторна робота №6

## Тема

Моделювання релейного регулятора мовою FBD

## Мета

Знайомство з принципами програмування релейних елементів на мові функціональних блоків FBD.

## Завдання

![task](assets/task.png)

## Виконання

Значення виходу поза інтервалом \[-4; 4\] можна чітко визначити. На інтервалі \[-4; 4\] вихід ДРЛ визначається попереднім станом ДРЛ, тобто за допомогою похідної за часом від вхідного сигналу.
Таким чином, поведінку ДРЛ можна записати у вигляді правил та функцій наступним чином:

![graph](assets/graph.png)

### Написання програми

Я використав пилкоподібний графік для x, який набуває всіх можливих значень для функції та повертається назад

![main](assets/main.png)

Та сам код та з'єднання для реалізації функції

![vars](assets/vars.png)

![1](assets/1.png)  
![2](assets/2.png)  
![3](assets/3.png)  
![4](assets/4.png)  
![5](assets/5.png)  
![6](assets/6.png)  
![7](assets/7.png)  
![8](assets/8.png)  
![91011](assets/91011.png)  

### Отриманий графік

![mygraph](assets/mygraph.png)

Ось так виглядає графіки отримані при виконанні програми. Як видно, всі частини графіка співпадають з наведеними в завданні, та коли в нас додатня похідна, ми отримаємо нижню частину, а коли рухаємося назад, отримаємо верхню

## Висновок

На цій лабораторній роботі я розробив релейні елементи за допомогою функціональних блоків FBD.