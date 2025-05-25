import os 
import google.generativeai as genai
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

promptSistema = """
Identifique o perfil de compra para cada cliente a seguir.

O formato de saída deve ser:

cliente - descreva o perfil do cliente em 3 palavras
"""

promptUsuario = carrega(os.path.join("dados", "lista_de_compras_100_clientes.csv")) 

modeloFlash = genai.GenerativeModel(f"models/{model}")
qntTokens = modeloFlash.count_tokens(promptUsuario)

print(f"O modelo foi: {model}")

llm = genai.GenerativeModel (
    model_name= model,
    system_instruction=promptSistema
)

reposta = llm.generate_content(promptUsuario)

print(f"Resposta: {reposta.text}")