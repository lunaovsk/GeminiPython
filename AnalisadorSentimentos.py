import os 
import google.generativeai as genai
from google.api_core.exceptions import NotFound
from dotenv import load_dotenv


load_dotenv() 

keyApiGoogle = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = keyApiGoogle)
model = "gemini-1.5-flash"


def carrega(nomeArquivo):
  try:
    with open(nomeArquivo, "r") as arquivo:
      dados = arquivo.read()
      return dados
  except IOError as e:
    print(f"Erro: {e}")

def salva(nomeArquivo, conteudo): 
    try:
        with open(nomeArquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")
def analisadorSentimentos (nomeProduto):
    promptSistema = f"""
            Você é um analisador de sentimentos de avaliações de produtos.
            Escreva um parágrafo com até 50 palavras resumindo as avaliações e
            depois atribua qual o sentimento geral para o produto.
            Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

            # Formato de Saída

            Nome do Produto:
            Resumo das Avaliações:
            Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
            Ponto fortes: lista com três bullets
            Pontos fracos: lista com três bullets
        """
    promptUsuario = carrega("dados/avaliacoes.txt")

    print(f"Iniciamos a anpalise de sentimentos do produto: {nomeProduto}")

    try:
        llm = genai.GenerativeModel (
            model_name= model,
            system_instruction=promptSistema
        )

        reposta = llm.generate_content(promptUsuario)
        textoResposta = reposta.text

        salva(f"dados/reposta-{nomeProduto}.txt", textoResposta)
        return reposta.text
    except NotFound as e: 
       print("Erro no nome do modelo: {e}")

def main(): 
   listaDeProdutos = ["Camisetas de algodão orgânico", "Jeans feitos com materiais reciclados", "Maquiagem mineral"]
   for p in listaDeProdutos:
      analisadorSentimentos(p)

if __name__ == "__main__":
   main()