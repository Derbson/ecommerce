from validate_docbr import CPF
from datetime import date
import re


def validate_cpf(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)


def validate_age(age):
    if age <= 0 or age >= 120:
        return False
    return True

def validate_cep(cep):
    if re.search(r'[^0-9]', cep) or len(cep) != 8:
        return False
    return True
    

def valida_data_nascimento(age,born): 
    today = date.today() 
    try:  
        birthday = born.replace(year = today.year)    
    except ValueError:  
        birthday = born.replace(year = today.year, 
                  month = born.month + 1, day = 1) 
  
    if birthday > today:
        if age == (today.year - born.year - 1):
            return True
        return False
    else:
        if age == (today.year - born.year):
            return True
        return False     

    
