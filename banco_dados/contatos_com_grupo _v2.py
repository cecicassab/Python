from bd import nova_conexao
from mysql.connector.errors import ProgrammingError
from collections import defaultdict


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
        try:
            cursor.execute(sql)
            contatos = cursor.fetchall()
        finally:
            cursor.close()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        agrupados = defaultdict(list)
        for contato in contatos:
            agrupados[contato['grupo']].append(contato['contato'])
            
        print(agrupados)