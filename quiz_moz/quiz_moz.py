import random
import time
import json


class QuizMocambique:
    def __init__(self):
        self.pontuacao = 0
        self.perguntas_respondidas = 0
        self.perguntas = self.carregar_perguntas()

    def carregar_perguntas(self):
        """Carrega as perguntas de um ficheiro JSON."""
        try:
            with open("perguntas.json", "r", encoding="utf-8") as file:
                perguntas = json.load(file)
                random.shuffle(perguntas)  # Embaralha as perguntas
                return perguntas[:10]  # Seleciona 10 perguntas
        except FileNotFoundError:
            print("Erro: O ficheiro 'perguntas.json' não foi encontrado!")
            return []
        except json.JSONDecodeError:
            print("Erro: O ficheiro 'perguntas.json' tem um formato inválido!")
            return []

    def exibir_boas_vindas(self):
        print("\n" + "=" * 60)
        print("        BEM-VINDO AO QUIZ DE CONHECIMENTOS SOBRE MOÇAMBIQUE")
        print("=" * 60)
        print("\nTeste seus conhecimentos sobre Moçambique!")
        print("O quiz contém perguntas selecionadas aleatoriamente.")
        print("Responda digitando a letra da opção (A, B, C ou D).")
        print("\nATENÇÃO: O quiz será encerrado se você errar uma pergunta!")
        print("\nBoa sorte!\n")

    def fazer_pergunta(self, pergunta_dict):
        letras = ['A', 'B', 'C', 'D']
        print("\n" + "-" * 60)
        print(pergunta_dict["pergunta"])
        print("-" * 60)

        for i, opcao in enumerate(pergunta_dict["opcoes"]):
            print(f"{letras[i]}. {opcao}")

        while True:
            resposta = input("\nSua resposta (A-D): ").strip().upper()
            if resposta in letras:
                return letras.index(resposta)
            else:
                print("Por favor, digite uma letra entre A e D.")

    def verificar_resposta(self, resposta_usuario, resposta_correta):
        letras = ['A', 'B', 'C', 'D']
        if resposta_usuario == resposta_correta:
            print("\n✓ CORRETO! Muito bem!")
            self.pontuacao += 1
            self.perguntas_respondidas += 1
            time.sleep(1.5)
            return True
        #caso usuario erre uma pergunta vai exibir esta mensagem e encerrar o quiz.
        else:
            print(f"\n✗ INCORRETO! A resposta correta é {letras[resposta_correta]}.")
            print("\nVocê errou uma questão! O quiz será encerrado.")
            print(f"Sua pontuação final: {self.pontuacao}/{self.perguntas_respondidas + 1}")
            time.sleep(2)
            return False

    def exibir_resultado_final(self):
        percentual = (self.pontuacao / self.perguntas_respondidas) * 100

        print("\n" + "=" * 60)
        print(f"          RESULTADO FINAL: {self.pontuacao}/{self.perguntas_respondidas} ({percentual:.1f}%)")
        print("=" * 60)

        if self.pontuacao == self.perguntas_respondidas:
            print("\nPARABÉNS! Você acertou todas as perguntas!")
        else:
            print("\nVocê completou o quiz com sucesso!")

    def iniciar_quiz(self):
        self.exibir_boas_vindas()

        if not self.perguntas:
            print("Não foi possível iniciar o quiz. Verifique o ficheiro 'perguntas.json'.")
            return

        for pergunta_dict in self.perguntas:
            resposta_correta = self.fazer_pergunta(pergunta_dict)
            resultado = self.verificar_resposta(resposta_correta, pergunta_dict["resposta_correta"])

            # Se o usuário errou, encerra o quiz
            if not resultado:
                return

        # Se chegou até aqui, completou o quiz
        self.exibir_resultado_final()


if __name__ == "__main__":
    quiz = QuizMocambique()
    quiz.iniciar_quiz()
