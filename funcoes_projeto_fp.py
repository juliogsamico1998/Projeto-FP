def criacao_de_treino():
    try:    
        print('\n')
        arquivo=open('treino.txt','a')
        treino=input('Digite o tipo do treino: ')
        arquivo.write('Tipo de treino: '+treino+"\n")
        data=input('Digite a data de início do treino: ')
        arquivo.write('Data de termino: '+data+"\n")
        tempo_de_duracao=input('Digite o tempo de duração do treino em minutos: ')
        arquivo.write('tempo de duração: '+tempo_de_duracao+"\n")
        quantidade_de_exercícios=int(input('Digite quantos exercícios terá o seu treino: '))
        for i in range(quantidade_de_exercícios):
            exercicios=input('Digite o exercício e a faixa de repetições: ')
            arquivo.write(exercicios+'\n')
        arquivo.write('\n')
        arquivo.close()
    except ValueError:
        print("Erro: Digite um número válido para a quantidade de exercícios.")
    except Exception as e:
        print(f"Erro ao criar treino: {e}")

def visualizacao_do_arquivo():
    print('\n')
    try:
        arquivo = open('treino.txt', 'r')
        print(arquivo.read())
        arquivo.close()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")

def edicao_do_conteudo():
    print('\n')
    try:
        with open('treino.txt', 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

        treinos = conteudo.strip().split('\n\n')

        tipo_procurado = input("Digite o nome (tipo) do treino que deseja editar: ").strip().lower()

        encontrado = False
        for i, bloco in enumerate(treinos):
            if f"tipo de treino: {tipo_procurado}" in bloco.lower():
                print("\nTreino encontrado:")
                print(bloco)

                confirmar = input("\nDeseja editar esse treino? (sim/não): ").strip().lower()
                if confirmar == 'sim':
                    print("\nDigite o novo conteúdo para este treino (linha por linha):")
                    novo_tipo = input("Novo tipo de treino: ")
                    nova_data = input("Nova data de término: ")
                    novo_tempo = input("Novo tempo de duração (minutos): ")
                    nova_qtd_exercicios = int(input("Quantos exercícios terá esse treino: "))
                    
                    novos_exercicios = []
                    for j in range(nova_qtd_exercicios):
                        ex = input(f"Exercício {j+1} e faixa de repetições: ")
                        novos_exercicios.append(ex)

                    novo_bloco = (
                        f"Tipo de treino: {novo_tipo}\n"
                        f"Data de termino: {nova_data}\n"
                        f"tempo de duração: {novo_tempo}\n"
                        + '\n'.join(novos_exercicios)
                    )

                    treinos[i] = novo_bloco
                    encontrado = True
                    break
                else:
                    print("Edição cancelada.")
                    return

        if encontrado:
            with open('treino.txt', 'w', encoding='utf-8') as arquivo:
                arquivo.write('\n\n'.join(treinos).strip() + '\n\n')
            print("\nTreino atualizado com sucesso.")
        else:
            print("Treino com esse nome não encontrado.")

    except ValueError:
        print("Erro: Entrada numérica inválida para quantidade de exercícios.")
    except FileNotFoundError:
        print("Erro: Arquivo 'treino.txt' não encontrado.")
    except Exception as e:
        print(f"Erro inesperado na edição: {e}")
    
def excluir_conteudo():
    print('\n')
    try:
        termo = input('Digite o termo que deseja buscar para excluir (tipo, data, exercício, etc): ').strip().lower()
        with open('treino.txt', 'r') as arquivo:
            conteudo = arquivo.read()
        treinos = conteudo.strip().split("\n\n")  # Divide o conteúdo em blocos
        encontrados = [treino for treino in treinos if termo in treino.lower()]
        if encontrados:
            print("\nBlocos encontrados para exclusão:")
        for treino in encontrados:
            print(f"\n{treino}")
        confirmar = input("\nDeseja realmente excluir esses blocos? (sim/não): ").strip().lower()
        if confirmar == 'sim':
            treinos_restantes = [treino for treino in treinos if termo not in treino.lower()]
            with open('treino.txt', 'w') as arquivo:
                arquivo.write('\n\n'.join(treinos_restantes).strip())
                print("\nBlocos excluídos com sucesso.")
        else:
            print("Nenhum treino encontrado com esse termo.")
    except FileNotFoundError:
        print("Arquivo 'treino.txt' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar a exclusão: {e}")

def adicionar_conteudo():
    print('\n')
    try:
        arquivo = open('treino.txt', 'a')
        adicionar_elemento = input('Digite algo que você gostaria de adicionar: ')
        arquivo.write('\n\n'+adicionar_elemento + '\n')
        arquivo.close()
    except Exception as e:
        print(f"Erro ao adicionar conteúdo: {e}")


def filtrar_conteudo():
    print('\n')
    try:
        termo = input('Digite o termo que deseja buscar (tipo, data, exercício, etc): ').strip().lower()
        arquivo = open('treino.txt', 'r')
        conteudo = arquivo.read()
        arquivo.close()
        treinos = conteudo.split("\n\n")
        encontrados = [treino.strip() for treino in treinos if termo in treino.lower()]
        if encontrados:
            print("\nResultados encontrados:")
            for treino in encontrados:
                print(f"\n{treino}")
        else:
            print("Nenhum treino encontrado com esse termo.")
    except FileNotFoundError:
        print("Arquivo não encontrado ou não existente")
    except Exception as e:
        print(f"Erro ao filtrar conteúdo: {e}")

def adicionar_metas():
    print('\n')
    try:
        quantidade_de_metas = int(input('Digite a quantidade de metas que você deseja adicionar: '))
        if quantidade_de_metas <= 0:
            print("A quantidade de metas deve ser um número positivo.")
        else:
            with open('metas.txt', 'a') as arquivo:
                for i in range(quantidade_de_metas):
                    inserir_meta = input(f'Digite a sua meta #{i + 1} para o treino: ').strip()
                    if inserir_meta:
                        linha = f'inconcluído / {inserir_meta} - número da meta {i + 1}\n\n'
                        arquivo.write(linha)
                    else:
                        print(f"Meta #{i + 1} foi ignorada porque estava vazia.")
        print("\nMetas adicionadas com sucesso.")

    except ValueError:
        print("Erro: Digite um número inteiro válido para a quantidade de metas.")
    except FileNotFoundError:
        print("Erro: O arquivo 'metas.txt' não pôde ser encontrado ou criado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


def atualizar_e_ver_metas():
    print('\n')
    try:
        try:
            arquivo = open('metas.txt', 'r')
            conteudo = arquivo.read()
            arquivo.close()
        except FileNotFoundError:
            print("Erro: O arquivo 'metas.txt' não foi encontrado.")
            return

        print(conteudo)

        try:
            print('\n')
            decisao_para_marcar_conclusao = input('Se você concluiu alguma meta digite sim, caso contrário digite não: ')
            if decisao_para_marcar_conclusao == 'sim':
                metas = conteudo.split('\n\n')
                try:
                    selecao = int(input('Digite o número da meta que foi concluída (o número da meta está no final da meta): '))
                    conclusao_de_meta = metas[selecao - 1]
                    edicao = conclusao_de_meta.split()
                    edicao.pop(0)
                    edicao.insert(0, 'concluido')
                    meta_concluida = (' '.join(edicao))
                    metas.pop(selecao - 1)
                    metas.insert(selecao - 1, meta_concluida)
                    final = ('\n\n'.join(metas))
                    with open('metas.txt', 'w') as file:
                        file.write(final)
                except ValueError:
                    print("Erro: Digite um número válido para selecionar a meta.")
                except IndexError:
                    print("Erro: O número informado não corresponde a nenhuma meta.")
        except Exception as e:
            print(f"Ocorreu um erro ao processar a decisão: {e}")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def proficiencia_nivelamento_conteudo():
    try:
        termo = "concluido"
        arquivo = open('metas.txt', 'r')
        conteudo = arquivo.read()
        arquivo.close()
        treinos = conteudo.split("\n\n")
        encontrados = [treino.strip() for treino in treinos if termo in treino.lower()]       
        meta = len(treinos)
        feito = len(encontrados)
        if encontrados:
            resultado = (feito / (meta-1))* 100 
            if resultado>=80:
                print("parabens, o seu nivel é avançado.")
            elif 80>resultado>=50:
                print("o seu nivel é bom.")
            elif 50>feito>=20:
                print("o seu nivel é baixo!")
            else:
                print("melhore!")
    except FileNotFoundError:
        print("Arquivo não encontrado ou não existente")
    except Exception as e:
        print(f"Erro ao filtrar conteúdo: {e}")
