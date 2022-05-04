import sqlite3

def criaClienteTable():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE clientes (
        cpf	VARCHAR(11) NOT NULL,
        nome TEXT NOT NULL,
        fone TEXT,
        plano TEXT NOT NULL
    );
    """)
    print('Tabela criada com sucesso.')
    conn.close()
    return conn

def insereCliente(cpf,nome,fone,plano):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO clientes (cpf, nome, fone, plano)
    VALUES (?,?,?,?)
    """,(cpf,nome,fone,plano,))
    # gravando no bd
    conn.commit()
    print('Dados inseridos com sucesso.')
    conn.close()

def atualizaCliente(cpf,nome,fone,plano):
    conn = sqlite3.connect('clientes.db')  
    cursor = conn.cursor()
    # alterando os dados da tabela
    cursor.execute("""
    UPDATE clientes
    SET nome = ?, fone = ?, plano = ?
    WHERE cpf = ?
    """, (nome,fone,plano,cpf,))
    conn.commit()
    print('Dados atualizados com sucesso.')
    conn.close()

def deleteCliente(cpf):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM clientes
    WHERE cpf = ?
    """, (cpf,))
    conn.commit()
    print('Registro excluido com sucesso.')
    conn.close()


def criaAlugawelTable():
    conn = sqlite3.connect('aluguel.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE aluguel (
        idEmprestimo	TEXT NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        IdExemplar TEXT,
        DataIni TEXT NOT NULL,
        DataFin	TEXT NOT NULL,
        Funcionario TEXT NOT NULL
    );
    """)
    print('Tabela criada com sucesso.')
    conn.close()
    return conn

def insereAlugawel(a,b,c,d,e):
    conn = sqlite3.connect('aluguel.db')
    cursor = conn.cursor()
    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO aluguel (idEmprestimo,cpf , IdExemplar, DataIni,DataFin,Funcionario )
    VALUES (?,?,?,?,?,?)
    """,(a,b,c,d,e,))
    # gravando no bd
    conn.commit()
    print('Dados inseridos com sucesso.')
    conn.close()

def atualizaAlugawel(a,b,c,d,e):  
    conn = sqlite3.connect('aluguel.db')
    cursor = conn.cursor()
    # alterando os dados da tabela
    cursor.execute("""
    UPDATE aluguel
    SET cpf = ?, IdExemplar = ?,DataIni = ?, DataFin = ?, Funcionario = ?
    WHERE idEmprestimo = ?
    """, (b,c,d,e,a,))
    conn.commit()
    print('Dados atualizados com sucesso.')
    conn.close()

def deleteAlugawel(a):
    conn = sqlite3.connect('aluguel.db')
    cursor = conn.cursor()
    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM aluguel
    WHERE idEmprestimo = ?
    """, (a,))
    conn.commit()
    print('Registro excluido com sucesso.')
    conn.close()



def criaCopiaTable():
    conn = sqlite3.connect('unidadeJogo.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE unidadeJogo (
        IdExemplar TEXT,
        IdJogo TEXT NOT NULL,
        Disponibilidade	INTEGER NOT NULL
    );
    """)
    print('Tabela criada com sucesso.')
    conn.close()
    return conn

def insereCopia(a,b,c):
    conn = sqlite3.connect('unidadeJogo.db')
    cursor = conn.cursor()
    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO unidadeJogo (IdExemplar,IdJogo , Disponibilidade)
    VALUES (?,?,?)
    """,(a,b,c,))
    # gravando no bd
    conn.commit()
    print('Dados inseridos com sucesso.')
    conn.close()

def atualizaCopia(a,b,c):  
    conn = sqlite3.connect('unidadeJogo.db')
    cursor = conn.cursor()
    # alterando os dados da tabela
    cursor.execute("""
    UPDATE unidadeJogo
    SET IdJogo = ?, Disponibilidade = ?
    WHERE IdExemplar = ?
    """, (b,c,a,))
    conn.commit()
    print('Dados atualizados com sucesso.')
    conn.close()

def deleteCopia(a):
    conn = sqlite3.connect('unidadeJogo.db')
    cursor = conn.cursor()
    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM unidadeJogo
    WHERE IdExemplar = ?
    """, (a,))
    conn.commit()
    print('Registro excluido com sucesso.')
    conn.close()



def criaJogoTable():
    conn = sqlite3.connect('jogo.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE jogo (
        IdJogo TEXT,
        Desenvolvedora TEXT NOT NULL,
        Plataforma TEXT NOT NULL,
        Genero TEXT NOT NULL,
        Lancamento TEXT NOT NULL,
        FaixaEtaria TEXT NOT NULL,
        ExemplaresDisponiveis INTEGER NOT NULL,
        Preco	INTEGER NOT NULL
    );
    """)
    print('Tabela criada com sucesso.')
    conn.close()
    return conn

def insereJogo(a,b,c,d,e,f,g,h):
    conn = sqlite3.connect('jogo.db')
    cursor = conn.cursor()
    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO jogo (IdJogo,Desenvolvedora , Plataforma,Genero,Lancamento,FaixaEtaria,ExemplaresDisponiveis,Preco)
    VALUES (?,?,?,?,?,?,?,?)
    """,(a,b,c,d,e,f,g,h,))
    # gravando no bd
    conn.commit()
    print('Dados inseridos com sucesso.')
    conn.close()

def atualizaJogo(a,b,c,d,e,f,g,h):  
    conn = sqlite3.connect('jogo.db')
    cursor = conn.cursor()
    # alterando os dados da tabela
    cursor.execute("""
    UPDATE jogo
    SET Desenvolvedora = ?, Plataforma = ?, Genero = ?, Lancamento = ?, FaixaEtaria = ?, ExemplaresDisponiveis = ?, Preco = ?
    WHERE IdJogo = ?
    """, (b,c,d,e,f,g,h,a,))
    conn.commit()
    print('Dados atualizados com sucesso.')
    conn.close()

def deleteJogo(a):
    conn = sqlite3.connect('jogo.db')
    cursor = conn.cursor()
    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM jogo
    WHERE IdJogo = ?
    """, (a,))
    conn.commit()
    print('Registro excluido com sucesso.')
    conn.close()


def leituraCliente(conn,cpf):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes WHERE cpf = ? ", (cpf,))
    c = cursor.fetchall()
    for row in c:
        print (row)
    conn.close()
    return row


def leTudoClientes(conn):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM clientes;
    """)
    for linha in cursor.fetchall():
        print(linha)
    conn.close()


#testes
#conn = sqlite3.connect('clientes.db')
#leTudoClientes(conn)
conn = sqlite3.connect('clientes.db')
#a = leituraOne(conn,'nome','22222')
#print(a)
conn = sqlite3.connect('clientes.db')
a=leituraCliente(conn,'22222')
print(a[1])



