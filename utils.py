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
        return float(value)
    else:
        return None

def clean_date(value):
    if value:
        d, m, y = [int(v) for v in value.split('/')]

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