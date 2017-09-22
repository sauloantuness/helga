import os, sys
import pickle
from meddent.meddent import *
from pprint import pprint
from datetime import datetime

def save_obj(obj, folder, name):
    with open('data/'+ folder + '/' + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f)

def load_obj(folder, name):
    with open('data/' + folder + '/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def days_hours_minutes(td):
    return td.days, td.seconds//3600, (td.seconds//60)%60

def get_contratos():
	# sys.setrecursionlimit(10000)
	ID_CLIENTE = 11855
	link_pagina_tratamento = None
	cliente = Cliente(ID_CLIENTE)

	while ID_CLIENTE: 
		begin = datetime.now()

		cliente.set_id_cliente(ID_CLIENTE)
		soup = cliente.get_pagina_tratamento(link_pagina_tratamento)
		link_pagina_tratamento = None

		tratamento = Tratamento(soup)
		procedimentos = tratamento.get_procedimentos()

		if procedimentos:
			tratamento = {
				'id_tratamento': procedimentos[0]['id_tratamento'],
				'procedimentos': procedimentos,
			}

			print(tratamento['id_tratamento'] + ' tratamento')
			save_obj(tratamento, 'tratamentos', tratamento['id_tratamento'])

			pagamento = Pagamento(soup)
			pagamentos = pagamento.get_pagamentos()

			for pagamento in pagamentos:
				print('\t' + pagamento['id_pagamento'] + ' pagamento')
				save_obj(pagamento, 'pagamentos', pagamento['id_pagamento'])


			link_pagina_tratamento = cliente.get_link_tratamento_anterior(soup)
		else:
			print(str(ID_CLIENTE) + ' invalido')


		if not link_pagina_tratamento:
			ID_CLIENTE -= 1

		end = datetime.now()
		duration = end - begin
		print('Tempo estimado: %d:%02d' % days_hours_minutes(duration * ID_CLIENTE)[1:])


if __name__ == '__main__':
	if not os.path.exists('./data/clientes'):
	    os.makedirs('./data/clientes')

	if not os.path.exists('./data/contratos'):
	    os.makedirs('./data/contratos')

	if not os.path.exists('./data/mensalidades'):
	    os.makedirs('./data/mensalidades')

	if not os.path.exists('./data/pagamentos'):
	    os.makedirs('./data/pagamentos')

	if not os.path.exists('./data/tratamentos'):
	    os.makedirs('./data/tratamentos')

	get_contratos()
	# pprint(load_obj('tratamentos', '13852'))
	# pprint(load_obj('pagamentos', '35163'))