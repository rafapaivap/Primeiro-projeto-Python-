print('-----------------painting budget--------------------')
larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
print('----------------------------------------------------')
print('ATENÇÃO! Caso não haja portas ou janelas, digite o valor 0. Caso haja mais de uma janela ou porta, some-os.')
porta_alt = float(input('Altura da porta: '))
porta_larg = float(input('Largura da porta: '))
janela_alt = float(input('Altura da janela: '))
janela_larg = float(input('Largura da janela: '))
porta = porta_alt * porta_larg
janela = janela_alt * janela_larg
porta_janela = janela + porta
area = larg * alt
areareal = area - porta_janela
print('Sua parede tem {:.2f}m2 de área total desconsiderando portas e janelas.'.format(areareal))
m2_tinta = 27
qtd_tinta = areareal / m2_tinta 
print('-----------------------------------------------------')
print('Para pintar esta área, você precisara de {:.2f}L de tinta'.format(qtd_tinta))
print('-----------------------------------------------------')
'''Valores de tintas'''
tinta_suvinil = 30
tinta_coral = 12
tinta_eucatex = 19
tinta_quartzolit = 8
'''Opçoes'''
print('Código Suvinil [1]')
print('Código Coral [2]')
print('Código Eucatex [3]')
print('Código Quartzolit [4]')
opcao_tinta = input('Tinta escolhida: ')
if opcao_tinta == '1': 
    total = tinta_suvinil*areareal + areareal*12
    print('O valor da mão de obra é:R${:.2f}'.format(areareal*12))
    print('Valor total da obra:R${:.2f}'.format(total))
elif opcao_tinta == '2': 
    total = tinta_coral*areareal + areareal*12
    print('O valor da mão de obra é:R${:.2f}'.format(areareal*12))
    print('Valor total da obra:R${:.2f}'.format(total))
elif opcao_tinta == '3': 
    total = tinta_coral*areareal + areareal*12
    print('O valor da mão de obra é:R${:.2f}'.format(areareal*12))
    print('Valor total da obra:R${:.2f}'.format(total))
elif opcao_tinta == '4': 
    total = tinta_quartzolit*areareal + areareal*12
    print('O valor da mão de obra é:R${:.2f}'.format(areareal*12))
    print('Valor total da obra:R${:.2f}'.format(total))
else:   
   print('Opção Inválida')
print('-------------------------------------------------------------------------')
print('Desconto de 5% para pagamento a vista e em até 6x sem juros no cartão')
pagamento = int(input('Forma de pagamento: Vista[1]/Parcelado[2]: '))
if pagamento == 1:
    print('Desconto de 5%')
    calc_desc = ((5/100) * total) 
    desc = total - calc_desc
    print(' Desconto aplicado para pagamento a vista. Valor total R${:.2f}'.format(desc))
elif pagamento == 2:
    parc_x = int(input('Quantidade de parcelas: '))
    if parc_x == 2:
       parcela = total/2
       print('2X sem juros de R${:.2f}'.format(parcela))
    elif parc_x == 3:
        parcela = total/3
        print('3X sem juros de R${:.2f}'.format(parcela))
    elif parc_x == 4:
        parcela = total/4
        print('4X sem juros de R${:.2f}'.format(parcela))
    elif parc_x == 5:
        parcela = total/5
        print('5X sem juros de R${:.2f}'.format(parcela))
    elif parc_x == 6:
        parcela = total/6
        print('6X sem juros de R${:.2f}'.format(parcela))
    else:
        print('Pagamento até 6X sem juros')

    