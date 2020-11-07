from testeAutomatizado.soma import soma

try:
    print(soma('9', 5))
except AssertionError as e:
    print(f'Erro: {e}')
