def gerartabuada():
    per = 'S' and 's'
    while per == 'S' or 's':
        num = int(input('Digite um número entre 1 e 10 e lhe direi sua tabuada: '))
        if num > 0 and num < 11:
            print(f'Tabuada do número: {num}')
            for i in range(1, 11):
                print(f'{num} x {i} = {num*i}')
            per = str(input('Quer continuar? S/N'))
        else:
            print('O número digitado não condiz com o enunciado!')
            per = str(input('Quer continuar? S/N '))

gerartabuada()
