# Códigos ANSI para cores
class Cores:
    TITULO = '\033[95m'    # Título
    AMARELO = '\033[93m'   # Favorito
    VERDE = '\033[92m'     # Positivo
    VERMELHO = '\033[91m'  # Negativo
    RESET = '\033[0m'      # Reseta

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    contatos.append(contato)
    print(f"{Cores.VERDE}\nContato adicionado com sucesso!{Cores.RESET}")

def listar_contatos():
    if not contatos:
        print(f"{Cores.VERMELHO}\nNenhum contato na agenda.{Cores.RESET}")
        return
    for i, contato in enumerate(contatos):
        favorito = " (Favorito)" if contato["favorito"] else ""
        print(f"{i + 1}. {contato['nome']} - {contato['telefone']} - {contato['email']}{favorito}")

def editar_contato():
    listar_contatos()
    if not contatos:
        return
    indice = int(input("\nDigite o número do contato que deseja editar: ")) - 1
    if 0 <= indice < len(contatos):
        nome = input("Novo nome (deixe em branco para manter o atual): ")
        telefone = input("Novo telefone (deixe em branco para manter o atual): ")
        email = input("Novo email (deixe em branco para manter o atual): ")
        if nome:
            contatos[indice]["nome"] = nome
        if telefone:
            contatos[indice]["telefone"] = telefone
        if email:
            contatos[indice]["email"] = email
        print(f"{Cores.VERDE}\nContato atualizado com sucesso!{Cores.RESET}")
    else:
        print(f"{Cores.VERMELHO}\nContato inválido.{Cores.RESET}")

def favoritar_contato():
    listar_contatos()
    if not contatos:
        return
    indice = int(input("\nDigite o número do contato que deseja favoritar: ")) - 1
    if 0 <= indice < len(contatos):
        contatos[indice]["favorito"] = True
        print(f"{Cores.AMARELO}\nContato favoritado com sucesso!{Cores.RESET}")
    else:
        print(f"{Cores.VERMELHO}\nContato inválido.{Cores.RESET}")

def remover_favorito():
    listar_favoritos()
    favoritos = [c for c in contatos if c["favorito"]]
    if not favoritos:
        return
    indice = int(input("\nDigite o número do contato favorito que deseja remover: ")) - 1
    if 0 <= indice < len(favoritos):
        favoritos[indice]["favorito"] = False
        print(f"{Cores.VERDE}\nContato removido dos favoritos com sucesso!{Cores.RESET}")
    else:
        print(f"{Cores.VERMELHO}\nContato inválido.{Cores.RESET}")

def listar_favoritos():
    favoritos = [c for c in contatos if c["favorito"]]
    if not favoritos:
        print(f"{Cores.VERMELHO}\nNenhum contato favorito.{Cores.RESET}")
        return
    for i, contato in enumerate(favoritos):
        print(f"{i + 1}. {contato['nome']} - {contato['telefone']} - {contato['email']} (Favorito)")

def apagar_contato():
    listar_contatos()
    if not contatos:
        return
    indice = int(input("Digite o número do contato que deseja apagar: ")) - 1
    if 0 <= indice < len(contatos):
        contatos.pop(indice)
        print(f"{Cores.VERDE}\nContato apagado com sucesso!{Cores.RESET}")
    else:
        print(f"{Cores.VERMELHO}\nContato inválido.{Cores.RESET}")

contatos = []
while True:
    print(f"{Cores.TITULO}\nAplicativo Agenda de Contatos{Cores.RESET}")
    print("\n1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Editar contato")
    print("4 - Favoritar contato")
    print("5 - Remover favorito")
    print("6 - Listar contatos favoritos")
    print("7 - Apagar contato")
    print("8 - Sair")

    opcao = input("\nEscolha uma opção: ")
    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        editar_contato()
    elif opcao == "4":
        favoritar_contato()
    elif opcao == "5":
        remover_favorito()
    elif opcao == "6":
        listar_favoritos()
    elif opcao == "7":
        apagar_contato()
    elif opcao == "8":
        print(f"{Cores.VERMELHO}\nSaindo do aplicativo...{Cores.RESET}")
        break
    else:
        print(f"{Cores.VERMELHO}\nOpção inválida. Tente novamente.{Cores.RESET}")
