import os
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
	ID_CONTRATO = 1353
	c = ContratoOrto(ID_CONTRATO)

	while ID_CONTRATO: 
		begin = datetime.now()

		c.set_id_contrato(ID_CONTRATO)
		contrato = c.get_info()

		if contrato:
			import pdb; pdb.set_trace()
			print(contrato['id_contrato'])
			save_obj(contrato, 'contratos', contrato['id_contrato'])

			for mensalidade in contrato.get_mensalidades():
				print('\t' + mensalidade['id_mensalidade'])
				save_obj(mensalidade, 'mensalidades', mensalidade['id_contrato'])

		else:
			print(str(ID_CONTRATO) + u' inválido')

		ID_CONTRATO -= 1

		end = datetime.now()

		duration = end - begin

		print('Tempo estimado: %d:%02d' % days_hours_minutes(duration * ID_CONTRATO)[1:])


if __name__ == '__main__':
	if not os.path.exists('./data/clientes'):
	    os.makedirs('./data/clientes')

	if not os.path.exists('./data/contratos'):
	    os.makedirs('./data/contratos')

	if not os.path.exists('./data/mensalidades'):
	    os.makedirs('./data/mensalidades')

	get_contratos()