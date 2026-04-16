def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    print("=== Conversor de Temperaturas ===")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        c = float(input("Digite a temperatura em Celsius: "))
        print(f"{c}°C = {celsius_para_fahrenheit(c)}°F")
    elif opcao == "2":
        f = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_para_celsius(f)}°F")
    else:
        print("Opção inválida!")
