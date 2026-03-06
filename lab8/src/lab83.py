class Person:
  def __init__(self, first_name: str, last_name: str, age: int):
    self.first_name = first_name
    self.last_name = last_name
    self._age = age

  @property
  def age(self) -> int:
    return self._age

  @age.setter
  def age(self, value: int):
    if value < 0:
      raise ValueError("Возраст не может быть отрицательным")
    self._age = value

  @property
  def full_name(self) -> str:
    return f"{self.first_name} {self.last_name}"


if __name__ == "__main__":
  pass