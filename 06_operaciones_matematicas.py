"""
https://platzi.com/clases/4204-pensamiento-logico-desafios/56218-playgrounds-operacion-matematica/

Basado en la solución del desafio anterios para llegar a la solución crea una función que reciba dos números y llegue al resultado esperado.

Solución del desafio anterior

(5-4)  = 1   :   (5+4)  = 9  →  19
(8-2)  = 6   :   (8+2)  = 10 →  610
(10-8) = 2   :   (10+8) = 18 →  218
(12-9) = 3   :   (12+9) = 21 →  321
(18-2) = 16  :   (18+2) = 20 →  1620
(21-5) = 16  :   (21+5) = 26 →  1626

Input:

solution(5, 4)
solution(21, 5)

Output:

19
1626
"""


suma = lambda num1, num2: num1 + num2

resta = lambda num1, num2: num1 - num2

num1 = int(input("dame el primer numero: "))
num2 = int(input("dame el segundo numero: "))

print(f'{resta(num1,num2)}{suma(num1,num2)}')