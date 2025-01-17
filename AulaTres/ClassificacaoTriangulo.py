A = int(input('Digite o primeiro lado do triângulo:'))
B = int(input('Digite o segundo lado do triângulo:'))
C = int(input('Digite o terceiro lado do triângulo:'))

if(A > 0) and (B > 0) and (C > 0):
    if( A + B > C) and (A + C > B) and (B + C > A):
        if (A != B and A != C):
            print('Triângulo escaleno')
        else:
            if(A == B and A == C):
                print('Triângulo equilátero')
            else:
                print('Triangulo isósceles')
    else:
        print('Ao menos um dos valores está inválido para ser um triângulo')
else:
    print('Ao menos um dos valores está inválido para ser um triângulo')