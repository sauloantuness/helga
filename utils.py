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
        'Dentista': 0,
        'Dr. A Valeska Santos Da Silva Bigi': 2,
        'Pasta De Orto Dra.valeska': 3,
        'Dr. Pasta Rx': 5,
        'Dra. A Anielle Ferreira Rodrigues': 7,
        'Dra. A Lorraine Fernandes Tinoco': 8,
        'A Dra.marcele Luna': 9,
        'Dr. Aparelho Extra Orto': 10,
        'Dra. Wanderleya Becker Munhoz': 11,
        'Dr.  A Protético': 16,
        'Dr.  A Camila Calabria': 17,
        'Dr. Pasta De Orto Dra Camila Calabria': 18,
        'Dr. Pasta De Orto Dra Anielle': 20,
        'Dra. Dra Anielle Amil': 21,
        'Dra. Dra Lorraine Amil': 22,
        'Dr. A Frederico': 29,
        'Dr. Bernardo Giralt': 34,
        'Dra. A Isabel Cristina Theodoro Da Silva': 35,
        'Dra. A Dra Anielle Orto': 36,
        'Dr. Gabriel De Lemos De Oliveira': 39,
        'Dr. A Gabriel Amil': 40,
        'Dr. A Helga': 41,
        'Dra. Patricia Cardoso': 100,
        'Dra. A Lorraine Fernandes Tinoco': 101,
        'Dra. Patricia Cardoso': 100,
        'Dra. A Lorraine Fernandes Tinoco': 101,
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