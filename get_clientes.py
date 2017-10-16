import os
import pickle
from meddent.meddent import *
from meddent.config import *
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

def downloaded():
    files = os.listdir('./data/clientes')
    ids = [int(f.split('.')[1]) for f in files]
    return ids


def get_clientes():
    dowloaded_ids = dowloaded()

    ID_CLIENTE = CONFIG['ID_CLIENTE']
    c = Cliente(ID_CLIENTE)

    while ID_CLIENTE:

        if ID_CLIENTE in dowloaded_ids:
            print(ID_CLIENTE)
            ID_CLIENTE -= 1
            continue

        begin = datetime.now()

        c.set_id_cliente(ID_CLIENTE)
        cliente = c.get_info()

        if cliente:
            print(cliente['id_cliente'])
            save_obj(cliente, 'clientes', cliente['id_cliente'])
        else:
            print(str(ID_CLIENTE) + ' invalido')

        ID_CLIENTE -= 1

        end = datetime.now()

        duration = end - begin

        print('Tempo estimado: %d:%02d' % days_hours_minutes(duration * ID_CLIENTE)[1:])


if __name__ == '__main__':
    if not os.path.exists('./data/clientes'):
        os.makedirs('./data/clientes')

    get_clientes()