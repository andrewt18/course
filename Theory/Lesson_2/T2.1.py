# Очень примитивная реализация
class Number:
  def __init__(self, num_system, registers):
    self.registers = []
    self.num_system = num_system
    for x in registers:
      if x > (num_system - 1): raise ValueError("Register value more than {}".format(num_system - 1))
      self.registers.append(x)

  def __add__(self, other):
    if self.num_system == other.num_system:
      overflow = False
      result = []
      for x, y in zip(self.registers, other.registers):
        r = x + y
        if overflow:
          r += 1
          overflow = False
        if r > (self.num_system - 1):
          r -= self.num_system
          overflow = True
        result.append(r)
      if overflow: result.append(1)
      return Number(self.num_system, result)
    else: 
      raise ValueError("The digits have different numeral system")


x = Number(10, (8, 9))
y = Number(10, (3, 3))
z = x + y
print(z.registers)
