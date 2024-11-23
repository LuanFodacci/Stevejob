def resumo():
    mensagem = "Steve Jobs foi um empresário e inventor norte-americano, cofundador da Apple Inc."
    return mensagem


def doutorado():
    mensagem = "Steve Jobs não possuia doutorado."
    return mensagem


def contribuicoes():
    mensagem = "Steve Jobs fez contribuições significativas para a ciência da computação, incluindo a popularização da Interface Gráfica de Usuário (GUI) e o Mouse, o foco no Design e Experiência do Usuário, a Inovação em Hardware e Software Integrados, a Revolução da Computação Móvel com o iPhone, a criação da App Store e Economia de Aplicativos, a Transformação do Computador Pessoal, o impacto na Tecnologia no Entretenimento e Multimídia, a inovação com o iPad e Computação Pessoal Portátil, e o estabelecimento de uma Cultura de Inovação e Empreendedorismo na Apple."
    return mensagem


def artigos():
    mensagem = "Alguns artigos de Steve Jobs: \nThe innovation Secrets of Steve Jobs (2001) \nSteve Jobs: The Man Who Thinks Different (2001) \nSteve Jobs: a Biografia (2011) "
    return mensagem


def citacoes():
    mensagem = "3 Citações importantes de Steve Jobs são: \nYour work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. - Stanford Commencement Address (2005) \nDesign is not just what it looks like and feels like. Design is how it works. - Apple Press Release (1997) \nInnovation is what distinguishes a leader from a follower. - The Innovation Secrets of Steve Jobs (2001)"
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
