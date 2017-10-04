import os
import pickle
import pyodbc
from pprint import pprint
from datetime import datetime
from utils import *
from meddent.config import *

server = '192.168.15.58'
#server = 'r13.ddns.me'
port = '49841' 
database = CONFIG['DATABASE']
username = 'sa'
password = 'r13r13r13'

cnxn = pyodbc.connect('DRIVER=FreeTDS;SERVER='+server+';PORT='+port+';DATABASE='+database+';UID='+username+';PWD='+ password + ';TDS_Version=7.2;')
cursor = cnxn.cursor()


def load_obj(folder, name):
    print('data/' + folder + '/' + name)
    with open('data/' + folder + '/' + name, 'rb') as f:
        return pickle.load(f)

def clean_contrato(contrato):
    contrato['id_contrato'] = clean_int(contrato['id_contrato'])
    contrato['valor'] = clean_valor(contrato['valor'])
    contrato['tempo'] = clean_str(contrato['tempo'])
    contrato['multa'] = clean_str(contrato['multa'])
    contrato['juros'] = clean_str(contrato['juros'])
    contrato['primeira_mensalidade'] = clean_date(contrato['primeira_mensalidade'])
    contrato['registro'] = clean_date(contrato['registro'])
    contrato['status'] = clean_str(contrato['status'])
    contrato['obs'] = clean_str(contrato['obs'])
    contrato['id_cliente'] = clean_contrato_id_cliente(contrato['codigo'], cursor)
    contrato['id_dentista'] = clean_dentista(contrato['dentista'])

    return contrato

def insert_contrato(contrato):
    contrato = clean_contrato(contrato)

    sql = """
        insert into tb_contrato(
            id_contrato,
            codigo,
            valor,
            tempo,
            multa,
            juros,
            primeira_mensalidade,
            registro,
            status,
            obs,
            id_cliente,
            id_dentista
    ) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """

    cursor.execute(sql, 
        contrato['id_contrato'],
        contrato['codigo'],
        contrato['valor'],
        contrato['tempo'],
        contrato['multa'],
        contrato['juros'],
        contrato['primeira_mensalidade'],
        contrato['registro'],
        contrato['status'],
        contrato['obs'],
        contrato['id_cliente'],
        contrato['id_dentista'],
    )

    cursor.commit()

def clean_mensalidade(mensalidade):
    mensalidade['id_mensalidade'] = clean_int(mensalidade['id_mensalidade'])
    mensalidade['status'] = clean_mensalidade_status(mensalidade['status'])
    mensalidade['vencimento'] = clean_date(mensalidade['vencimento'])
    mensalidade['valor'] = clean_valor(mensalidade['valor'])
    mensalidade['multa'] = clean_valor(mensalidade['multa'])
    mensalidade['pagamento'] = clean_float(mensalidade['pagamento'])
    mensalidade['desconto'] = clean_float(mensalidade['desconto'])
    mensalidade['residuo'] = clean_valor(mensalidade['residuo'])
    mensalidade['obs'] = clean_str(mensalidade['obs'])
    mensalidade['id_contrato'] = clean_int(mensalidade['id_contrato'])

    return mensalidade

def insert_mensalidade(mensalidade):
    mensalidade = clean_mensalidade(mensalidade)
    sql = """
        insert into tb_mensalidade(
            id_mensalidade,
            status,
            vencimento,
            valor,
            multa,
            pagamento,
            desconto,
            residuo,
            obs,
            id_contrato
    ) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """

    cursor.execute(sql, 
        mensalidade['id_mensalidade'],
        mensalidade['status'],
        mensalidade['vencimento'],
        mensalidade['valor'],
        mensalidade['multa'],
        mensalidade['pagamento'],
        mensalidade['desconto'],
        mensalidade['residuo'],
        mensalidade['obs'],
        mensalidade['id_contrato']
    )

    cursor.commit()

def clean_tratamento(tratamento):
    tratamento['id_tratamento'] = clean_int(tratamento['id_tratamento'])
    tratamento['id_cliente'] = clean_int(tratamento['id_cliente'])
    tratamento['id_dentista'] = clean_dentista(tratamento['dentista'])

    return tratamento

def insert_tratamento(tratamento):
    tratamento = clean_tratamento(tratamento)

    sql = """
        insert into tb_tratamento(
            id_tratamento,
            id_cliente,
            id_dentista
    ) values (?, ?, ?) """


    cursor.execute(sql, 
        tratamento['id_tratamento'],
        tratamento['id_cliente'],
        tratamento['id_dentista'],
    )

    for procedimento in tratamento['procedimentos']:
        insert_procedimento(procedimento)


def clean_procedimento(procedimento):
    procedimento['id_procedimento'] = clean_int(procedimento['id_procedimento'])
    procedimento['data'] = clean_date(procedimento['data'])
    procedimento['procedimento'] = clean_str(procedimento['procedimento'])
    procedimento['especialidade'] = clean_str(procedimento['especialidade'])
    procedimento['valor'] = clean_valor(procedimento['valor'])
    procedimento['quantidade'] = clean_int(procedimento['quantidade'])
    procedimento['total'] = clean_valor(procedimento['total'])
    procedimento['id_tratamento'] = clean_int(procedimento['id_tratamento'])

    return procedimento

def insert_procedimento(procedimento):
    procedimento = clean_procedimento(procedimento)

    sql = """
        insert into tb_procedimento(
            id_procedimento,
            id_tratamento,
            data,
            procedimento,
            especialidade,
            valor,
            quantidade,
            total
    ) values (?, ?, ?, ?, ?, ?, ?, ?) """

    cursor.execute(sql, 
        procedimento['id_procedimento'],
        procedimento['id_tratamento'],
        procedimento['data'],
        procedimento['procedimento'],
        procedimento['especialidade'],
        procedimento['valor'],
        procedimento['quantidade'],
        procedimento['total'],
    )

    cursor.commit()

def clean_pagamento(pagamento):    
    pagamento['id_pagamento'] = clean_int(pagamento['id_pagamento'])
    pagamento['id_tratamento'] = clean_int(pagamento['id_tratamento'])

    pagamento['data'] = clean_date(pagamento['data'])

    pagamento['tipo'] = clean_str(pagamento['tipo'])
    pagamento['valor'] = clean_valor(pagamento['valor'])

    return pagamento

def insert_pagamento(pagamento):
    pagamento = clean_pagamento(pagamento)

    sql = """
        insert into tb_pagamento(
            id_pagamento,
            data,
            tipo,
            valor,
            id_tratamento
    ) values (?, ?, ?, ?, ?) """

    cursor.execute(sql, 
        pagamento['id_pagamento'],
        pagamento['data'],
        pagamento['tipo'],
        pagamento['valor'],
        pagamento['id_tratamento'],
    )

    cursor.commit()

def clean_cliente(cliente):
    cliente['id_cliente'] = clean_int(cliente['id_cliente'])
    
    cliente['nome'] = clean_str(cliente['nome'])
    cliente['codigo'] = clean_int(cliente['codigo'])
    
    cliente['sexo'] = clean_str(cliente['sexo'])
    cliente['nascimento'] = clean_nascimento(cliente)
    
    cliente['id_convenio'] = clean_int(cliente['convenio'])
    
    cliente['profissao'] = clean_str(cliente['profissao'])

    cliente['cpf'] = clean_cpf(cliente['cpf'])
    cliente['id_estado_civil'] = clean_str(cliente['estado_civil'])
    
    cliente['nacionalidade'] = clean_str(cliente['nacionalidade'])
    cliente['naturalidade'] = clean_str(cliente['naturalidade'])
    
    cliente['rg'] = clean_str(cliente['rg'])
    cliente['rg_orgao'] = clean_str(cliente['rgorgao'])

    cliente['telefone_comercial'] = clean_str(cliente['comercial'])
    cliente['telefone_residencial'] = clean_str(cliente['residencial'])

    cliente['celular'] = clean_str(cliente['celular'])
    cliente['celular_2'] = clean_str(cliente['celular2'])

    cliente['email'] = clean_str(cliente['email'])

    cliente['endereco'] = clean_str(cliente['endereco'])
    cliente['complemento'] = clean_str(cliente['complemento'])

    cliente['id_cidade'] = clean_int(cliente['id_cidade'])
    cliente['id_bairro'] = clean_int(cliente['id_bairro'])
    
    cliente['id_estado'] = clean_str(cliente['id_estado'])
    cliente['cep'] = clean_str(cliente['cep'])
    
    cliente['id_marketing'] = clean_str(cliente['id_marketing'])
    cliente['id_indicacao'] = clean_int(cliente['id_dentista'])
    
    cliente['obs'] = clean_str(cliente['obs'])

    cliente['responsavel_nome'] = clean_str(cliente['responsavel_nome'])
    cliente['responsavel_cpf'] = clean_cpf(cliente['responsavel_cpf'])
    cliente['responsavel_endereco'] = clean_str(cliente['responsavel_endereco'])

    return cliente

def insert_cliente(cliente):
    cliente = clean_cliente(cliente)

    sql = """
        insert into tb_cliente(
            id_cliente,
            nome,
            codigo,
            sexo,
            nascimento,
            id_convenio,
            profissao,
            cpf,
            id_estado_civil,
            nacionalidade,
            naturalidade,
            rg,
            rg_orgao,
            telefone_comercial,
            telefone_residencial,
            celular,
            celular_2,
            email,
            endereco,
            complemento,
            id_cidade,
            id_bairro,
            id_estado,
            cep,
            id_marketing,
            id_indicacao,
            obs,
            responsavel_nome,
            responsavel_cpf,
            responsavel_endereco
    ) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """

    cursor.execute(sql, 
        cliente['id_cliente'],
        cliente['nome'],
        cliente['codigo'],
        cliente['sexo'],
        cliente['nascimento'],
        cliente['id_convenio'],
        cliente['profissao'],
        cliente['cpf'],
        cliente['id_estado_civil'],
        cliente['nacionalidade'],
        cliente['naturalidade'],
        cliente['rg'],
        cliente['rg_orgao'],
        cliente['telefone_comercial'],
        cliente['telefone_residencial'],
        cliente['celular'],
        cliente['celular_2'],
        cliente['email'],
        cliente['endereco'],
        cliente['complemento'],
        cliente['id_cidade'],
        cliente['id_bairro'],
        cliente['id_estado'],
        cliente['cep'],
        cliente['id_marketing'],
        cliente['id_indicacao'],
        cliente['obs'],
        cliente['responsavel_nome'],
        cliente['responsavel_cpf'],
        cliente['responsavel_endereco']
    )

    cursor.commit()

if __name__ == '__main__':
     # t = load_obj('tratamentos', '17769.pkl')
     # pprint(t)
     # exit()
     for obj in sorted(os.listdir('data/pagamentos/')):
        item = load_obj('pagamentos', obj)
        command = insert_pagamento(item)
