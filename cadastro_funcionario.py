def cadastroFuncionario():
    while True:
        nome = input("Nome: ")
        idade = int(input("Idade: "))

        lista_de_cargo = ["estagiario", "junior", "pleno", "senior"]
        cargo = input("Cargo: ")
        if cargo not in lista_de_cargo:
            continue
        salario = float(input("Salário: "))
        break
    return [nome, idade, cargo, salario]

funcionario = cadastroFuncionario()
