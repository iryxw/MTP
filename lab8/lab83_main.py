from src.lab83 import Person

def main() -> None:
  p = Person("Анастасия", "Иванова", 25)

  print(f"Полное имя: {p.full_name}") 
  print(f"Возраст: {p.age}") 

  p.age = 26
  print(f"Новый возраст: {p.age}")

  # p.age = -5   
  # ValueError("Возраст не может быть отрицательным")

  # p.full_name = "Новое имя" 
  # AttributeError (только для чтения)


if __name__ == "__main__":
  main()