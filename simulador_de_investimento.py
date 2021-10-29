
while True:
    print("-------------------------------")
    print("  Seja bem-vindo(a) ao Mybank  ")
    print("    SIMULADOR DE INVESTIMENTO    ")
    print("-------------------------------")

    print("Títulos que oferecemos simulação: ")
    print("1-Tesouro Prefixado 2024")
    print("2-Tesouro Prefixado 2026")

    cliente = str(input("Qual simulação deseja fazer? 1/2: "))

    if cliente == '1':
        vi = int(input("Qual o valor que você quer investir?: "))
        vm = int(input("Qual o valor você vai investir todo mês?: "))

        v = (vm*32) + vi
        porcentagem_ir = (v*95)/100
        ir = v - porcentagem_ir
        porcentagem_b3 = (v/100)*0.25
        vlu = v*0.1049
        vb = v + vlu

        vl = vb-(ir+porcentagem_b3)

    elif cliente == '2':
        vi = int(input("Qual o valor que você quer investir?: "))
        vm = int(input("Qual o valor você vai investir todo mês?: "))

        v = (vm*50) + vi
        porcentagem_ir = (v*95)/100
        ir = v - porcentagem_ir
        porcentagem_b3 = (v/100)*0.25
        vlu = v*0.1049
        vb = v + vlu

        vl = vb-(ir+porcentagem_b3)


    print("-------------------------------")
    print("   RESULTADO DA SIMULAÇÃO      ")
    print("-------------------------------")
    print("Valor inicial investido: ", vi)
    print("Aportes Mensais (32): ", vm)
    print("Valor total investido: ", v)
    print("Valor bruto: ", vb)
    print("I.R.: ", ir)
    print("Taxa da B3: ", porcentagem_b3)
    print("Valor líquido: ", vl)

    print("-------------------------------")
    opcao = str(input("Deseja realizar outra simulação? s/n: "))

    if opcao == 'n':
        break

print("Programa encerrado")