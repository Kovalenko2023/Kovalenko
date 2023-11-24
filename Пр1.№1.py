a = float(input("Яка довжина відрізка a?"))
b = float(input("Яка довжина відрізка b?"))

t = a//b
f = a%b

    
if b <= a:
    print(t, f)

else:
    print("Відрізок b не поміщується у відрізок a")


