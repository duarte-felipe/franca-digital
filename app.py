import gradio as gr
import requests
import io
from PIL import Image # Pillow
import os # Para acessar variáveis de ambiente
import json

# --- Configuração ---
# No Hugging Face Spaces, configure HF_TOKEN como um "Space Secret"
HF_TOKEN = os.environ.get("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"

headers = {}
if HF_TOKEN:
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    print("INFO: Token HF carregado da variável de ambiente.") # Isso aparecerá nos logs do Space
else:
    # Esta mensagem aparecerá nos logs do Space se o token não estiver configurado
    print("ALERTA: HF_TOKEN não encontrado como variável de ambiente. A API não funcionará.")
    # Você pode optar por levantar um erro aqui ou deixar a interface carregar com uma mensagem de erro.

def gerar_imagem_para_gradio(prompt_texto):
    """
    Função que recebe um prompt, chama a API e retorna a imagem ou uma mensagem de erro.
    """
    if not HF_TOKEN:
        return None, "Erro Crítico: Token do Hugging Face não está configurado no servidor. Contate o administrador do Space."
    if not prompt_texto or not prompt_texto.strip():
        return None, "Por favor, insira um prompt válido."

    payload = {"inputs": prompt_texto}
    status_message = f"Enviando prompt: '{prompt_texto}'. Aguarde..."
    print(status_message) # Log para o servidor

    try:
        # Timeout aumentado para dar tempo à API
        response = requests.post(API_URL, headers=headers, json=payload, timeout=180) # Timeout de 3 minutos
        
        # Verifica se a resposta foi bem-sucedida e contém uma imagem
        if response.status_code == 200 and 'image' in response.headers.get('Content-Type', ''):
            print("Imagem recebida com sucesso da API.")
            try:
                image = Image.open(io.BytesIO(response.content))
                return image, f"Imagem gerada para: '{prompt_texto}'"
            except Exception as e: # PIL.UnidentifiedImageError é uma subclasse de Exception
                print(f"Erro ao abrir a imagem recebida: {e}")
                return None, f"Erro ao processar a imagem recebida da API: {e}"
        else:
            # Tratar erros da API (que geralmente vêm como JSON)
            status_code = response.status_code
            try:
                error_details = response.json()
                api_error_message = error_details.get("error", "Erro desconhecido na resposta da API.")
                if isinstance(api_error_message, list): # Às vezes o erro é uma lista
                    api_error_message = api_error_message[0]
                
                estimated_time = error_details.get("estimated_time")
                full_error_message = f"Erro da API (Status {status_code}): {api_error_message}"
                if estimated_time:
                    full_error_message += f" (Modelo pode estar carregando, tempo estimado: {estimated_time:.0f}s. Tente novamente.)"
                print(full_error_message)
                return None, full_error_message
            except json.JSONDecodeError: # Se a resposta de erro não for JSON
                error_text = response.text[:200] # Pegar os primeiros 200 caracteres
                print(f"Erro da API (Status {status_code}): {error_text}")
                return None, f"Erro da API (Status {status_code}): {error_text}"

    except requests.exceptions.Timeout:
        print("Erro: Timeout ao chamar a API.")
        return None, "Erro: A requisição demorou muito para responder (timeout). Tente um prompt mais simples ou novamente mais tarde."
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão com a API: {e}")
        return None, f"Erro de conexão com a API: {e}"
    except Exception as e: # Pega outros erros inesperados
        print(f"Um erro inesperado ocorreu: {e}")
        return None, f"Um erro inesperado ocorreu: {str(e)}"

# --- Interface Gradio ---
with gr.Blocks(theme=gr.themes.Soft()) as iface:
    gr.Markdown(
        """
        # 🎨 Gerador de Imagens com IA Franca Digital (Stable Diffusion 3 Medium)
        Digite uma descrição (prompt) para gerar uma imagem.
        A primeira geração pode demorar um pouco enquanto o modelo "aquece" na API.
        """
    )
    with gr.Row():
        with gr.Column(scale=2):
            prompt_input = gr.Textbox(
                lines=3,
                placeholder="Ex: Um gato astronauta com capacete de vidro, olhando para a Terra do espaço, estrelas ao fundo, arte digital detalhada.",
                label="Descreva a Imagem que Você Quer Criar:"
            )
            generate_button = gr.Button("Gerar Imagem ✨", variant="primary")
        with gr.Column(scale=1):
            output_image = gr.Image(label="Imagem Gerada", type="pil", height=512, width=512)
            status_textbox = gr.Textbox(label="Status / Mensagens")
    
    gr.Examples(
        examples=[
            ["Um dragão majestoso feito de cristais coloridos voando sobre montanhas vulcânicas, fantasia épica, altamente detalhado."],
            ["Retrato de um cientista robô idoso com óculos, em um laboratório futurista, iluminação suave, estilo Norman Rockwell."],
            ["Uma floresta encantada à noite, com cogumelos bioluminescentes e um caminho de pedras brilhantes, atmosfera mágica, aquarela digital."]
        ],
        inputs=[prompt_input]
    )

    generate_button.click(
        fn=gerar_imagem_para_gradio,
        inputs=[prompt_input],
        outputs=[output_image, status_textbox]
    )

# Para rodar localmente para teste: iface.launch()
# Para Hugging Face Spaces, a plataforma chama iface.launch() automaticamente se este for o último comando.
if __name__ == '__main__':
    if not HF_TOKEN:
        print("**************************************************************************")
        print("ALERTA: HF_TOKEN não está configurado como variável de ambiente!")
        print("A aplicação Gradio será iniciada, mas a geração de imagens FALHARÁ.")
        print("Ao hospedar no Hugging Face Spaces, configure HF_TOKEN como um 'Secret'.")
        print("**************************************************************************")
    iface.launch()

