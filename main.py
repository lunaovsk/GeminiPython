import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv() 

keyApiGoogle = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = keyApiGoogle)
modeloEscolhido = "gemini-1.5-flash"


promptSistema = "Liste apenas os nomes dos produto, e ofereça uma breve descrição. "

configModelo = {
    "temperature": 0.1,
    "top_p": 1.0,
    "top_k": 2,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain" 
}

llm = genai.GenerativeModel (
    model_name = modeloEscolhido,
    system_instruction = promptSistema,
    generation_config = configModelo

)

pergunta = "Liste 3 produtos de moda para sair hoje de noite? "
reposta = llm.generate_content(pergunta)
os.system('cls')
print(reposta.text)