# Programa para Gerenciamento de Gastos Mensais
# A função deste programa é ajudar a monitorar seus gastos
# mensais, para que você saiba melhor onde está gastando seu dinheiro.

# Iniciando o programa
print("Bem-vindo ao Gerenciador de Gastos Mensais.")

# salvando as despesas mensais em um arquivo de texto externo
arquivoDeGastos = open("registro-de-gastos.txt", "a")

# função para armazenar os registros de gastos --- precisa melhorar
def salvarGasto(mes, descrição, valor):
  arquivoDeGastos.write('%s\t%s\t%s\n' % ("mês: "+mes, "descrição: "+descrição, valor))

while(True):
  
    print("Gerenciador de Despesas")
    print("------------------------------")
    print("Opções:")
    print("1 - Incluir")
    print("2 - Exibir")
    print("3 - Sair")
    print("------------------------------")
    opcao=int(input("== Digite a opção desejada: =="))

# solicitar informações ao usuario
    if(opcao==1):
        print("== algumas despesas são: ==")
        print("== Aluguel - Condominio - Energia - Internet - Faculdade - Financiamento - Cartão de Crédito ==")
        mes = input("Digite o mês que você gastou o dinheiro:")
        descrição = input("Descrição do gasto:")
        valor = float(input("Qual foi o valor gasto?"))

# Confirmar as informações antes de confirmar (uma última verificação)
        confirmarInformacoes = input("Gostaria de confirmar essas informações antes de salvar? (s/n) ")
        if confirmarInformacoes == "s":
            salvarGasto(mes, descrição, valor)

# Se usuário digitar "n"
        else:
            print("Nenhum gasto foi salvo.")
    
    elif(opcao==3):
        break



# Finalizando o programa
arquivoDeGastos.close()
print("Obrigado por usar o Gerenciador de Gastos Mensais.")