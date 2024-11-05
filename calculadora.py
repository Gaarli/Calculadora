# Esse programa é uma calculadora implementada em python
# Ele solicita uma operação e em seguida 2 números
# Depois disso, é mostrado na tela o resultado da operação escolhida aplicada
# aos dois números

# As operacoes foram modularizadas para melhor organizacao do codigo
# As operacoes suportadas sao soma, subtracao, multiplicacao e divisao
# E se encontram implementadas no modulo operacoes
import operacoes

# A função principal coordena o output na tela
# E também solicita a operação e os números
# No final mostra o resultado
# E pergunta se o usuário quer fazer outra operação
def main():
    # Leitura para inicializar a calculadora
    comando = int(input('Calcular? 1 - SIM & 2 - NAO'))

    # Inicia o loop de cálculos até que o usuário deseje parar
    while(comando==1):
        # Mostra as operações possíveis
        print('As operações são: ')
        print('1 - soma')
        print('2 - subtracao')
        print('3 - multiplicacao')
        print('4 - divisao')

        # Le a operacao
        operacao = int(input('Digite a operacao'))

        # Le os numeros para o calculo
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
        
        # Analise da operacao
        if operacao==1:
            print('A soma de {} e {} é {}'.format(n1,n2,operacoes.soma(n1,n2)))
        elif operacao==2:
            print('A subtracao de {} de {} é {}'.format(n2,n1,operacoes.subtracao(n1,n2)))
        elif operacao==3:
            print('A multiplicacao de {} por {} é {}'.format(n1,n2,operacoes.mult(n1,n2)))
        else:
            print('A divisao de {} por {} é {}'.format(n1,n2,operacoes.div(n1,n2)))

        # Verifica se o usuario deseja fazer um novo calculo
        comando = int(input('Voce deseja calcular novamente? 1 - SIM & 2 - NAO'))

# Chama a funcao principal
main()