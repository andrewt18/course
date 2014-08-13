# Очень примитивная реализация
class Number:
  def __init__(self, num_system, registers):
    self.registers = []
    self.num_system = num_system
    for x in registers:
      if x > (num_system - 1): raise ValueError("Register value more than {}".format(num_system - 1))
      self.registers.append(x)

  def __sub__(self, other):
    if self.num_system != other.num_system:
      raise ValueError("The digits have different numeral system")
    negative = False
    result = []
    for x, y in zip(self.registers, other.registers):
      r = x - y
      if negative:
        r -= 1
        negative = False
      if r < 0:
        r += self.num_system
        negative = True
      result.append(r)
    if negative: 
      result.append(0)
      help_var = []
      for e in range(len(result)):
        if e == (len(result)-1):
          help_var.append(1)
        else:
          help_var.append(0)
      new_result = Number(self.num_system, help_var) - Number(self.num_system, result)
      count = 0
      for a in range(len(new_result.registers)):
        if count > 0:   #Если только первое число справа, являющееся не нолем должно быть негативным. Если негативными должны быть все, можно убрать эту переменную.
          break
        if new_result.registers[a] != 0:
          new_result.registers[a] = -new_result.registers[a]
          count += 1 
      result = new_result.registers
    return Number(self.num_system, result)


x = Number(10, (0, 2))
y = Number(10, (1, 1))
z = x - y
print(z.registers)
