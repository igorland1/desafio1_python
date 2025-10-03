# 📇 Agenda de Contatos - Python

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Rocketseat-8257E6?style=for-the-badge&logo=rocket&logoColor=white" alt="Rocketseat"/>
</div>

## 📋 Sobre o Projeto

Este projeto é o **Desafio 01** da formação Python da [Rocketseat](https://www.rocketseat.com.br/). Trata-se de uma aplicação de linha de comando para gerenciar uma agenda de contatos, permitindo adicionar, editar, deletar e marcar contatos como favoritos.

O projeto foi desenvolvido com o objetivo de aplicar conceitos fundamentais de Python, incluindo:
- Estruturas de dados (listas e dicionários)
- Funções
- Loops e condicionais
- Entrada e saída de dados
- Formatação de texto com códigos ANSI

## ✨ Funcionalidades

A aplicação oferece as seguintes funcionalidades:

- ✅ **Adicionar contato** - Cadastre novos contatos com nome, telefone e email
- 📋 **Listar contatos** - Visualize todos os contatos cadastrados
- ✏️ **Editar contato** - Atualize as informações de um contato existente
- ⭐ **Favoritar contato** - Marque contatos importantes como favoritos
- 🚫 **Remover favorito** - Desmarque contatos da lista de favoritos
- 💛 **Listar favoritos** - Visualize apenas os contatos marcados como favoritos
- 🗑️ **Apagar contato** - Remova contatos da agenda

## 🎨 Interface

A aplicação utiliza códigos ANSI para colorir o terminal, tornando a experiência mais agradável:

- 🟣 **Roxo** - Títulos
- 🟡 **Amarelo** - Contatos favoritos
- 🟢 **Verde** - Mensagens de sucesso
- 🔴 **Vermelho** - Mensagens de erro e avisos

## 🚀 Como Executar

### Pré-requisitos

- Python 3.x instalado em sua máquina

### Passos

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/agenda-contatos-python.git
```

2. Navegue até o diretório do projeto:
```bash
cd agenda-contatos-python
```

3. Execute o programa:
```bash
python projeto.py
```

## 💻 Como Usar

Ao executar o programa, você verá um menu com 8 opções:

```
Aplicativo Agenda de Contatos

1 - Adicionar contato
2 - Listar contatos
3 - Editar contato
4 - Favoritar contato
5 - Remover favorito
6 - Listar contatos favoritos
7 - Apagar contato
8 - Sair
```

Digite o número correspondente à ação desejada e siga as instruções na tela.

## 🗂️ Estrutura do Código

```python
# Classes e Funções principais:
- Cores: Define as cores ANSI para formatação do terminal
- adicionar_contato(): Adiciona um novo contato à agenda
- listar_contatos(): Exibe todos os contatos cadastrados
- editar_contato(): Permite editar informações de um contato
- favoritar_contato(): Marca um contato como favorito
- remover_favorito(): Remove a marcação de favorito
- listar_favoritos(): Exibe apenas contatos favoritos
- apagar_contato(): Remove um contato da agenda
```

## 🎯 Objetivos de Aprendizado

Este desafio permitiu praticar:

- ✅ Manipulação de listas e dicionários
- ✅ Criação e utilização de funções
- ✅ Controle de fluxo com loops e condicionais
- ✅ Validação de entrada do usuário
- ✅ Formatação e estilização de saída no terminal
- ✅ Organização e estruturação de código

## 📝 Regras da Aplicação

- Cada contato possui: nome, telefone, email e status de favorito
- É possível ter múltiplos contatos favoritos
- Os contatos são armazenados em memória durante a execução
- A numeração dos contatos é gerada automaticamente

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📄 Licença

Este projeto está sob a licença MIT.

## 👨‍💻 Autor

Desenvolvido com 💜 durante a formação Python da Rocketseat

---

<div align="center">
  Feito por Igor Landi 🚀
</div>
