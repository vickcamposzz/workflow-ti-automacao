# Sistema Inteligente de Triagem e Validação de Ofícios de TI
# Fase 1 — Workflow-first

---

# Propósito da Fase

Desenvolver um workflow estruturado para recebimento, leitura e organização de ofícios de TI enviados ao órgão público.

---

# Objetivo da Atividade

Construir um fluxo capaz de:

- receber ofícios;
- identificar o tipo de solicitação;
- validar dados obrigatórios;
- extrair informações relevantes;
- registrar inconsistências;
- produzir uma tabela estruturada.

---

# Workflow Esperado

## Etapa 1 — Receber Ofício

Entrada:
Documento contendo solicitação de TI.

Saída:
Texto identificado.

---

## Etapa 2 — Identificar Serviço

Serviços possíveis:

- criação AD;
- criação SGD;
- acesso remoto;
- reset senha;
- permissões.

---

## Etapa 3 — Extrair Dados

Campos esperados:

- nome completo;
- CPF;
- setor;
- perfil solicitado;
- justificativa;
- telefone.

---

## Etapa 4 — Validar Informações

Verificações:

- CPF informado;
- nome completo;
- setor preenchido;
- justificativa presente.

- inconsistências registradas.