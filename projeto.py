import tkinter as tk
import sqlite3
import pandas as pd

# conexao = sqlite3.connect('locadora_jogo.db')

# c = conexao.cursor()

# c.execute(''' CREATE TABLE CLIENTE (
#     cpf_cliente text,
#     nome text,
#     telefone text
#     )
# ''')

# c.execute(''' CREATE TABLE ALUGUEL (
#     id_emprestimo int,
#     cpf_cliente text,
#     id_exemplar int,
#     data_emprestimo text,
#     data_devolucao text
#     )
# ''')

# c.execute(''' CREATE TABLE JOGO (
#      nome text,
#      id_jogo int,
#      desenvolvedora text,
#      plataforma text,
#      genero text,
#      data_lancamento text,
#      faixa_etaria int,
#      quant_disponivel int,
#      preco text
#      )
#  ''')

# c.execute(''' CREATE TABLE FUNCIONARIO (
#     nome text,
#     cpf_funcionario text,
#     telefone text,
#     data_contratacao text,
#     funcao text
#     )
# ''')

# conexao.commit()

# conexao.close()

def cadastra_cliente(cpf, nome, telefone):

    conexao = sqlite3.connect('locadora_jogo.db')

    c = conexao.cursor()

    c.execute(" INSERT INTO CLIENTE VALUES (:cpf, :nome, :telefone)",
        {
            'cpf':cpf.get(),
            'nome':nome.get(),
            'telefone':telefone.get(),
        }
    )

    conexao.commit()
    print("Cliente Cadastrado com Sucesso")
    conexao.close()

    cpf.delete(0, "end")
    nome.delete(0, "end")
    telefone.delete(0, "end")

def cadastro_jogo(i,a,b,c,d,e,f,g,h):
    conn = sqlite3.connect('locadora_jogo.db')
    cursor = conn.cursor()
    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO JOGO (nome, id_jogo,desenvolvedora, plataforma,genero,data_lancamento,faixa_etaria,quant_disponivel,preco)
    VALUES (?,?,?,?,?,?,?,?,?)
    """,(str(i.get()),int(a.get()),str(b.get()),str(c.get()),str(d.get()),str(e.get()),int(f.get()),int(g.get()),int(h.get()),))
    # gravando no bd
    conn.commit()
    print('Dados inseridos com sucesso.')
    conn.close()

    i.delete(0, "end")
    a.delete(0, "end")
    b.delete(0, "end")
    c.delete(0, "end")
    d.delete(0, "end")
    e.delete(0, "end")
    f.delete(0, "end")
    g.delete(0, "end")
    h.delete(0, "end")

def cadastra_funcionario(cpf, nome, telefone, data_contratacao, funcao):
    

    conexao = sqlite3.connect('locadora_jogo.db')

    c = conexao.cursor()

    c.execute(" INSERT INTO FUNCIONARIO VALUES (:nome, :cpf, :telefone, :data_contratacao, :funcao)",
        {
            'cpf':cpf.get(),
            'nome':nome.get(),
            'telefone':telefone.get(),
            'data_contratacao':data_contratacao.get(),
            'funcao':funcao.get()
        }
    )

    conexao.commit()
    print("Funcionário Cadastrado com Sucesso")
    conexao.close()

    cpf.delete(0, "end")
    nome.delete(0, "end")
    telefone.delete(0, "end")
    data_contratacao.delete(0, "end")
    funcao.delete(0, "end")

def aluga_jogo(a,b,c,d,e):
    conn = sqlite3.connect('locadora_jogo.db')
    cursor = conn.cursor()
    aux= int(c.get())
    print(aux)
    print('debug.')
    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO ALUGUEL (id_emprestimo,cpf_cliente , id_exemplar, data_emprestimo,data_devolucao)
    VALUES (?,?,?,?,?)
    """,(int(a.get()),str(b.get()),int(c.get()),str(d.get()),str(e.get()),))

    cursor.execute("SELECT * FROM JOGO WHERE id_jogo  = ? ", (int(c.get()),))
    c = cursor.fetchall()
    for row in c:
       num = row[7]-1
    # alterando os dados da tabela
    print(num)
    cursor.execute("""
    UPDATE JOGO
    SET quant_disponivel=?
    WHERE id_jogo = ?
    """, (num,aux,))
    conn.commit()
    print('Dados atualizados com sucesso.')
    # gravando no bd
    conn.commit()
    print('Dados inseridos com sucesso.')
    conn.close()

def exporta_nota_cadastro():

    conexao = sqlite3.connect('locadora_jogo.db')

    c = conexao.cursor()

    c.execute("SELECT *, oid FROM CLIENTE")
    clientes_cadastrados = c.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['nome','cpf','telefone','Id_banco'])
    clientes_cadastrados.to_excel('clientes_cadastrados.xlsx')

    conexao.commit()
    print("Base de Clientes cadastrados Importado com Sucesso")
    conexao.close()

def exporta_base_jogos():

    conexao = sqlite3.connect('locadora_jogo.db')

    c = conexao.cursor()

    c.execute("SELECT *, oid FROM JOGO")
    jogos_cadastrados = c.fetchall()
    jogos_cadastrados = pd.DataFrame(jogos_cadastrados, columns=['nome','ID_Jogo','Desenvolvedora','Plataforma', 'Gênero', 'Data_lancamento','Faixa_Etaria', 'Quantidade_disponivel', 'Preço','Id_banco'])
    jogos_cadastrados.to_excel('jogos__cadastrados.xlsx')

    conexao.commit()
    print("Base de Jogos Exportada com Sucesso")
    conexao.close()

def exporta_nota_funcionario():
    conexao = sqlite3.connect('locadora_jogo.db')

    c = conexao.cursor()

    c.execute("SELECT *, oid FROM FUNCIONARIO")
    funcionarios_cadastrados = c.fetchall()
    funcionarios_cadastrados = pd.DataFrame(funcionarios_cadastrados, columns=['Nome','CPF_Funcionario','Telefone', 'Data_de_Contratação', 'Função', 'Id_banco'])
    funcionarios_cadastrados.to_excel('Funcionarios_cadastrados.xlsx')

    conexao.commit()
    print("Base de funcionarios Cadastrados Importada com Sucesso")
    conexao.close()

def exporta_nota_aluguel():
    conexao = sqlite3.connect('locadora_jogo.db')

    c = conexao.cursor()

    c.execute("SELECT *, oid FROM ALUGUEL")
    funcionarios_cadastrados = c.fetchall()
    funcionarios_cadastrados = pd.DataFrame(funcionarios_cadastrados, columns=['ID do Empréstimo','CPF_Cliente','ID do Exemplar', 'Data_Emprestimo', 'Data_Devolução', 'Id_banco'])
    funcionarios_cadastrados.to_excel('jogos_alugados.xlsx')

    conexao.commit()
    print("Base de Jogos Alugados Importada com Sucesso")
    conexao.close()

def mostra_jogo():

    janela = tk.Tk()
    janela.title('Jogos')

    # Labels:
   

    conexao = sqlite3.connect('locadora_jogo.db')
    cursor = conexao.cursor()
    
    sqlite_select_query = """SELECT * from JOGO"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Total de jogos são:  ", len(records))
    print("\n")
    cont = 0
    
    for row in records:
        
        label_nome_jogo = tk.Label(janela, text=row[0])
        label_nome_jogo.grid(row=0, column=cont, padx=10, pady=10)

        label_id_jogo = tk.Label(janela, text=row[1])
        label_id_jogo.grid(row=1, column=cont, padx=10, pady=10)

        label_desenvolvedora = tk.Label(janela, text=row[2])
        label_desenvolvedora.grid(row=2, column=cont, padx=10, pady=10)

        label_plataforma = tk.Label(janela, text=row[3])
        label_plataforma.grid(row=3, column=cont, padx=10, pady=10)

        label_genero = tk.Label(janela, text=row[4])
        label_genero.grid(row=4, column=cont, padx=10, pady=10)

        label_data_lancamento = tk.Label(janela, text=row[5])
        label_data_lancamento.grid(row=5, column=cont, padx=10, pady=10)

        label_faixa_etaria = tk.Label(janela, text=row[6])
        label_faixa_etaria.grid(row=6, column=cont, padx=10, pady=10)

        label_quant_disp = tk.Label(janela, text=row[7])
        label_quant_disp.grid(row=7, column=cont, padx=10, pady=10)

        label_preco = tk.Label(janela, text=row[8])
        label_preco.grid(row=8, column=cont, padx=10, pady=10)
        
        cont = cont + 1
     
    conexao.commit()

    conexao.close()

def visualizar_nota():
    janela = tk.Tk()
    janela.title('Cliente')

    # Labels:
   
    conexao = sqlite3.connect('locadora_jogo.db')
    cursor = conexao.cursor()
    
    sqlite_select_query = """SELECT * from CLIENTE"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
   
    for row in records:
        
        label_nome_jogo = tk.Label(janela, text=row[1])
        label_nome_jogo.grid(row=0, column=0, padx=10, pady=10)

        label_id_jogo = tk.Label(janela, text=row[0])
        label_id_jogo.grid(row=1, column=0, padx=10, pady=10)

        label_desenvolvedora = tk.Label(janela, text=row[2])
        label_desenvolvedora.grid(row=2, column=0, padx=10, pady=10)
        

    conexao.commit()

    conexao.close()

def visualiza_aluguel():
    
    janela = tk.Tk()
    janela.title('Aluguel do cliente')
    
    conexao = sqlite3.connect('locadora_jogo.db')
    cursor = conexao.cursor()
    
    sqlite_select_query = """SELECT * from ALUGUEL"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
           
   
    for row  in records:
        
        
                    label_nome_jogo = tk.Label(janela, text=row[0])
                    label_nome_jogo.grid(row=0, column=0, padx=10, pady=10)

                    label_id_jogo = tk.Label(janela, text=row[1])
                    label_id_jogo.grid(row=1, column=0, padx=10, pady=10)
        
                    label_desenvolvedora = tk.Label(janela, text=row[2])
                    label_desenvolvedora.grid(row=2, column=0, padx=10, pady=10)

                    label_plataforma = tk.Label(janela, text=row[3])
                    label_plataforma.grid(row=3, column=0, padx=10, pady=10)

                    label_genero = tk.Label(janela, text=row[4])
                    label_genero.grid(row=4, column=0, padx=10, pady=10)
                    
                  
    
    conexao.commit()

    conexao.close()

def janela_area_cliente():
    janela = tk.Tk()
    janela.title('Área do Cliente')

    botao = tk.Button(janela, text='Já sou Cliente', command = janela_area_cliente_cadastrado)
    botao.grid(row=0, column=0,columnspan=2, padx=20, pady=20 , ipadx = 40)

    botao = tk.Button(janela, text='Não Sou cliente', command = janela_area_cliente_novo)
    botao.grid(row=1, column=0,columnspan=2, padx=20, pady=20 , ipadx = 40)

    botao_voltar = tk.Button(janela, text='Voltar', command = janela.destroy)
    botao_voltar.grid(row=2, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

def janela_area_cliente_novo():
    janela = tk.Tk()
    janela.title('Área de Registro')

    botao = tk.Button(janela, text='Fazer Cadastro', command = janela_cadastra_cliente)
    botao.grid(row=0, column=0,columnspan=2, padx=20, pady=20 , ipadx = 40)

    botao_voltar = tk.Button(janela, text='Voltar', command = janela.destroy)
    botao_voltar.grid(row=2, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

def janela_area_cliente_cadastrado():
    janela = tk.Tk()
    janela.title('Área do Cliente')

    botao = tk.Button(janela, text='Ver Jogos Disponiveis', command = janela_jogos)
    botao.grid(row=0, column=0,columnspan=2, padx=20, pady=20 , ipadx = 40)

    botao = tk.Button(janela, text='Alugar Jogo', command = janela_aluga_jogo)
    botao.grid(row=1, column=0,columnspan=2, padx=20, pady=20 , ipadx = 40)

    botao_voltar = tk.Button(janela, text='Voltar', command = janela.destroy)
    botao_voltar.grid(row=2, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

def janela_jogos():
    janela = tk.Tk()
    janela.title('Jogos')

    botao_exportar = tk.Button(janela, text='Visualizar jogos Disponíveis', command= mostra_jogo)
    botao_exportar.grid(row=0, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    botao_exportar = tk.Button(janela, text='Exportar Base dos jogos Disponíveis', command= exporta_base_jogos)
    botao_exportar.grid(row=1, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    botao_voltar = tk.Button(janela, text='Voltar', command = janela.destroy)
    botao_voltar.grid(row=3, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

def janela_aluga_jogo():
    janela = tk.Tk()
    janela.title('Aluguel Jogo')

    # Labels:
    label_id_emprestimo = tk.Label(janela, text='ID do Emprestimo')
    label_id_emprestimo.grid(row=0, column=0, padx=10, pady=10)

    label_cpf_cliente = tk.Label(janela, text='CPF Do Cliente')
    label_cpf_cliente.grid(row=1, column=0, padx=10, pady=10)

    label_id_exemplar = tk.Label(janela, text='ID do Exemplar')
    label_id_exemplar.grid(row=2, column=0, padx=10, pady=10)

    label_data_emprestimo = tk.Label(janela, text='Data do Emprestimo')
    label_data_emprestimo.grid(row=3, column=0, padx=10, pady=10)

    label_data_devolucao = tk.Label(janela, text='Data de Devolucao')
    label_data_devolucao.grid(row=4, column=0, padx=10, pady=10)

    # Entrys

    entry_id_emprestimo = tk.Entry(janela, text='ID do Emprestimo')
    entry_id_emprestimo.grid(row=0, column=1, padx=10, pady=10)

    entry_cpf_cliente = tk.Entry(janela, text='CPF do Cliente')
    entry_cpf_cliente.grid(row=1, column=1, padx=10, pady=10)

    entry_id_exemplar = tk.Entry(janela, text='ID do Exemplar')
    entry_id_exemplar.grid(row=2, column=1, padx=10, pady=10)

    entry_data_emprestimo = tk.Entry(janela, text='Data do Emprestimo')
    entry_data_emprestimo.grid(row=3, column=1, padx=10, pady=10)

    entry_data_devolucao = tk.Entry(janela, text='Data de Devolucao')
    entry_data_devolucao.grid(row=4, column=1, padx=10, pady=10)

    # Botões

    botao_alugar = tk.Button(janela, text='Alugar Jogo!', command=lambda: aluga_jogo(entry_id_emprestimo, entry_cpf_cliente, entry_id_exemplar, entry_data_emprestimo, entry_data_devolucao))
    botao_alugar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    botao_exportar = tk.Button(janela, text='Visualizar Aluguel', command= visualiza_aluguel)
    botao_exportar.grid(row=6, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    botao_voltar = tk.Button(janela, text='Voltar', command = janela.destroy)
    botao_voltar.grid(row=7, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

def janela_cadastra_cliente():
    
    janela = tk.Tk()
    janela.title('Cadastro e Aluguel')

    # Labels:
    label_nome = tk.Label(janela, text='Nome')
    label_nome.grid(row=0, column=0, padx=10, pady=10)

    label_cpf = tk.Label(janela, text='CPF')
    label_cpf.grid(row=1, column=0, padx=10, pady=10)

    label_telefone = tk.Label(janela, text='Telefone')
    label_telefone.grid(row=2, column=0, padx=10, pady=10)

    # Entrys

    entry_nome = tk.Entry(janela, text='Nome', width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=10)

    entry_cpf = tk.Entry(janela, text='CPF', width=30)
    entry_cpf.grid(row=1, column=1, padx=10, pady=10)

    entry_telefone = tk.Entry(janela, text='Telefone', width=30)
    entry_telefone.grid(row=2, column=1, padx=10, pady=10)

    # Botões

    botao_alugar = tk.Button(janela, text='Cadastre-se', command=lambda: cadastra_cliente(entry_cpf, entry_nome, entry_telefone))
    botao_alugar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    botao_exportar = tk.Button(janela, text='Visualizar Cadastro', command= visualizar_nota)
    botao_exportar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    botao_voltar = tk.Button(janela, text='Voltar', command = janela.destroy)
    botao_voltar.grid(row=6, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

def janela_area_funcionario():
    janela = tk.Tk()
    janela.title('Área do Funcionário')

    botao = tk.Button(janela, text='Cadastrar Jogo', command = janela_cadastra_jogo)
    botao.grid(row=0, column=0,columnspan=2, padx=20, pady=20 , ipadx = 40)

    botao = tk.Button(janela, text='Cadastrar Funcionário', command = janela_cadastra_funcionario)
    botao.grid(row=1, column=0,columnspan=2, padx=20, pady=20 , ipadx = 40)

    botao = tk.Button(janela, text='Exportar base de Clientes Cadastrados', command = exporta_nota_cadastro)
    botao.grid(row=2, column=0,columnspan=2, padx=20, pady=20 , ipadx = 40)

    botao = tk.Button(janela, text='Exportar base de Jogos Alugados', command = exporta_nota_aluguel)
    botao.grid(row=3, column=0,columnspan=2, padx=20, pady=20 , ipadx = 40)

    botao_voltar = tk.Button(janela, text='Voltar', command = janela.destroy)
    botao_voltar.grid(row=4, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

def janela_cadastra_jogo():
    janela = tk.Tk()
    janela.title('Cadastro Jogo')

    # Labels:
    label_nome_jogo = tk.Label(janela, text='Nome do Jogo')
    label_nome_jogo.grid(row=0, column=0, padx=10, pady=10)

    label_id_jogo = tk.Label(janela, text='ID do jogo')
    label_id_jogo.grid(row=1, column=0, padx=10, pady=10)

    label_desenvolvedora = tk.Label(janela, text='Desenvolvedora')
    label_desenvolvedora.grid(row=2, column=0, padx=10, pady=10)

    label_plataforma = tk.Label(janela, text='Plataforma')
    label_plataforma.grid(row=3, column=0, padx=10, pady=10)

    label_genero = tk.Label(janela, text='Gênero')
    label_genero.grid(row=4, column=0, padx=10, pady=10)

    label_data_lancamento = tk.Label(janela, text='Data de lancamento')
    label_data_lancamento.grid(row=5, column=0, padx=10, pady=10)

    label_faixa_etaria = tk.Label(janela, text='Faixa etaria')
    label_faixa_etaria.grid(row=6, column=0, padx=10, pady=10)

    label_quant_disp = tk.Label(janela, text='Quantidade Disponível')
    label_quant_disp.grid(row=7, column=0, padx=10, pady=10)

    label_preco = tk.Label(janela, text='Preço (R$)')
    label_preco.grid(row=8, column=0, padx=10, pady=10)

    # Entrys

    entry_nome_jogo = tk.Entry(janela, text='Nome do Jogo')
    entry_nome_jogo.grid(row=0, column=1, padx=10, pady=10)

    entry_id_jogo = tk.Entry(janela, text='id_jogo')
    entry_id_jogo.grid(row=1, column=1, padx=10, pady=10)

    entry_desenvolvedora = tk.Entry(janela, text='desenvolvedora')
    entry_desenvolvedora.grid(row=2, column=1, padx=10, pady=10)

    entry_plataforma = tk.Entry(janela, text='plataforma')
    entry_plataforma.grid(row=3, column=1, padx=10, pady=10)

    entry_genero = tk.Entry(janela, text='genero')
    entry_genero.grid(row=4, column=1, padx=10, pady=10)

    entry_data_lancamento = tk.Entry(janela, text='data_lancamento')
    entry_data_lancamento.grid(row=5, column=1, padx=10, pady=10)

    entry_faixa_etaria = tk.Entry(janela, text='faixa_etaria')
    entry_faixa_etaria.grid(row=6, column=1, padx=10, pady=10)

    entry_quant_disp = tk.Entry(janela, text='quant_disp')
    entry_quant_disp.grid(row=7, column=1, padx=10, pady=10)

    entry_preco = tk.Entry(janela, text='preco')
    entry_preco.grid(row=8, column=1, padx=10, pady=10)

    # Botões

    botao_alugar = tk.Button(janela, text='Cadastrar jogo!', command=lambda: cadastro_jogo(entry_nome_jogo, entry_id_jogo, entry_desenvolvedora, entry_plataforma, entry_genero, entry_data_lancamento, entry_faixa_etaria, entry_quant_disp, entry_preco))
    botao_alugar.grid(row=9, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    botao_exportar = tk.Button(janela, text='Exportar Lista de Jogos', command=exporta_base_jogos)
    botao_exportar.grid(row=10, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    botao_voltar = tk.Button(janela, text='Voltar', command = janela.destroy)
    botao_voltar.grid(row=11, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

def janela_cadastra_funcionario():
    janela = tk.Tk()
    janela.title('Cadastro Funcionário')

    # Labels:
    label_nome = tk.Label(janela, text='Nome')
    label_nome.grid(row=0, column=0, padx=10, pady=10)

    label_cpf = tk.Label(janela, text='CPF')
    label_cpf.grid(row=1, column=0, padx=10, pady=10)

    label_telefone = tk.Label(janela, text='Telefone')
    label_telefone.grid(row=2, column=0, padx=10, pady=10)

    label_telefone = tk.Label(janela, text='Data de Contratação')
    label_telefone.grid(row=3, column=0, padx=10, pady=10)

    label_funcao = tk.Label(janela, text='Cargo')
    label_funcao.grid(row=4, column=0, padx=10, pady=10)

    # Entrys

    entry_nome = tk.Entry(janela, text='Nome', width=30)
    entry_nome.grid(row=0, column=1, padx=10, pady=10)

    entry_cpf = tk.Entry(janela, text='CPF', width=30)
    entry_cpf.grid(row=1, column=1, padx=10, pady=10)

    entry_telefone = tk.Entry(janela, text='Telefone', width=30)
    entry_telefone.grid(row=2, column=1, padx=10, pady=10)

    entry_data_contratacao = tk.Entry(janela, text='Data_contratacao', width=30)
    entry_data_contratacao.grid(row=3, column=1, padx=10, pady=10)

    entry_funcao = tk.Entry(janela, text='funcao', width=30)
    entry_funcao.grid(row=4, column=1, padx=10, pady=10)

    # Botões

    botao_alugar = tk.Button(janela, text='Cadastrar Funcionário!', command=lambda:cadastra_funcionario(entry_cpf, entry_nome, entry_telefone, entry_data_contratacao, entry_funcao))
    botao_alugar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    botao_exportar = tk.Button(janela, text='Exportar Lista de Funcionários', command=exporta_nota_funcionario)
    botao_exportar.grid(row=6, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

    botao_voltar = tk.Button(janela, text='Voltar', command = janela.destroy)
    botao_voltar.grid(row=7, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)


janela = tk.Tk()
janela.title('Locadora de Jogos')

botao = tk.Button(janela, text='Área Cliente', command = janela_area_cliente)
botao.grid(row=0, column=0,columnspan=2, padx=20, pady=20 , ipadx = 40)

botao = tk.Button(janela, text='Área Funcionário', command = janela_area_funcionario)
botao.grid(row=1, column=0,columnspan=2, padx=20, pady=20 , ipadx = 40)

botao_voltar = tk.Button(janela, text='Sair', command = janela.destroy)
botao_voltar.grid(row=3, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

janela.mainloop()