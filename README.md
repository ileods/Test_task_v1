# Тестовое задание (версия 1)

Задание: написать калькулятор.

### [Ссылка на repl.it](https://replit.com/@DaryaIsachenko/Test)

Представленная версия разработана в ООП стиле. Благодаря этому код получился гибким. Можно спокойно добавлять новые операции, притом не только бинарные, но и унарные (например, факториал), либо какие-то пользовательские (например, округление).

Класс Calculator содержит в себе массив операций, унаследованных от абстрактного класса MathOperation. Это позволяет конфигурировать калькулятор. Может пригодиться и для обратной совместимости или разграничения набора функций. Например: 
```python
simple_calc = Calculator([
  OperationSum(4),
  OperationDiv(1),
  OperationMul(2),
  OperationSub(3)
])

premium_calc = Calculator([
  OperationSum(4),
  OperationDiv(1),
  OperationMul(2),
  OperationSub(3),
  OperationFactorial(0)
])

...

if user.premium:
  return premium_calc.calculate(str)
else:
  return simple_calc.calculate(str)
```
## Как работает калькулятор
В начале выражение разбивается на массив из чисел и символов операций:
```
"3+54*2" -> [3,"+", 54, "*", 2]
```
После этого формируется массив операций по приоритетности. Приоритетность указывается при конфигурировании объекта калькулятора.
```
simple_calc = Calculator([
  OperationSum(4),
  OperationDiv(1),             ->      priority = [OperationDiv, IperationMul, OperationSub, OperationSum]
  OperationMul(2),
  OperationSub(3)
])
```
Затем калькулятор ищет первый символ в массиве, совпадающий с обозначением операции. Обозначение операции задаётся при реализации класса MathOperation
```
--------------
             |
             v
[3,"+", 54, "*", 2]
```
И вызвает метод do_operation найденной операции, передавая как аргументы значения, индексы которых указаны в полe argument_index при реализации MathOperation
```
class OperationMul(MathOperation):
  def __init__(self, priority):
    super().__init__(priority, [-1,1], "*")
                                 | |
...                              | |
------------------|              | |
                  |              | |
              |---+------------- / |
              v   v                |
     [3,"+", 54, "*", 2] <---------+

OperationMult.do_operation([54,2])
```
После чего заменяет знак и аргументы операции на результат операции
```
[3,"+", 54, "*", 2] -> [3,"+", 108]
```
После нескольких итераций в массиве остаётся одно число - итоговый ответ
```
[111]
```

