import requests
from bs4 import BeautifulSoup


class Meddent():
    def __init__(self):
        self.CLIENTE_URL = 'http://meddent.com.br/admin/index.php?class=ClientesList&method=onEdit&key='
        self.login()

    def login(self):
        self.session = requests.Session()
        data = {
            'nome': 'helga',
            'senha': '123456'
        }

        url = 'http://meddent.com.br/admin/index.php'

        self.session.post(url=url, data=data)


    def get_input_value(self, soup, name):
        return soup.find(attrs={'name': name}).get('value')

    def get_select_value(self, soup, name):
        select = soup.find(attrs={'name': name})

        if select.find('option', attrs={'selected': 'selected'}):
            return select.find('option', attrs={'selected': 'selected'}).get('value')

        return select.find('option').get('value')

    def get_radio_value(self, soup, name):
        return soup.find(attrs={'name': name, 'checked': 'checked'}).get('value')

    def get_textarea_value(self, soup, name):
        return soup.find(attrs={'name': name}).text.strip()

    def get_info_cliente(self, id_cliente):
        url = self.CLIENTE_URL + str(id_cliente)
        r = self.session.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')


        cliente = {
            'id_cliente': self.get_input_value(soup, 'id_cliente'),

            'nome': self.get_input_value(soup, 'nome'),
            'codigo': self.get_input_value(soup, 'codigo'),
            
            'sexo': self.get_radio_value(soup, 'sexo'),
            'dia': self.get_input_value(soup, 'dia'),
            'mes': self.get_input_value(soup, 'mes'),
            'ano': self.get_input_value(soup, 'ano'),
            
            'convenio': self.get_select_value(soup, 'id_cartao'),
            
            'profissao': self.get_input_value(soup, 'profissao'),
            
            'cpf': self.get_input_value(soup, 'cpf'),
            'estadocivil': self.get_select_value(soup, 'estadocivil'),
            
            'nacionalidade': self.get_input_value(soup, 'nacionalidade'),
            'naturalidade': self.get_input_value(soup, 'naturalidade'),
            
            'rg': self.get_input_value(soup, 'rg'),
            'rgorgao': self.get_input_value(soup, 'rgorgao'),
            
            'comercial': self.get_input_value(soup, 'comercial'),
            'residencial': self.get_input_value(soup, 'residencial'),
            
            'celular': self.get_input_value(soup, 'celular'),
            'celular2': self.get_input_value(soup, 'radio'),
            
            'email': self.get_input_value(soup, 'email'),
            
            'endereco': self.get_input_value(soup, 'endereco'),
            'complemento': self.get_input_value(soup, 'complemento'),
            
            'id_cidade': self.get_select_value(soup, 'id_cidade'),
            'id_bairro': self.get_select_value(soup, 'id_bairro'),
            
            'id_estado': self.get_select_value(soup, 'estado'),
            'cep': self.get_input_value(soup, 'cep'),
            
            'id_marketing': self.get_select_value(soup, 'conheceu'),
            'id_dentista': self.get_select_value(soup, 'id_dentista'),
            
            'obs': self.get_textarea_value(soup, 'obs'),
        }

        return cliente