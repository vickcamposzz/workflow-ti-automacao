from fastmcp import FastMCP

from tools_chamados import (
    buscar_usuario,
    validar_ad,
    validar_sgd,
    listar_servicos,
    carregar_json
)

mcp = FastMCP("mcp_chamados_ti")

@mcp.tool()
def usuario(nome: str):
    return buscar_usuario(nome)

@mcp.tool()
def servicos():
    return listar_servicos()

@mcp.tool()
def validar_ad_tool(indice: int):

    dados = carregar_json()

    chamado = dados["chamados"][indice]

    return validar_ad(chamado)

@mcp.tool()
def validar_sgd_tool(indice: int):

    dados = carregar_json()

    chamado = dados["chamados"][indice]

    return validar_sgd(chamado)

if __name__ == "__main__":
    mcp.run()