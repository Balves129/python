# Armazenei os dias da semana em uma biblioteca
votos_da_semana ={
    "Segunda": 0,
    "Terca": 0,
    "Quarta": 0,
    "Quinta": 0,
    "Sexta": 0
}
# função para registrar um voto em determinado dia
def num_votos(dia_da_semana):
    
    if dia_da_semana in votos_da_semana: #Aqui, se a variável dia_da_semana estiver dentro de votos_da_semana,
                                         #ela executa a próxima linha
        
        votos_da_semana[dia_da_semana] +=1 #Aqui, incrementa 1 no dia votado. dia_da_semana é a variável criada para puxar os dias
        
        print(f"Você votou no dia {dia_da_semana}! ")
    else:
        print("Dia inválido, selecione de acordo com as opções!")
        
# Aqui vamos encontrar o dia mais votado
def dia_mais_votado():
    dia_mais_votado = max(votos_da_semana, key=votos_da_semana.get)
    return dia_mais_votado

# Sistema de escolha de opçoes para votação
while True:
    print("\nEscolha um dia para votar ou digite 'sair' para encerrar:")
    print("1. Segunda-feira")
    print("2. Terça-feira")
    print("3. Quarta-feira")
    print("4. Quinta-feira")
    print("5. Sexta-feira")
    
    escolha = input("Opção: ")
    
    # Um if para encerrar o programa quando o periodo de votação terminar
    if escolha == "sair":
        break


    if escolha.isdigit(): #isdigit verifica se nossa string "escolha" possui apenas digitos numéricos
        try:
            num_dia = int(escolha) 
            if 1<= num_dia <=5:
                dias = list(votos_da_semana.keys())
                dia_escolhido = dias[num_dia -1]
                num_votos(dia_escolhido)
            else:
                print("Opção inválida, escolha de 1 a 5!")
        except ValueError:
            print("Opcção inválida! Escolha de 1 a 5!")
    else:
        print("Opcção inválida! Por favor escolha de 1 a 5 ou digite 'sair'.")
            

        
print("Apuração de votos")
for dia_da_semana, votos in votos_da_semana.items():
    print(f"{dia_da_semana}: {votos} votos ")
    
    dia_ganhador= dia_mais_votado()
    


 
