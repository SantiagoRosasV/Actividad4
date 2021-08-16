import math
def main():
     #escribe tu código abajo de esta línea
   pass
import math
a=float(input('Dame valor a:'))
b=float(input('Dame valor b:'))
c=float(input('Dame valor c:'))
s=((a+b+c)/2)
d=str(s*(s-a)*(s-b)*(s-c))
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print('Area:' ,area)


if __name__ == '__main__':
    main()
