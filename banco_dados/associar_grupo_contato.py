from bd import nova_conexao
from mysql.connector.errors import ProgrammingError


selecionar_grupo = 'select id from grupos where descricao = %s'
atualizar_contato = 'update contatos set grupo_id = %s where nome = %s'

contato_grupo = {
    'Luan': 'Casa',
    'Lara': 'Trabalho',
    'Maria': 'Casa',
    'João': 'Casa',
    'Otávio': 'Trabalho',
    'Bia': 'Trabalho'
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato, (grupo_id,contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('Contatos associados')