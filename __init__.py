def is_valid_cpf(cpf):

    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se o CPF tem 11 dígitos e se não é uma sequência repetida
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    
    # Função para calcular os dígitos verificadores
    def calc_digit(cpf, peso_inicial):
        soma = sum(int(cpf[i]) * (peso_inicial - i) for i in range(peso_inicial - 1))
        digito = (soma * 10 % 11) % 10
        return digito

    # Calcula e verifica os dois dígitos verificadores
    primeiro_digito = calc_digit(cpf, 10)
    segundo_digito = calc_digit(cpf, 11)
    
    return primeiro_digito == int(cpf[9]) and segundo_digito == int(cpf[10])

# Teste da função
cpf = input('Digite um CPF: ')

if is_valid_cpf(cpf): 
    print(f"O CPF {cpf} é válido!")
else :
    print(f"O CPF {cpf} não é válido!")
