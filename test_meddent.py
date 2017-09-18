import unittest
from meddent import Meddent

class TestMeddent(unittest.TestCase):

    def test_deve_retornar_secao_autenticada(self):
        m = Meddent()
        r = m.session.get('http://meddent.com.br/admin/index.php')
        m.session.close()

        self.assertTrue('Helga' in r.text)

    def test_info_cliente(self):
        m = Meddent()
        cliente = m.get_info_cliente(3024)
        m.session.close()

        self.assertEqual(cliente['id_cliente'], '3024')

        self.assertEqual(cliente['nome'], 'Lindaci')
        self.assertEqual(cliente['codigo'], '132351')
        
        self.assertEqual(cliente['sexo'], 'M')
        self.assertEqual(cliente['dia'], '00')
        self.assertEqual(cliente['mes'], '00')
        self.assertEqual(cliente['ano'], '0000')
        
        self.assertEqual(cliente['id_cartao'], 'Convênio')

        self.assertEqual(cliente['profissao'], 'profissao')

        self.assertEqual(cliente['cpf'], '111.111.111-11')
        self.assertEqual(cliente['estadocivil'], 'Escolha o estado civil')
        
        self.assertEqual(cliente['nacionalidade'], 'nacionalidade')
        self.assertEqual(cliente['naturalidade'], 'Naturalidade')
        
        self.assertEqual(cliente['rg'], 'rg')
        self.assertEqual(cliente['rgorgao'], 'orgao')
        
        self.assertEqual(cliente['comercial'], '(37) 1111-1111')
        self.assertEqual(cliente['residencial'], '(11) 1111-1111')
        
        self.assertEqual(cliente['celular'], '(37) 9999-9999')
        self.assertEqual(cliente['radio'], '(99) 9999-9999')
        
        self.assertEqual(cliente['email'], 'email@email.com')

        self.assertEqual(cliente['endereco'], 'Endereco')
        self.assertEqual(cliente['complemento'], 'complemento')
        
        self.assertEqual(cliente['id_cidade'], 'São João De Meriti')
        self.assertEqual(cliente['id_bairro'], 'Centro')

        self.assertEqual(cliente['estado'], 'Rio de Janeiro')
        self.assertEqual(cliente['cep'], '30.000-000')

        self.assertEqual(cliente['conheceu'], 'Como Conheceu a Clínica')
        self.assertEqual(cliente['id_dentista'], 'Quem Indicou')

        self.assertEqual(cliente['obs'], 'obs')


if __name__ == '__main__':
    unittest.main()