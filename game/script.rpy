define nome = ""
define escolha = ""
define prota = ""
image pink = "#ec1ef3"

# podemos definir os personagens como variáveis
# isso pode facilitar a escrita
define g = Character('Crowly Redraven', color="#789DBC")
define p = Character("[nome]", color="#F6EFBD")
define pri = Character('principe',color="#e7d93c")
define pro = Character('Kea Evenwood',color="#f04b69")

# imagens dos personagens ~~~~~~
image Personagem1:
    "personagem 1"
    zoom 0.433

image Personagem2:
    "personagem 2"
    zoom 0.75

image Personagem3:
    "personagem 3 2"
    zoom 0.64

image Prota:
    "personagem [escolha]"

# imagens dos fundos ~~~~~~~~~~~
image BgCastelo:
    "bg castelo"
    zoom 4

screen escolha_personagem:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.27
        ypos 0.5
        idle "Personagem1"
        action [SetVariable("escolha", "1"), Jump("inicio")]

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        idle "Personagem2"
        action [SetVariable("escolha", "2"), Jump("inicio")]

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.75
        ypos 0.5
        idle "Personagem3"
        action [SetVariable("escolha", "3 2"), Jump("inicio")]

# label: dá o nome a um lugar do programa
# label start: é o que roda quando o jogador inicia o jogo
label start:
    scene pink

    # menu:
    #     "proceso de criacao":
    #         jump criacao
    #     "jogar":

    call screen escolha_personagem

    label inicio:

        $ nome = renpy.input("Qual é o seu nome?")

        scene BgCastelo
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

        show Prota

        p "Oi, eu sou protagonista"

        hide Prota
        with fade

        show Prota

        "Escolha uma das proximas opições"

        menu:
            # comando que representa uma escolha do jogador
            "foge para o jardim": # primeira opcção
                jump opcao_1
                # jump: após essa escolha, pula para outra parte

            "esperar o guarda": # segunda opção
                jump opcao_2

    label opcao_2:
        # vai para a opção escolhida
        p "esperar"
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
            "coperar":
                scene
                p""
                #dialogo
                menu:
                    "continuar coperando":
                        scene
                        #dialogo
                        jump fim_principe
                    "arrogante":
                        scene
                        #dialogo
                        jump final_prometida

    label opcao_1:
        p "foge jardim"
        menu:
            "fugir do castelo":
                show guarda
                g "DIALOG"
                jump fim_comum
            "falar com a moça":
                pro "dialogo"
                p "g"
                pro"d"
                scene ycfg 
                pri "feitico"
                scene kjjhj
                jump final_prometida
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
        scene
        "GAME OVER! :D"
        "VOCÊ MORREU"
        jump creditos
        return
    label criacao:
        scene
        jump creditos
        return
    label final_prometida:
        scene
        ""
        #narador dialoge gigant
        jump creditos
        return
    label fim_principe:
        scene
        ""
        jump creditos
        #dialogo infinito
        return
    label fim_guarda:
        scene
        ""
        jump creditos
        #dialogo infinito
        return
    return
    # termina o jogo

label creditos:
    scene black
    show screen cena_creditos
    pause 100
    hide screen cena_creditos
    return

screen cena_creditos:
    vbox:
        xsize 1000
        ysize 5500
        xalign 0.5
        yalign 0.0
        at transform:
            subpixel True
            easein 100:
                yalign 1.0
        vbox:
            ysize 720
            text ""
            text "Titulo":
                color "#ffffff"
                size 100
                xalign 0.5
                bold True 
            text "Nomes":
                color "#ffffff"
                size 50
                xalign 0.5