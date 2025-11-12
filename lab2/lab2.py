def NOD(a: int, b: int) -> int:
  if (b == 0): 
    return a
  return NOD(b, a % b)

def calculate(a: float, b: float, c: str) -> float | str:
  match c:
    case "+":
      return a + b
    case "-":
      return a - b
    case "/":
      return a / b
    case "*":
      return a * b
    case "^":
      return a ** b
    case _:
      return "Я не знаю такую команду"

def squares(a: int) -> dict[int, int]:
  return {b : b*b for b in range(a)}

print("task 1")
print(NOD(6, 14))
print(NOD(2, 7))
print("\n\n")

print("task 2")
print(calculate(2.1, 2.9, '+'))
print(calculate(2.1, 2.9, '-'))
print(calculate(2.1, 2.9, '/'))
print(calculate(2.1, 2.9, '*'))
print(calculate(2.1, 2.9, '^'))
print(calculate(2.1, 2.9, '%'))
print("\n\n")

print("task 3")
print(squares(3))
print(squares(5))
print("\n\n")