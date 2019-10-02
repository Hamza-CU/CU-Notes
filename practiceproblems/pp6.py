#Problem 1 (Simple Calculator - *)

print("""Hello, I am a simple calculator.
What operation would you like to perform?
Type: A for addition
      S for subtraction
      M for multiplication
      D for division""")

oper = str(input())
num1 = int(input(print("What is operand 1?")))
num2 = int(input(print("What is operand 2?")))

add = str("A")
sub = str("B")
mul = str("C")
div = str("D")

if add == oper:
    Aans = num1 + num2
    print(num1, "+" , num2 , "=" , Aans)
elif sub == oper:
    Bans = num1 - num2
    print(num1, "-", num2, "=", Bans)
elif mul == oper:
    Cans = num1 * num2
    print(num1, "*" , num2 , "=" , Cans)
elif div == oper:
    Dans = num1/num2
    DansR = num1 % num2
    print(num1, "/", num2, "=", Dans, "remainder", DansR)
else:
    print("Invalid Entry")
