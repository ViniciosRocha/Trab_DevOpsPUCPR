"""
Módulo para validação de CPF (Cadastro de Pessoas Físicas)
Implementa o algoritmo oficial de validação dos dígitos verificadores
"""

def calcular_digito(cpf_base, multiplicador_inicial):
    """
    Calcula um dígito verificador do CPF
    cpf_base: lista com os primeiros 9 dígitos (para o 1º dígito) 
              ou 10 dígitos (para o 2º dígito)
    multiplicador_inicial: 10 para o 1º dígito, 11 para o 2º dígito
    """
    soma = 0
    multiplicador = multiplicador_inicial
    
    for digito in cpf_base:
        soma += digito * multiplicador
        multiplicador -= 1
    
    resto = soma % 11
    digito = 0 if resto < 2 else 11 - resto
    return digito

def validar_cpf(cpf: str) -> bool:
    """
    Valida um CPF fornecido como string.
    Retorna True se válido, False caso contrário.
    """
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais (ex: 111.111.111-11)
    if cpf == cpf[0] * 11:
        return False
    
    # Converte para lista de inteiros
    digitos = [int(d) for d in cpf]
    
    # Cálculo do primeiro dígito verificador
    primeiro_digito = calcular_digito(digitos[:9], 10)
    
    # Cálculo do segundo dígito verificador
    segundo_digito = calcular_digito(digitos[:10], 11)
    
    # Verifica se os dígitos calculados conferem
    return digitos[9] == primeiro_digito and digitos[10] == segundo_digito

def formatar_cpf(cpf: str) -> str:
    """
    Formata um CPF no padrão XXX.XXX.XXX-XX
    """
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return cpf
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

if __name__ == "__main__":
    print("=== Validador de CPF ===\n")
    
    while True:
        cpf_input = input("Digite o CPF (apenas números ou com pontos/traço): ")
        
        if validar_cpf(cpf_input):
            print(f"✅ CPF {formatar_cpf(cpf_input)} é VÁLIDO!")
        else:
            print(f"❌ CPF {formatar_cpf(cpf_input)} é INVÁLIDO!")
        
        print()
        continuar = input("Deseja testar outro CPF? (s/n): ")
        if continuar.lower() != 's':
            print("\nEncerrando programa...")
            break
# Versao com CI/CD configurado
