import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        conexao.close()

#Insere varios registros na base de dados
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#               '(%s, %s, %s, %s)'
#         dados = [
#             ('Muriel', 'Figueredo', 19, 55),
#             ('Rose', 'Figueredo', 19, 55),
#             ('Jose', 'Figueredo', 19, 55),
#         ]
#         cursor.executemany(sql, dados)
#         conexao.commit()

#Deleta uma linha cujo o nome seja o selecionado

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE nome=%s'
#         cursor.execute(sql, ('Jack',))
#         conexao.commit()

#Deleta uma linha cujo o id esteja entre os selecionados

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (11,12, 13))
#         conexao.commit()

#Deleta uma linha cujo o id esteja entre os selecionados

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (18, 19))
#         conexao.commit()

#Modifica um registro mudando o nome baseado no ID

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('Joana', 5))
        conexao.commit()

#Mostra os dados registrados até o momento

with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)