# Sistema Inteligente de Triagem e Validação de Ofícios de TI
# Fase 3 — Tool Calling + Python + MCP

---

# Propósito da Fase

Adicionar validação automática utilizando Python e exposição das ferramentas via MCP.

---

# Ferramentas Esperadas

## Funções Python

- carregar_json();
- validar_ad();
- validar_sgd();
- buscar_usuario();
- listar_servicos();

---

# Servidor MCP

Nome:

mcp_chamados_ti

---

# Workflow Esperado

1. Ler JSON;
2. Validar contratos;
3. Tratar erros;
4. Expor funções via MCP;
5. Realizar consultas.

---

# Exemplos de Perguntas

- Existe acesso SGD para Ana Vitória?
- Quais usuários possuem perfil TI-PGE?
- O ofício possui CPF?

---

# Critérios de Conclusão

- JSON validado;
- funções funcionando;
- MCP operacional.