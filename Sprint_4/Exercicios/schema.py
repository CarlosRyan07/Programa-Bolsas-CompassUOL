import os


def criar_estrutura():
    """
    Desenvolvido para facilitar a criação de um projeto
    com base no schema.
    :param:
    :return:
    """
    try:
        with open('relatorio.md', 'w') as r:
            pass
        os.makedirs('secao_2', exist_ok=True)
        os.makedirs('secao_3', exist_ok=True)
        for i in range(1, 8):
            with open(f'secao_2/ex_{i}.py', 'w') as a:
                pass
        os.makedirs('secao_3/tarefa_1', exist_ok=True)
        os.makedirs('secao_3/tarefa_3', exist_ok=True)
        with open('secao_3/tarefa_1/carguru.py', 'w') as a:
            pass
        with open('secao_3/tarefa_1/Dockerfile', 'w') as a:
            pass
        with open('secao_3/tarefa_3/script.py', 'w') as a:
            pass
        print("criada com sucesso!")
    except Exception as e:
        print(f"PROBLEMA!!! : {e}")


if __name__ == "__main__":
    criar_estrutura()