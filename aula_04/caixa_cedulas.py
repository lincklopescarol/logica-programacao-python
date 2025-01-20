valor = int(input('Digite o valor em R$: '))

while True:
    if valor >= 200:
        cedulas200 = valor // 200
        valor = valor - cedulas200 * 200
        print('Cédulas de 200: {}'.format(cedulas200))
        if not valor:
            break
    if valor >= 100:
        cedulas100 = valor // 100
        valor = valor - cedulas100 * 100
        print('Cédulas de 100: {}'.format(cedulas100))
        if not valor:
            break
    if valor >= 50:
        cedulas50 = valor // 50
        valor = valor - cedulas50 * 50
        print('Cédulas de 50: {}'.format(cedulas50))
        if not valor:
            break
    if valor >= 20:
        cedulas20 = valor // 20
        valor = valor - cedulas20 * 20
        print('Cédulas de 20: {}'.format(cedulas20))
        if not valor:
            break
    if valor >= 10:
        cedulas10 = valor // 10
        valor = valor - cedulas10 * 10
        print('Cédulas de 10: {}'.format(cedulas10))
        if not valor:
            break
    if valor >= 5:
        cedulas5 = valor // 5
        valor = valor - cedulas5 * 5
        print('Cédulas de 5: {}'.format(cedulas5))
        if not valor:
            break
    if valor:
        moedas1 = valor
        print('Moedas de 1: {}'.format(moedas1))
        break
