import re
from validate_docbr import CPF


def cpf_valido(numero_do_cpf):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)


def nome_valido(nome):
    return nome.isalpha()


def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9


def celular_valido(numero_de_celular):
    """ Verifica se o numero de celular é valido (00) 00000-0000"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_de_celular)
    return resposta