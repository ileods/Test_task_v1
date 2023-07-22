from abc import ABC, abstractmethod

class MathOperation(ABC):
  #                      1          [-1, 1]         "*"    
  def __init__(self, priority, argument_position, symbol):
    self.priority = priority
    self.argument_position = argument_position
    self.symbol = symbol

  @abstractmethod
  def do_operation(self, args):
    pass

class OperationSum(MathOperation):
  def __init__(self, priority):
    super().__init__(priority, [-1,1], "+")
  def do_operation(self, args):
    return args[0] + args[1]

class OperationMul(MathOperation):
  def __init__(self, priority):
    super().__init__(priority, [-1,1], "*")
  def do_operation(self, args):
    return args[0] * args[1]

class OperationDiv(MathOperation):
  def __init__(self, priority):
    super().__init__(priority, [-1,1], "/")
  def do_operation(self, args):
    return args[0] / args[1]

class OperationSub(MathOperation):
  def __init__(self, priority):
    super().__init__(priority, [-1,1], "-")
  def do_operation(self, args):
    if args[0] == None:
      args[0] = 0
    return args[0] - args[1]

#Пример унарной операции
class OperationFactorial(MathOperation):
  def __init__(self, priority):
    super().__init__(priority, [-1], "!")
  def do_operation(self, args):
    res = 1
    for i in range(1,int(args[0])+1):
      res *= i
    return res

class Calculator:
  def __init__(self, operations):
    self.operations = operations

  def __string_expression_to_array(self, str_expression):
    # "1+54*2" -> [1,"+", 54, "*", 2]
    expression = []
    
    number = "";
    for s in str_expression:
      try:
        float(s)
        number += s
      except ValueError:
        if number != "":
          expression.append(float(number))
          number = ""
        expression.append(s)
    if number != "":
      expression.append(float(number))

    return expression

  def __round_answer(self, float_answer):
    if float_answer % 1 == 0:
      return int(float_answer)
    return float_answer
  
  def calculate(self, str_expression):

    expression = self.__string_expression_to_array(str_expression)
    
    # operations = [OperationSum, OperationMult] -> priority = [OperationMult, OperationSum]
    priority = sorted(self.operations, key=lambda operation: operation.priority)

    for operation in priority:
      i = 0
      while (i < len(expression)):
        if expression[i] == operation.symbol:
          index_to_delete = []
          args = []
          
          for arg_index in operation.argument_position:
            index = i + arg_index
            if (index >= len(expression)) or (index < 0):
              args.append(None)
              continue
            else:
              args.append(expression[index])
              index_to_delete.append(index)
              
          res = operation.do_operation(args)
          expression[i] = res

          index_to_delete.sort(reverse = True)
          for index in index_to_delete:
            expression.pop(index)
          i = 0
        i += 1
    return(self.__round_answer(expression[0]))

calc = Calculator([
  OperationSum(4),
  OperationDiv(1),
  OperationMul(2),
  OperationSub(3),
  OperationFactorial(0)
])

while True:
  str_expression = str(input())
  print(str(calc.calculate(str_expression)) + "\n")