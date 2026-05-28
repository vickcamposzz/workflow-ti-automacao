

# Workflow-First para Automação de Chamados de TI

Projeto acadêmico desenvolvido com foco em Workflow-first, contratos YAML, validação de JSON, Tool Calling, MCP e automação de processos reais de TI em órgão público.

O sistema simula o fluxo de atendimento utilizado para:

* criação de usuários Active Directory (AD);
* solicitação de perfis SGD;
* validação de documentos;
* extração automatizada de dados via PDF;
* validação contratual utilizando YAML.

---

# Objetivo

Automatizar a leitura e validação de ofícios administrativos utilizados em solicitações internas de TI.

O projeto recebe arquivos PDF contendo solicitações de:

* criação de usuário AD;
* criação de perfil SGD.

A partir disso, o workflow:

1. lê o PDF;
2. extrai os dados relevantes;
3. gera estrutura JSON;
4. valida os dados utilizando contratos YAML;
5. retorna sucesso ou inconsistências encontradas.

---

# Tecnologias Utilizadas

* Python
* PyMuPDF
* JSON
* YAML
* MCP (Model Context Protocol)
* FastMCP
* Workflow-first
* Tool Calling

---

# Estrutura do Projeto

```bash
projeto-ti/
│
├── tools_chamados.py
├── mcp_chamados_ti.py
├── chamados_ti.json
├── contrato_ad.yaml
├── contrato_sgd.yaml
├── oficio_ad.pdf
├── oficio_sgd.pdf
├── oficio_ad_incompleto.pdf
├── oficio_sgd_incompleto.pdf
│
├── fases/
│   ├── fase-1-workflow-first.md
│   ├── fase-2-workflows-contratos.md
│   ├── fase-3-tool-calling-python-mcp.md
│   └── fase-4-agentes-orquestracao.md
```

---

# Funcionalidades

* Leitura automática de PDFs;
* Extração de dados textuais;
* Geração de JSON estruturado;
* Validação de contratos YAML;
* Tratamento de erros;
* Simulação de Tool Calling;
* Exposição de funções via MCP;
* Workflow-first aplicado a processos reais.

---

# Exemplos de Testes

## Teste PDF AD válido

```python
from tools_chamados import *

texto = ler_pdf("oficio_ad.pdf")

dados = extrair_dados_pdf(texto)

validar_pdf_extraido(dados)
```

---

## Teste PDF SGD válido

```python
texto = ler_pdf("oficio_sgd.pdf")

dados = extrair_dados_pdf(texto)

validar_pdf_sgd(dados)
```

---

## Teste PDF inválido

```python
texto = ler_pdf("oficio_ad_incompleto.pdf")

dados = extrair_dados_pdf(texto)

validar_pdf_extraido(dados)
```

---

# Resultados Esperados

## PDF válido

```json
{
  "status": "ok",
  "mensagem": "PDF validado com sucesso"
}
```

## PDF inválido

```json
{
  "status": "erro",
  "mensagem": "Campo obrigatório ausente"
}
```

---

# Conceitos Aplicados

* Workflow-first
* Contratos estruturados
* Validação automatizada
* Tool Calling
* MCP
* Automação de processos administrativos
* Processamento de documentos PDF
* Estruturação JSON

---

# Autor

Ana Vitória Campos da Silva

Projeto acadêmico desenvolvido para disciplina de Inteligencia Artificial.
