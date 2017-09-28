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
        value = value.replace(',', '.')
        return value
    else:
        return None

def clean_date(value):
    if value:
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
        'Dentista': 0,
        'Dr. A Aparelho Extra Orto': 21,
        'Dra. A Camila Da Silva Calabria': 10,
        'Dra. A Danusa Gomes Barros': 3,
        'Dra. A Danusa Gomes Barros Unimed': 41,
        'A Dra. Marcelle': 23,
        'Dr. A Fernando Implante': 29,
        'Dr. A Fernando Polinati': 5,
        'Dra. A Gabrielle Dos Santos Andrade': 35,
        'Dr. A Glauco Gomes Vilar': 1,
        'Dra. A Izabel': 40,
        'Dra. A Maria Do Carmo': 7,
        'A Pasta De Orto Dr.glauco': 18,
        'Dra. A Pasta De Orto.camila': 16,
        'Dr. A Pasta Orto Rx': 8,
        'Dr. A Protese': 32,
        'Dr. A Reserva': 43,
        'Dr. A Rodrigo Von Kap-hernr De Oliveira': 6,
        'Dra. A Vânia Regina Botelho Soares': 2,
        'Dr. Comissão De  Orto': 12,
        'Dra. Lorraine Fernandes': 42,
        'Pasta De Orto Dra.valeska': 17,
        'Dra. Sobra De Caixa': 11,
        'Dra. Valeska Santos Da Silva Bigi': 13,
        'Dra. Wanderleya Becker M.f.manso': 38,
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