# Programa que tenha uma função notas() que pode receber várias notas de alunos
# Vai retornar um dicionário com as seguintes informações:
# a) Quantidade de notas
# b) A maior nota
# c) A menor nota
# d) A média da turma
# e) A situação (opcional)
# Adicione também as docstrings da função

def notas(*nota, sit = False):
    """
    -> Função para analisar notas e situação de alunos
    :param nota: Uma ou mais nota dos alunos (aceita várias)
    :param sit: valor booleano opcional, informa a situação da turma
    :return: dicionário com várias informações sobre a situação da turma
    """
    aluno = dict()
    aluno['quantidade'] = len(nota)

    aluno['maior'] = max(nota)

    aluno['menor'] = min(nota)

    aluno['media'] = sum(nota) / len(nota)

    if sit:
        if aluno['media'] > 7:
            aluno['situação'] = 'Boa'
        elif aluno['media'] > 5:
            aluno['situação'] = 'Regular'
        else:
            aluno['situação'] = 'Ruim'

    return aluno


resposta = notas(1)
print(resposta)
