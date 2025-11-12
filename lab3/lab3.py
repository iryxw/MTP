from abc import ABC, abstractmethod
from math import sqrt

class figure(ABC):
  @abstractmethod
  def perimetr(self):
    pass

  @abstractmethod
  def square(self):
    pass

class square(figure):
  
  def __init__(self, widht, height):
    self.width = widht
    self.height = height
  
  def perimetr(self) -> float:
    return 4 * self.width
  
  def square(self) -> float:
    return self.width * self.height
  
  @staticmethod
  def help() -> str:
    message = "Это класс 'Квадрат'. " \
    "В этом классе определены методы 'периметр' и 'площадь'."
    return message
  
  
class triangle(figure):
  
  def __init__(self, a, b, c) -> None:
    self.a = a
    self.b = b
    self.c = c
  
  def perimetr(self) -> float:
    return self.a + self.b + self.c
  
  def square(self) -> float:
    half_perimetr = self.perimetr() / 2
    aa = half_perimetr - self.a
    bb = half_perimetr - self.b
    cc = half_perimetr - self.c
    return sqrt(half_perimetr * aa * bb * cc)
  
class MyNumbers:
  def __init__(self):
    self.a = 1

  def __iter__(self):
    return self

  def __next__(self):
    x = self.a
    self.a += 2
    if x <= 15:
      return x
    else:
      raise StopIteration

print(square.help())
mySquare = square(2, 2)
print(mySquare.help())
