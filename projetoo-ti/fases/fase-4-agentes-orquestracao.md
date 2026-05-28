# Sistema Inteligente de Triagem e Validação de Ofícios de TI
# Fase 4 — Agentes e Orquestração

---

# Propósito da Fase

Criar um agente capaz de analisar ofícios de TI e gerar um roteiro básico de atendimento utilizando ferramentas MCP autorizadas.

---

# Missão do Agente

"Analisar ofícios de TI recebidos pelo órgão público, validar os dados obrigatórios conforme o tipo de serviço e gerar um roteiro básico de atendimento utilizando ferramentas autorizadas via MCP."

---

# Ferramentas Permitidas

- usuario();
- servicos();
- validar_ad_tool();
- validar_sgd_tool();

---

# Limites do Agente

- máximo de 5 consultas;
- sem APIs externas;
- apenas dados locais;
- sem integração real com Active Directory.

---

# Workflow Esperado

1. Receber solicitação;
2. Identificar serviço;
3. Validar contrato;
4. Consultar dados;
5. Gerar roteiro;
6. Registrar incertezas.

---

# Contrato da Saída

A saída deve conter:

- nome do usuário;
- tipo do serviço;
- etapas sugeridas;
- inconsistências;
- alertas;
- limitações.

---

# Critérios de Conclusão

- agente documentado;
- MCP funci