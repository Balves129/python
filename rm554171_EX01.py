#função para definir plano
def calcular_bonus(faturamento_anual, plano):
    receber_bonus = {
        "Basic" : 30,
        "Silver": 20,
        "Gold": 10,
        "Platinum": 5
    }
    # Se planos estiverem dentro de receber bonus ele valida e calcula
    if plano in receber_bonus:
        porcentagem = receber_bonus[plano]
        
        #formula para calcular bonus
        bonus = faturamento_anual * porcentagem/100
        
        #Returna o resultado da função acima
        return bonus
    else:
        print("Plano inválido")
        
#Solicitar ao usuario os dados necessários
plano_cliente = input("Digite o tipo de plano(Basic; Silver; Gold; Platinum): ")
print("-------------------------------------")
valor_anual= float(input("Digite o faturamento deste ano: "))

#Faz a verificação do bonus recebido após o calculo
meu_bonus= calcular_bonus(valor_anual,plano_cliente)

#Nesse if, é necessário que seja diferente de um plano que não existe para 
#que funcione conforme queremos. Se for um plano invalido, a mensagem é mostrada com valor de none 
# e encerrado
if meu_bonus != "Plano inválido":
    print(f"Bonus do plano {plano_cliente} recebido. Valor total de {meu_bonus} reais.")
else:
    print("Plano invalido")
