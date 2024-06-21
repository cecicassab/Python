from bd import nova_conexao
from mysql.connector.errors import ProgrammingError


sql = """
    select
        grupo.descricao as grupo
        contatos.nome as contato
    from contatos
    inner join grupos on contatos.grupo_id = grupos.id
    order by grupo,contato
"""
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato["grupo"]}: {contato["contato"]}')