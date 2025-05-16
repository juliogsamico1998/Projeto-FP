import os
import random
from funcoes_projeto_fp import *
os.system('clear')
print('WOD TRACKER')
print('Funções para uso:\n1-Criar o treino\n2-visualizar\n3-editar\n4-excluir\n5-filtrar\n6-adição de metas\n7-vizualizar metas / atualizar\n8-adicionar algo\n9-nivelamento\n')
print('Digite 0 para encerrar o programa\n')
while True:
    try:
        opcao = int(input('\nDigite a opção de operação a ser realizada (0 para sair): '))
        if opcao == 0:
            print("Encerrando o programa. Até mais!")
            break
        elif opcao == 1:
            criacao_de_treino()
        elif opcao == 2:
            visualizacao_do_arquivo()
        elif opcao == 3:
            edicao_do_conteudo()
        elif opcao == 4:
            excluir_conteudo()
        elif opcao == 5:
            filtrar_conteudo()
        elif opcao == 6:
            adicionar_metas()
        elif opcao == 7:
            atualizar_e_ver_metas()
        elif opcao == 8:
            adicionar_conteudo()
        elif opcao == 9:
            proficiencia_nivelamento_conteudo() 
        else:
            print("Opção inválida, tente outra opção.")
    except ValueError:
        print("Erro: Digite um número inteiro válido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado durante a execução: {e}")


sorte=random.randint(1,3)
if sorte==1:
    print('\nTREINO ALTERNATIVO:\nAMRAP 12 minutos\n10-Burpees\n15-Kettlebell Swings\n20-Wall Balls')
elif sorte==2:
    print('\nTREINO ALTERNATIVO:\n5 Rounds for Time\n5-Deadlifts\n10-Handstand Push-ups\n20-Wall Balls')
else:
    print('\nTREINO ALTERNATIVO:\nEMOM por 10 minutos\nMinutos ímpares:12-Thrusters\nMinutos pares:10-Toes to Bar')