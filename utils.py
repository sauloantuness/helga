def clean_cpf(cpf):
	cpf = ''.join(d for d in cpf if d.isdigit())
	if cpf:
		return int(cpf)
	return None

def clean_str(value):
    if value:
        return str(value)
    else:
        return None

def clean_int(value):
    if value:
        return int(value)
    else:
        return None

def clean_float(value):
    if value:
        value = value.replace(',', '.')
        return float(value)
    else:
        return None

def clean_valor(value):
    if value:
        value = value.split(' ')[1]
        value = value.replace('.', '')
        value = value.replace(',', '.')
        value = float(value)
        return value
    else:
        return None

def clean_date(value):
    if value:
        if '-' in value:
            y, m, d = [v for v in value.split('-')]
        else:
            d, m, y = [v for v in value.split('/')]

        return '-'.join([y, m, d])
    else:
        return None

def clean_nascimento(cliente):
    nascimento = None

    if cliente['ano'] == '0000' or cliente['mes'] == '00' or cliente['dia'] == '00':
        return None

    if cliente['ano'] and cliente['mes'] and cliente['dia']:
        nascimento = cliente['ano'] + '-' + cliente['mes'] + '-' + cliente['dia']

    return nascimento

def clean_dentista(dentista):
    dentistas = {
        'A Dra. Marcelle': 23,
        'A Pasta De Orto Dr.glauco': 18,
        'Dentista': 0,
        'Dr. A Alexandre P. Martins': 42,
        'Dr. A Alexandre Unimed': 46,
        'Dr. A Aparelho Extra Orto Fernanda': 55,
        'Dr. A Aparelho Extra Orto Glaucia': 39,
        'Dr. A Aparelho Extra Orto Jorge Guilherme': 50,
        'Dr. A Aparelho Extra Orto': 21,
        'Dr. A Fernando Implante': 29,
        'Dr. A Fernando Polinati': 5,
        'Dr. A Frederico': 6,
        'Dr. A Glauco Gomes Vilar': 1,
        'Dr. A Pasta De Orto Paula': 19,
        'Dr. A Pasta Orto Rx': 8,
        'Dr. A Protese': 32,
        'Dr. A Prótese': 40,
        'Dr. A Reserva': 43,
        'Dr. A Reserva': 54,
        'Dr. A Rodrigo Von Kap-hernr De Oliveira': 6,
        'Dr. Aparelho Extra Orto Priscilla': 51,
        'Dr. Apasta Orto/rx': 4,
        'Dr. Bernardo Giralt': 56,
        'Dr. Comissão De  Orto': 12,
        'Dr. Dr Sobra De Caixa': 15,
        'Dr. Gabriel De Lemos De Oliveira': 48,
        'Dr. Jeferson Vaz': 44,
        'Dr. Jorge Guilherme': 28,
        'Dr. Pasta De Orto Jorge Guilherme': 31,
        'Dra.  A Glaucia Ribeiro(orto)': 43,
        'Dra. A Aparelho Extra Orto Paula': 47,
        'Dra. A Camila Da Silva Calabria': 10,
        'Dra. A Danusa Gomes Barros Unimed': 41,
        'Dra. A Danusa Gomes Barros': 3,
        'Dra. A Dra Juliana Pinto': 16,
        'Dra. A Fernanda  De Lima': 11,
        'Dra. A Fernanda Martins De Araujo': 52,
        'Dra. A Fernanda Martins Orto': 53,
        'Dra. A Gabrielle Dos Santos Andrade': 49,
        'Dra. A Glaucia Ribeiro': 9,
        'Dra. A Helga': 45,
        'Dra. A Izabel': 40,
        'Dra. A Maria Do Carmo': 7,
        'Dra. A Pasta De Orto Glaucia': 37,
        'Dra. A Pasta De Orto Priscila': 17,
        'Dra. A Pasta De Orto.camila': 16,
        'Dra. A Paula Calabria': 2,
        'Dra. A Priscilla Rocha': 3,
        'Dra. A Vânia Regina Botelho Soares': 2,
        'Dra. Lorraine Fernandes': 42,
        'Dra. Sobra De Caixa': 11,
        'Dra. Valeska Santos Da Silva Bigi': 13,
        'Dra. Valeska Santos': 20,
        'Dra. Wanderleya Becker M.f.manso': 38,
        'Pasta De Orto Dra.valeska': 17,
        'Dra. Patricia Cardoso': 100,
        'Dra. A Lorraine Fernandes Tinoco', 101,
    }

    return dentistas.get(dentista, None)

def clean_contrato_id_cliente(codigo, cursor):
    sql = 'select id_cliente from tb_cliente where codigo = ?;'
    id_cliente,  = cursor.execute(sql, codigo).fetchone()
    return id_cliente

def clean_mensalidade_status(status):
    if status == '../images/icons/newpaga.jpg':
        return 'paga'
    if status == '../images/icons/newatraso.jpg':
        return 'atraso'