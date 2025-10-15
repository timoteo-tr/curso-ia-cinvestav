print("Evalúa la función f(n)")
n = float(input("Ingresa el valor de \"n\":"))

if n <= -1:
     fn = 1/n
elif n<=10:
    fn = n
else:
    fn = n**2

print("f(",n,")=",fn)

