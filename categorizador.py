import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv() 

keyApiGoogle = os.getenv("GEMINI_API_KEY")
genai.configure(api_key = keyApiGoogle)
modeloEscolhido = "gemini-1.5-flash"

def categoriaProdutos(nomeProduto, listaCategoriaPossiveis):
    promptSistema = f"""
            Você é um categorizador de produtos.
            Você deve assumir as categorias presentes na lista abaixo.
            Você deve sempre ter um português correto e claro. 
            Você não deve ter incertezas
            # Lista de Categorias Válidas
            {listaCategoriaPossiveis}
            # Formato da Saída
            Produto: Nome do Produto
            Categoria: apresente a categoria do produto
            # Exemplo de Saída
            Produto: Escova elétrica com recarga solar
            Categoria: Eletrônicos Verdes
        """ 
    llm = genai.GenerativeModel (
    model_name = modeloEscolhido,
    system_instruction = promptSistema,
    )
    reposta = llm.generate_content(nomeProduto)
    return reposta.text
    
def main():   
    listaCategoriaPossiveis = "Eletrônicos Verdes,Moda Sustentável,Produtos de Limpeza Ecológicos,Alimentos Orgânicos,Produtos de higie sustentáveis"
    produto = input("Informe qual o produto que deseja classificar: ")
    while produto != "":
        print(f"Resposta: {categoriaProdutos(produto, listaCategoriaPossiveis)}")
        produto = input("Informe qual o produto que deseja classificar: ")

if __name__ == "__main__":
    main()



