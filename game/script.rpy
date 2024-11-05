define nome = ""
image pink = "#ec1ef3"

# podemos definir os personagens como variáveis
# isso pode facilitar a escrita
define g = Character('Crowly Redraven', color="#789DBC")
define p1 = Character("[nome]", color="#F6EFBD")
define p2 = Character("[nome]", color="#F6EFBD")
define p3 = Character("[nome]", color="#F6EFBD")
define pri = Character('principe',color="#e7d93c")
define pro = Character('Kea Evenwood',color="#f04b69")

# label: dá o nome a um lugar do programa
# label start: é o que roda quando o jogador inicia o jogo
label start:
    scene pink
    
    $ nome = renpy.input("Qual é o seu nome?")

    scene bg castelo
    # scene: limpa todas as imagens e mostra a imagem de fundo
    # bg castelo: nome da imagem na pasta images

    show guarda
    # show: comando para exibir alguma imagem
    # guarda: nome da imagem que está na pasta images

    g "Quem esta ai?! Quem é você?!"
    # g: nome da variável do personagem que está falando
        # podemos digitar uma string também, entre aspas
    # "Oi, eu sou o guarda": fala do personagem

    hide guarda
    # hide: esconde a imagem
    with fade
    # transição para esconder a imagem

    show protagonista

    p1 "Oi, eu sou protagonista"

    hide protagonista
    with fade
    
    show protagonista

    "Escolha uma opcao"

    menu:
        # comando que representa uma escolha do jogador
        "Opcao boa": # primeira opcção
            jump opcao_boa
            # jump: após essa escolha, pula para outra parte

        "Opcao ruim": # segunda opção
            jump opcao_ruim
    
    label opcao_2:
        # vai para a opção escolhida
        p1 "esperar"
        g""
        p""
        menu:
            "tretar":
                scene
                p""
                #dialogo      
                menu:
                    "mentir":
                        #dialogo
                        scene
                        jump fim_comum
                    "verdadeira":
                        #dialogo
                        scene
                        jump fim_guarda
    label opcao_1:
        p1 "esconder"
        menu:
            "opicao-fugir":
                show guarda
                g "DIALOG"
                jump fim_comum
            "opicao-falar com ela":
                pro "dialogo"
                p "g"
                pro"d"
                scene ycfg 
                pri "feitico"
                scene kjjhj
                menu:
                    "opicao-mentira":
                        p "d" 
                        pro "d"
                        jump fim_comum
                    "opicao-verdade":
                        p ""
                        pro ""
                        #mais dialogo
                        jump final_prometida

               
                



                
        jump fim_comum
    
    label fim_comum:
        "Cabou!! :D"
    
    label final_prometida:
        scene
        ""
        #narador dialoge gigant
    label fim_principe:
        scene
        ""
        #dialogo infinito
    label fim_guarda:
        scene
        ""
        #dialogo infinito
    return
    # termina o jogo