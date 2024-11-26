define nome = ""
define escolha = ""
define prota = ""
image cor = "#cbecff"

# podemos definir os personagens como variáveis
# isso pode facilitar a escrita
define g = Character('Crowly Redraven', color="#789DBC")
define p = Character("[nome]", color="#F6EFBD")
define pri = Character('principe',color="#e7d93c")
define pro = Character('Lina Slytherin',color="#f04b69")

# imagens dos personagens ~~~~~~
image Escolha1:
    "escolha1"
    zoom 0.7

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

image Pro:
    "prometida"
    zoom 1.0

image Pri:
    "principe"
    zoom 1.0

image Guarda:
    "guarda"
    yanchor 0.5
    ypos 0.2
    zoom 1.0

# imagens dos fundos ~~~~~~~~~~~
image BgCastelo:
    "bg castelo"
    zoom 4

screen escolha_personagem:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.22
        ypos 0.5
        idle "Escolha1"
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
    scene cor

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

        show Guarda at left
        # show: comando para exibir alguma imagem
        # guarda: nome da imagem que está na pasta images

        g "Quem esta ai?! Quem é você?!"

        hide guarda
        show Prota at right
        p "E-eu... O-O que?.... *Desmaia*"
        hide Prota
        "*Você é levada para a sala do trono*"
        show Prota at right
        p "*Acorda na  cela*"
        hide Prota

        menu:
            # comando que representa uma escolha do jogador
            "foge para o jardim": # primeira opcção
                jump opcao_1
                # jump: após essa escolha, pula para outra parte

            "Esperar por alguém": # segunda opção
                jump opcao_2

    label opcao_2:
        # vai para a opção escolhida
        show Guarda at left
        pause 50

        show Prota at right
        p "Você! Onde eu estou?!"
        show Guarda at left
        g "Calada! Você sera levada para o principe, você entendeu?"

        menu:
            "Tretar":
                "*Você é jogada de volta na cela pelo guarda*"
                g "Qual o seu problema?!"
                hide Guarda
                show Prota at right
                p "Qual é o seu problema?! Quem é vc?! Onde eu to?!"
                hide Prota
                show Guarda at left
                g "Qual o meu problema?! Qual o seu problema?! Eu não vou arriscar uma doida igual você de frente ao rei!"
                hide Guarda
                with fade
                ""
                menu:
                    "mentir":
                        #dialogo
                        scene
                        jump fim_comum
                    "verdadeira":
                        #dialogo
                        scene
                        jump fim_guarda
            "Cooperar":

                "*Você é levada para a sala do trono*"
                g "Senhor, senhora. *Referencia*"
                hide Guarda
                show Pri at left
                pause 50
                hide Pri
                show Pro at left
                pause 50
                hide Pro

                show Pri at left
                pri "Então vc é a pessoa que causou aquela bagunça? Os alarmes soaram por sua causa, sabia?"

                menu:
                    "Continuar cooperando":
                        show Prota at right 
                        p "Não, senhor... Eu não sei como vim parar aqui"
                        hide Prota
                        show Pri at left
                        pri "Não sabe? Huh..."
                        hide Pri
                        show pro at left
                        pro "Meu amor, deveriamos lançar um feitiço da verdade nela e tomarmos nossa decisão a partir dai"
                        hide pro
                        show Pri at left
                        pri "Ah.... Sim, vc tem razão"
                        "*Ele ergue o braço e casta o feitiço ao seu redor*"
                        hide Pri
                        show pro at left
                        pro "Viu? Ela esta falando a verdade..."
                        hide pro
                        show Pri at left
                        pri "É o que parece..."
                        hide Pri
                        show Prota at right
                        p "Senhor... Teria um lugar aonde eu possa ficar a noite?"
                        hide Prota
                        show Pri at left
                        pri "Sim, fique aqui... Já que você apareceu em meu reino a responsabilidade é minha."

                        jump fim_principe
                    "arrogante":
                        scene
                        #dialogo
                        jump final_prometida

    label opcao_1:
        p "foge jardim"
        menu:
            "fugir do castelo":
                show Guarda at left
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

    label final_prometida:
        scene
        "A prometida e ela conversam entre si e entendem que têm muito em comum."
        "Se passam um ou dois dias e elas fogem juntas, pois a sociedade não aceitará seu amor."
        "Elas fogem para uma vila distante, onde vivem felizes e confortáveis juntas, como deve ser."
        jump creditos
        return
    label fim_principe:
        scene
        "Ela permanece no castelo por um tempo e eles começam a se aproximar"
        "Após meses, eles entenderam que sentiam algo a mais"
        "O príncipe a levou para o jardim e pediu em casamento"
        "E eles viveram felizes para sempre"
        jump creditos
        return
    label fim_guarda:
        scene
        "Após ela ficar aos seus cuidados, eles começam a passar muito tempo juntos"
        "A partir de um tempo, eles criam sentimentos que florescem cada vez mais"
        "Certo dia, em uma manhã insolarada, o guarda Crowly Redraven a pede em casamento"
        "E eles vivem felizes por muitos e muitos anos"
        jump creditos
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
            text "Um agradecimento a todos do Projeto Olá Mundos por ajudarem tanto":
                color "#ffffff"
                size 100
                xalign 0.5
                bold True 
            text "especialmente para nossa especial professora Lina":
                color "#ffffff"
                size 100
                xalign 0.5
                bold True
            text "e a nós criadores, Carla Lima Camilo e Noah Alfonso Garcia":
                color "#ffffff"
                size 100
                xalign 0.5
                bold True 
            text "Fonte das imagens: internet":
                color "#ffffff"
                size 100
                xalign 0.5
                bold True