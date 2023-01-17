import re
  
# Criando uma expressão regular
condicao_email="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
 
email_usuario=input('Digite o E-mail: ')
 
# Usando o método search do modulo re 
if re.search(condicao_email, email_usuario): 
    print('Email valido')
else:
    print('Email invalido')
