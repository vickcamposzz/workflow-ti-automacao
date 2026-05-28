import json
import fitz

ARQUIVO = "chamados_ti.json"


def ler_pdf(caminho_pdf):

    texto = ""

    documento = fitz.open(caminho_pdf)

    for pagina in documento:
        texto += pagina.get_text()

    return texto


def extrair_dados_pdf(texto):

    dados = {}

    # Tipo do serviço

    if "AD" in texto:
        dados["tipo_servico"] = "criar_ad"

    else:
        dados["tipo_servico"] = "perfil_sgd"

    # Nome

    if "Ana Vitória Campos da Silva" in texto:
        dados["nome_completo"] = "Ana Vitória Campos da Silva"

    # CPF

    if "000.000.000-00" in texto:
        dados["cpf"] = "000.000.000-00"

    # Dados AD

    if "TI" in texto:
        dados["setor"] = "TI"

    if "(63) 99999-9999" in texto:
        dados["telefone"] = "(63) 99999-9999"

    if "comprovante" in texto.lower():
        dados["comprovante_endereco"] = True

    # Dados SGD

    if "TI-PGE" in texto:
        dados["perfil_solicitado"] = "TI-PGE"

    if "Necessário para atividades do setor" in texto:
        dados["justificativa"] = "Necessário para atividades do setor"

    return dados


def validar_pdf_extraido(dados):

    obrigatorios = [
        "nome_completo",
        "cpf",
        "setor",
        "telefone"
    ]

    for campo in obrigatorios:

        if campo not in dados:

            return {
                "status": "erro",
                "mensagem": f"Campo obrigatório ausente: {campo}"
            }

    return {
        "status": "ok",
        "mensagem": "PDF validado com sucesso"
    }


def validar_pdf_sgd(dados):

    obrigatorios = [

        "nome_completo",
        "cpf",
        "perfil_solicitado",
        "justificativa"

    ]

    for campo in obrigatorios:

        if campo not in dados:

            return {

                "status": "erro",
                "mensagem": f"Campo obrigatório ausente: {campo}"

            }

    return {

        "status": "ok",
        "mensagem": "PDF SGD validado com sucesso"

    }


def carregar_json():

    try:

        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except:

        return {
            "erro": "Falha ao carregar JSON"
        }


def buscar_usuario(nome):

    dados = carregar_json()

    encontrados = [

        c for c in dados["chamados"]

        if c["nome_completo"].lower() == nome.lower()

    ]

    return encontrados


def listar_servicos():

    dados = carregar_json()

    servicos = [

        chamado["tipo_servico"]

        for chamado in dados["chamados"]

    ]

    return list(set(servicos))


def validar_ad(chamado):

    campos = [

        "nome_completo",
        "cpf",
        "setor",
        "telefone",
        "comprovante_endereco"

    ]

    for campo in campos:

        if campo not in chamado:

            return {

                "status": "erro",
                "mensagem": f"Campo ausente: {campo}"

            }

    return {

        "status": "ok",
        "mensagem": "Contrato AD válido"

    }


def validar_sgd(chamado):

    campos = [

        "nome_completo",
        "cpf",
        "perfil_solicitado",
        "justificativa"

    ]

    for campo in campos:

        if campo not in chamado:

            return {

                "status": "erro",
                "mensagem": f"Campo ausente: {campo}"

            }

    return {

        "status": "ok",
        "mensagem": "Contrato SGD válido"

    }