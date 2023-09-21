#Importando math para calcular a raiz
import math

# Pedindo as informações das variáveis
a = int(input("informe o valor de A: "))
b = int(input("informe o valor de B: "))
c = int(input("informe o valor de C: "))

# fazendo o valor de delta
delta = b * b -4 * a * c

#fazendo a verificação
if delta > 0.0:
#calculando as raizes de delta para valores positivos
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2* a)
    print(f"Para {a}x² + {b}x + {c} obtivemos os valores de: x1: {x1} e x2: {x2}")

elif delta == 0:
#calculando as raizes de delta se for negativo    
    x = (-b + math.sqrt(delta)) / (2 * a)
    print(f"Para {a}x² + {b}x + {c} obtivemos os valores de: x: {x}")
    
else:
    print(f"Para {a}x² + {b}x + {c} não exitem valores para x")
    