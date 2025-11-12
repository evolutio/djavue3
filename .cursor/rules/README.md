# 🧩 Regras do Projeto DjaVue

Este diretório contém as **regras do projeto** para o DjaVue, um template fullstack Django + Vue 3.

## 📂 Estrutura

```
.cursor/rules/
├── README.md                    # Este arquivo
├── djavue-project.mdc          # Regras gerais do projeto
├── backend/                    # Regras do backend Django
│   ├── django-architecture.mdc # Arquitetura em camadas
│   ├── django-services.mdc     # Padrão de services
│   ├── django-models.mdc       # Padrão de models
│   └── django-tests.mdc        # Padrão de testes
└── frontend/                   # Regras do frontend Vue
    ├── vue-architecture.mdc    # Arquitetura Vue
    ├── vue-stores.mdc          # Padrão de stores Pinia
    ├── vue-api-client.mdc      # Padrão de API Client
    ├── vue-components.mdc      # Padrão de componentes
    └── vue-router.mdc          # Padrão de rotas
```

## 📘 Regras Globais

- **djavue-project.mdc**: Visão geral do projeto, arquitetura, convenções e princípios gerais

## 🦄 Regras do Backend (Django)

### django-architecture.mdc
Define a arquitetura em camadas:
- **urls** → **views** → **services** → **models**
- Views enxutas (thin controllers)
- Services com regras de negócio (Python puro, testável)
- Models com método `to_dict_json()`

### django-services.mdc
Padrões para services:
- Nomenclatura: `[nome]_svc.py`
- Funções retornam `dict`
- Validações e tratamento de erros
- Logging adequado

### django-models.mdc
Padrões para models:
- Método `to_dict_json()` obrigatório
- Método `__str__()` para representação
- Meta options apropriadas
- Campos com validações

### django-tests.mdc
Padrões para testes:
- pytest como framework
- Estrutura de testes
- Fixtures e mocking
- Cobertura de código

## 🎨 Regras do Frontend (Vue 3)

### vue-architecture.mdc
Define a arquitetura:
- **Router** → **Pages** → **Store** → **API Client** → **Backend**
- Organização modular por contexto
- Convenções de nomenclatura

### vue-stores.mdc
Padrões para stores Pinia:
- State, actions e getters
- Uso em componentes (Options API e Composition API)
- Tratamento de loading e erros

### vue-api-client.mdc
Padrões para API Client:
- Organização por contexto
- Configuração do Axios
- Tratamento de erros (interceptors)
- Nomenclatura de funções

### vue-components.mdc
Padrões para componentes:
- Props com validação
- Events declarados
- Estilos scoped
- Composition API

### vue-router.mdc
Padrões para rotas:
- Organização por contexto
- Nomenclatura consistente
- Layouts reutilizáveis
- Proteção de rotas

## 🚀 Como Usar

As regras são aplicadas automaticamente pelo Cursor AI baseado em:

1. **alwaysApply: true**: Aplicadas sempre (regras globais)
2. **globs**: Aplicadas quando arquivos correspondem aos padrões
3. **description**: Usadas quando relevante ao contexto

## 📝 Convenções

### Nomenclatura
- **Python**: `snake_case`
- **JavaScript**: `camelCase` (funções/variáveis), `PascalCase` (componentes)
- **Apps Django**: Plural quando representam coleções
- **Stores**: `use[Nome]Store`

### Estrutura
- Backend: Apps separadas por contexto
- Frontend: Módulos separados por contexto
- Organização modular e reutilizável

## 🔧 Manutenção

- Manter regras atualizadas com as práticas do projeto
- Adicionar novas regras quando necessário
- Documentar padrões novos ou mudanças
- Revisar periodicamente para consistência

## 📚 Referências

- [Django Documentation](https://docs.djangoproject.com/)
- [Vue 3 Documentation](https://vuejs.org/)
- [Pinia Documentation](https://pinia.vuejs.org/)
- [Vue Router Documentation](https://router.vuejs.org/)

