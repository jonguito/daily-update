

class tarefas:
    def __init__ (self, estudo, academia, cardio):
        self.estudo = estudo
        self.academia = academia
        self.cardio = cardio

    def __repr__(self):
        return f'tarefas(estudo = {self.estudo}, academia = {self.academia}, cardio = {self.cardio})'

check = tarefas(estudo = False,academia = False,cardio = False)


def pergunta_treino():
    
    while True:
        pergunta = input('treinou hoje? digite S para sim e N para não.-->  ').upper()

        if pergunta != 'S' and pergunta != 'N':                
            print('Digite somente S para sim e N para não,nada além disso. ')


        elif pergunta == 'S' :

            print('¨¨'*40)
            print('boa mlk,gostei de ver.')
            print('¨¨'*40)

            dia_semana = input('em qual dia da semana você ta rodando esse código?--> ').upper()

            if dia_semana == 'DOMINGO' or dia_semana == 'SABADO' or dia_semana == 'SÁBADO':
                print('Hoje NÃO é dia de treino,mas vamo considerar .')

                check.academia = True
            else:

                print('Nice mano! seguindo o plano certinho!')
                check.academia = True  

                print(check)            
            break
        

        elif pergunta == 'N':
            print('complicado ein chefe.')
            dia_semana = input('em qual dia da semana você ta rodando esse código?').upper()

            if dia_semana in ('DOMINGO', 'SABADO', 'SÁBADO'):
                print('sem problemas meu parceiro! hoje NÃO é dia de treino.')
                print(check)
                

            elif dia_semana in ('SEGUNDA','TERÇA','QUARTA','QUINTA','SEXTA'):
                print('Deu mole chefe.tenta dnv amanhã.')
                print(check)
                 
            break                    
                       
        
def pergunta_estudo():
    while True:
        pergunta = input('Você estudou hoje? digite S para sim e N para não.-->   ').upper()
        if pergunta == 'S':

            print('¨¨'*40)
            print('Boa mano! CONTINUA ASSIM!!')
            print('¨¨'*40)

            check.estudo = True
            print(check)

        else:
            print('complicado chefe! amanhã é outro dia.')
            print(check)
        break


def pergunta_cardio():
    while True:
        pergunta = input('Você fez cardio hoje?').upper()
        if pergunta == 'S':
            try:
                tipo_cardio = int(input('''Qual tipo de Cardio você fez?
                1 = corrida
                2 = pedal
                3 = algum esporte específico(basquete,futebol...etc) --> '''))


                print('¨¨'*40)
                print('Boa mano! CONTINUA ASSIM!!')
                print('¨¨'*40)

                check.cardio = True
                print(check)
                break

            except ValueError:
                print('Digite somente o número correspondente ao tipo de cardio que você fez.')
        else:
            print('Tranquilo! amanhã é outro dia. ')
            break

print('¨¨'*40)
print('BORA AVALIAR SEU PROGRESSO DIÁRIO')
print('¨¨'*40)

pergunta_treino()
pergunta_estudo()
pergunta_cardio()


      




