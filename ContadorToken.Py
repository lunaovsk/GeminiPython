import os 
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv() 

keyApiGoogle = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = keyApiGoogle)

modeloFlash = "gemini-1.5-flash"
modeloPro = "gemini-1.5-pro"

custoEntradaFlash = 0.15
custoSaidaFlash = 3.5

custoEntradaPro = 1.25
custoSaidaPro = 10

modelFlash = genai.get_model(f"models/{modeloFlash}")
limitesModeloFlash = {
    "token": modelFlash.input_token_limit,
    "tokenSaida": modelFlash.output_token_limit,
}

print(f"Limites do modelo flash são: {limitesModeloFlash}")

modelPro = genai.get_model(f"models/{modeloPro}")
limitesModeloPro = {
    "token": modelPro.input_token_limit,
    "tokenSaida": modelPro.output_token_limit,
}

print(f"Limites do modelo pro são: {limitesModeloPro}")

llmFlash = genai.GenerativeModel (
    f"models/{modeloFlash}"
)

qntTokens = llmFlash.count_tokens("O que é uma calça de shopping?")
print(f"A qnt de tokens é: {qntTokens}")

resposta = llmFlash.generate_content("O que é uma calça de shopping?")
tokens_prompt = resposta.usage_metadata.prompt_token_count
tokens_resposta = resposta.usage_metadata.candidates_token_count

custo_total = (tokens_prompt * custoEntradaFlash) / 1000000 + (tokens_resposta * custoSaidaFlash) / 1000000
print(f"Custo Total U$ Flash: ", custo_total)

custo_total = (tokens_prompt * custoEntradaPro) / 1000000 + (tokens_resposta * custoSaidaPro) / 100.000
print(f"Custo Total U$ Pro: ", custo_total)