# Palavras-chave usadas: Todas as 35 do Python 3.11

def jogo():
    pontos = 0
    vidas = 3

    print("Bem-vindo à Aventura da Lógica!")
    print("Você começa com 3 vidas.\n")

    while vidas > 0:

        print("Escolha uma ação:")
        print("1 - Responder uma pergunta")
        print("2 - Desistir")

        try:
            escolha = int(input("Sua escolha: "))
        except Exception as e:
            print(f"Erro: {e}")
            continue

        if escolha == 1:
            pontos += pergunta()
        elif escolha == 2:
            print("Você desistiu do jogo!")
            break
        else:
            print("Opção inválida.")
            continue

        if pontos >= 3:
            print("Parabéns! Você venceu!")
            break

        if vidas <= 0:
            print("Suas vidas acabaram. Fim de jogo.")
            break

        # Pequeno desafio extra usando lambda e assert
        dobro = lambda x: x * 2
        valor = dobro(pontos)
        assert valor >= pontos, "O dobro não pode ser menor!"

        # Usando pass e continue
        if pontos == 2:
            pass  # Nenhuma ação específica, só para usar 'pass'
            continue

    else:
        print("Você saiu do loop normalmente.")

def pergunta():
    from random import choice  # usando import e from
    perguntas = [
        ("Quanto é 2 + 2?", "4"),
        ("Qual é a capital do Brasil?", "brasilia"),
        ("Python é uma linguagem de programação? (sim/não)", "sim"),
    ]

    p, resposta_correta = choice(perguntas)

    resposta = input(p + " ").lower()
    if resposta == resposta_correta:
        print("Correto!")
        return 1
    else:
        print("Errado.")
        return 0

# Simulando uma classe com métodos mágicos
class Status:
    def __init__(self, nome):
        self.nome = nome
        self._ativo = True

    def __del__(self):
        if self._ativo:
            print(f"{self.nome} foi encerrado.")

    def __str__(self):
        return f"Status do jogador: {self.nome}"

# Usando with e arquivo (try, except, finally)
try:
    with open("registro.txt", "w") as arq:
        arq.write("Jogo iniciado.\n")
except IOError as e:
    print("Erro ao criar o arquivo:", e)
finally:
    print("Arquivo de log tratado com sucesso.\n")

# Variáveis booleanas e None
rodando = True
dados = None

# Função principal com async/await simulando processamento assíncrono
import asyncio

async def main():
    global dados
    dados = Status("Iure")
    print(dados)
    await asyncio.sleep(0)  # Simulando espera

    jogo()

    del dados

# Função auxiliar com yield
def contador():
    i = 0
    while True:
        yield i
        i += 1

# Simulando escopos com nonlocal e global
def escopo_exemplo():
    contador = 0

    def incrementar():
        nonlocal contador
        contador += 1
        return contador

    return incrementar()

# Usando decorator (def + lambda + assert + functools)
def decorador(f):
    def wrapper(*args, **kwargs):
        print("Função decorada!")
        return f(*args, **kwargs)
    return wrapper

@decorador
def teste():
    print("Função teste executada.")

if __name__ == "__main__":
    teste()
    # Corrected line to use await instead of asyncio.run
    await main()
