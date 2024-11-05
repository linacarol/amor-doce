# podemos definir os personagens como variáveis
# isso pode facilitar a escrita
define g = Character('Guarda', color="#789DBC")
define p = Character('Protagonista', color="#F6EFBD")

# label: dá o nome a um lugar do programa
# label start: é o que roda quando o jogador inicia o jogo
label start:
    scene bg castelo
    # scene: limpa todas as imagens e mostra a imagem de fundo
    # bg castelo: nome da imagem na pasta images

    show guarda
    # show: comando para exibir alguma imagem
    # guarda: nome da imagem que está na pasta images

    g "Oi, eu sou o guarda"
    # g: nome da variável do personagem que está falando
        # podemos digitar uma string também, entre aspas
    # "Oi, eu sou o guarda": fala do personagem

    hide guarda
    # hide: esconde a imagem
    with fade
    # transição para esconder a imagem

    show protagonista

    p "Oi, eu sou protagonista"

    hide protagonista
    with fade

    show guarda

    g "Escolha uma opcao"

    menu:
        # comando que representa uma escolha do jogador
        "Opcao boa": # primeira opcção
            jump opcao_boa
            # jump: após essa escolha, pula para outra parte

        "Opcao ruim": # segunda opção
            jump opcao_ruim
    
    label opcao_boa:
        # vai para a opção escolhida
        "Resposta boa"
        jump fim_comum
    
    label opcao_ruim:
        "Resposta ruim"
        jump fim_comum
    
    label fim_comum:
        "Cabou!! :D"
    
    return
    # termina o jogo