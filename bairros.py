import requests
import ast
from meddent.meddent import Cliente

c = Cliente(11871)

s = c.session

for key in sorted(['6','5','3','4','2','7','8','1']):
	r = s.get('http://meddent.com.br/includes/AjaxSender.php?cmd=bairros&key=' + key)
	for bairro in ast.literal_eval(r.text):
		print("insert into tb_bairro(id_cidade, id_bairro, ds_bairro) values('{0}', '{1}', '{2}');".format(key, bairro['val'], bairro['txt']))