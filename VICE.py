# VICE12
# https://br.spoj.com/problems/VICE12/
# Proposta de encontrar o vice campeao entre três valores inputados pelo usuário

# A resolução foi feita com tratamento adequado de erros assim como requisitado;
# A 'ordenação' dos valores é feita de uma forma simples, se o numero é maior que o campeao,
# o campeao passa para o segundo lugar e este toma o seu lugar,
# se este, por outra via, for maior que o vice, este passa a ser o vice.
# A posicão do valor campeao só é registrada para o controle do vice sendo desprezível para o resultado.

# Um problema encontrado foi o nivel alto necessário de tratamento de dados do usuário caso seja necessário
# feedback mais preciso.


values = input("Entre os três valores: ").split(" ", 3)

primeiro = 0
segundo = 0
try:
    for item in values:
        try:
            item = int(item)
        except:
            raise ValueError('Valor inserido nao e numero')

        if (item > 100 or item < 1):
            raise ValueError("Numero nao esta entre 1 e 100")
        if (item > primeiro):
            segundo = primeiro
            primeiro = item
        elif item > segundo:
            segundo = item

    print("VICE: ", segundo)

except ValueError:
    raise
except:
    print("**Most likely an Input Error occured**\nTry again")
    raise

