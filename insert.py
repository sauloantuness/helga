import pyodbc

server = 'r13.ddns.me'
port = '49841' 
database = 'r13_educat_dev'
username = 'sa'
password = 'r13r13r13'

cnxn = pyodbc.connect('DRIVER=FreeTDS;SERVER='+server+';PORT='+port+';DATABASE='+database+';UID='+username+';PWD='+ password + ';TDS_Version=7.2;')
cursor = cnxn.cursor()
cursor.execute(command)
cursor.commit()


def insert_mensalidade():
	insert into tb_mensalidade 