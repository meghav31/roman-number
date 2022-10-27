#funtion to convert number to roman
def solve(num):
   res = ""
   table = [
      (1000, "M"),
      (900, "CM"),
      (500, "D"),
      (400, "CD"),
      (100, "C"),
      (90, "XC"),
      (50, "L"),
      (40, "XL"),
      (10, "X"),
      (9, "IX"),
      (5, "V"),
      (4, "IV"),
      (1, "I"),
   ]

   for cap, roman in table:
      d, m = divmod(num, cap)
      res += roman * d
      num = m

   return res


# for roman to number
def RL(x):
    if (x == 'I'):
        return 1
    if (x == 'V'):
        return 5
    if (x == 'X'):
        return 10
    if (x == 'L'):
        return 50
    if (x == 'C'):
        return 100
    if (x == 'D'):
        return 500
    if (x == 'M'):
        return 1000
    return -1
def RomtoInt(str):
    a = 0
    i = 0
    while (i < len(str)):
        x1 = RL(str[i])
        if (i + 1 < len(str)):
            x2 = RL(str[i + 1])
            if (x1 >= x2):
                a = a + x1
                i = i + 1
            else:
                a = a + x2 - x1
                i = i + 2
        else:
            a = a + x1
            i = i + 1
    return a
    
num = int(input("Enter the number to convert in roman number"))
print("Roman number is")
print(solve(num))


num2 = input("Enter the roman number to convert in  number")
print("Enterd number is")
print(py_solution().roman_to_int(num2))  
