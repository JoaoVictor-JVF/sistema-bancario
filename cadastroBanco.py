from time import sleep


def salvarDados(clientes, contas):
    with open("clientes.txt", "w") as f:
        for cpf, dados in clientes.items():
            f.write(f"{cpf};{dados['nome']};{dados['telefone']}\n")
    with open("contas.txt", "w") as f:
        for conta, dados in contas.items():
            historico = ",".join(map(str, dados['historico']))
            f.write(f"{conta};{dados['cpf']};{dados['saldo']};{historico}\n")


def carregarDados():
    clientes = {}
    contas = {}
    try:
        with open("clientes.txt", "r") as f:
            for linha in f:
                cpf, nome, telefone = linha.strip().split(";")
                clientes[cpf] = {'nome': nome, 'telefone': telefone}
    except FileNotFoundError:
        pass

    try:
        with open("contas.txt", "r") as f:
            for linha in f:
                conta, cpf, saldo, historico = linha.strip().split(";")
                historico = list(map(float, historico.split(",")))
                contas[conta] = {'cpf': cpf, 'saldo': float(
                    saldo), 'historico': historico}
    except FileNotFoundError:
        pass

    return clientes, contas


def opcao(min, max):
    op = 0
    while op < min or op > max:
        try:
            op = int(input("Opção: "))
            if op < min or op > max:
                print("Opção inválida!\n")
        except ValueError:
            print("Digite apenas números!\n")
    return op


def cadastroCliente(clientes):
    print("\n📌 Iniciando cadastro de cliente...\n")
    sleep(1)
    cpf = input("CPF: ")
    if cpf in clientes:
        print("⚠️ Cliente já cadastrado!\n")
        return
    nome = input("Nome completo: ")
    while True:
        try:
            tel = int(input("Telefone: "))
            break
        except ValueError:
            print("Digite apenas números!\n")
    clientes[cpf] = {'nome': nome, 'telefone': tel}
    print("✅ Cadastro realizado com sucesso!\n")


def listarClientes(clientes):
    print("\n📋 Listando clientes...\n")
    sleep(1)
    if clientes:
        for cliente in clientes:
            print(f"👤 Nome: {clientes[cliente]['nome']}")
            print
            print(f"📞 Telefone: {clientes[cliente]['telefone']}")
            print("-------------------------------")
    else:
        print("⚠️ Nenhum cliente cadastrado!\n")


def buscaCPF(clientes):
    print("\n🔎 Buscando cliente...\n")
    sleep(1)
    if clientes:
        cpf = input("CPF: ")
        if cpf in clientes:
            print(f"\n👤 Nome: {clientes[cpf]['nome']}")
            print(f"📞 Telefone: {clientes[cpf]['telefone']}")
            print("-------------------------------\n")
        else:
            print("⚠️ CPF não cadastrado!\n")
    else:
        print("⚠️ Nenhum cliente cadastrado!\n")


def removeCliente(clientes):
    print("\n🗑️ Removendo cliente...\n")
    sleep(1)
    if clientes:
        cpf = input("CPF: ")
        if cpf in clientes:
            print("Deseja mesmo excluir os dados do cliente?\n1 - Não\n2 - Sim")
            escolha = opcao(1, 2)
            if escolha == 1:
                print("❌ Exclusão cancelada!\n")
            else:
                del clientes[cpf]
                print("✅ Cliente removido com sucesso!\n")
        else:
            print("⚠️ CPF não cadastrado!\n")
    else:
        print("⚠️ Nenhum cliente cadastrado!\n")


def subMenuClientes(clientes):
    while True:
        print("\n--- SubMenu Clientes ---")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Buscar por CPF")
        print("4. Remover cliente")
        print("5. Voltar")
        print("------------------------\n")

        escolha = opcao(1, 5)

        if escolha == 1:
            cadastroCliente(clientes)
        elif escolha == 2:
            listarClientes(clientes)
        elif escolha == 3:
            buscaCPF(clientes)
        elif escolha == 4:
            removeCliente(clientes)
        else:
            print("🔙 Retornando ao menu principal...\n")
            return


def cadastroConta(clientes, contas):
    print("\n📌 Iniciando cadastro de conta...\n")
    sleep(1)
    if not clientes:
        print("⚠️ Nenhum cliente cadastrado!\n")
        return

    cpf = input("CPF: ")
    if cpf not in clientes:
        print("⚠️ CPF ainda não cadastrado!\n")
        return

    for conta in contas:
        if contas[conta]['cpf'] == cpf:
            print("⚠️ CPF já vinculado a uma conta!\n")
            return

    novaConta = str(max([int(c) for c in contas] + [0]) + 1).zfill(4)
    contas[novaConta] = {'cpf': cpf, 'saldo': 0, 'historico': [0, 0, 0]}
    print(f"✅ Conta {novaConta} criada com sucesso!\n")


def listarContas(contas):
    print("\n📋 Listando contas bancárias...\n")
    sleep(1)
    if not contas:
        print("⚠️ Nenhuma conta cadastrada!\n")
        return

    for conta, dados in contas.items():
        print(f"🏦 Conta: {conta}")
        print(f"🪪  CPF vinculado: {dados['cpf']}")
        print(f"💰 Saldo: R${dados['saldo']:.2f}")
        if dados['historico'][0] == 0 and dados['historico'][1] == 0:
            print("Histórico: Nenhuma movimentação ainda.")
        else:
            print(f"🔼 Depósitos: R${dados['historico'][0]:.2f}")
            print(f"🔽 Saques: R${dados['historico'][1]:.2f}")
        print("-------------------------------------")


def removerConta(contas):
    print("\n🗑️ Removendo conta...\n")
    sleep(1)
    if not contas:
        print("⚠️ Nenhuma conta cadastrada!\n")
        return

    numeroConta = input("Informe a conta: ")
    if numeroConta not in contas:
        print("⚠️ Conta não existe!\n")
        return

    print("Deseja mesmo excluir a conta?\n1 - Não\n2 - Sim")
    escolha = opcao(1, 2)
    if escolha == 1:
        print("❌ Exclusão cancelada!\n")
    else:
        del contas[numeroConta]
        print("✅ Conta removida com sucesso!\n")


def subMenuContasBancarias(clientes, contas):
    while True:
        print("\n--- SubMenu Contas Bancárias ---")
        print("1. Criar nova conta")
        print("2. Listar contas")
        print("3. Encerrar conta")
        print("4. Voltar")
        print("----------------------------------\n")

        escolha = opcao(1, 4)
        if escolha == 1:
            cadastroConta(clientes, contas)
        elif escolha == 2:
            listarContas(contas)
        elif escolha == 3:
            removerConta(contas)
        else:
            print("🔙 Retornando ao menu principal...\n")
            return


def deposito(contas):
    print("\n💰 Iniciando depósito...\n")
    sleep(1)
    if not contas:
        print("⚠️ Nenhuma conta cadastrada!\n")
        return

    numeroConta = input("Conta: ")
    cpf = input("CPF: ")
    if numeroConta in contas and contas[numeroConta]['cpf'] == cpf:
        try:
            valor = float(input("Valor do depósito: R$"))
            if valor <= 0:
                print("⚠️ Valor inválido!\n")
                return
            contas[numeroConta]['saldo'] += valor
            contas[numeroConta]['historico'][0] += valor
            contas[numeroConta]['historico'][2] += 1
            print("✅ Depósito realizado com sucesso!\n")
        except ValueError:
            print("⚠️ Valor inválido!\n")
    else:
        print("⚠️ Conta ou CPF incorretos!\n")


def saque(contas):
    print("\n🏧 Iniciando saque...\n")
    sleep(1)
    if not contas:
        print("⚠️ Nenhuma conta cadastrada!\n")
        return

    numeroConta = input("Conta: ")
    cpf = input("CPF: ")
    if numeroConta in contas and contas[numeroConta]['cpf'] == cpf:
        try:
            valor = float(input("Valor do saque: R$"))
            if valor <= 0 or valor > contas[numeroConta]['saldo']:
                print("⚠️ Valor inválido ou saldo insuficiente!\n")
                return
            contas[numeroConta]['saldo'] -= valor
            contas[numeroConta]['historico'][1] += valor
            contas[numeroConta]['historico'][2] += 1
            print("✅ Saque realizado com sucesso!\n")
        except ValueError:
            print("⚠️ Valor inválido!\n")
    else:
        print("⚠️ Conta ou CPF incorretos!\n")


def transferencia(contas):
    print("\n🔁 Iniciando transferência...\n")
    sleep(1)
    if not contas:
        print("⚠️ Nenhuma conta cadastrada!\n")
        return

    print("📤 Conta de origem:")
    origem = input("Conta: ")
    cpf_origem = input("CPF: ")
    print("📥 Conta de destino:")
    destino = input("Conta: ")
    cpf_destino = input("CPF: ")

    if origem in contas and destino in contas and contas[origem]['cpf'] == cpf_origem and contas[destino]['cpf'] == cpf_destino:
        try:
            valor = float(input("Valor da transferência: R$"))
            if valor <= 0 or valor > contas[origem]['saldo']:
                print("⚠️ Valor inválido ou saldo insuficiente!\n")
                return
            contas[origem]['saldo'] -= valor
            contas[origem]['historico'][1] += valor
            contas[origem]['historico'][2] += 1

            contas[destino]['saldo'] += valor
            contas[destino]['historico'][0] += valor
            contas[destino]['historico'][2] += 1

            print("✅ Transferência concluída com sucesso!\n")
        except ValueError:
            print("⚠️ Valor inválido!\n")
    else:
        print("⚠️ Dados incorretos. Verifique as contas e os CPFs.\n")


def subMenutransaçoes(contas):
    while True:
        print("\n--- SubMenu Transações ---")
        print("1. Depósito")
        print("2. Saque")
        print("3. Transferência entre contas")
        print("4. Voltar")
        print("--------------------------\n")

        escolha = opcao(1, 4)
        if escolha == 1:
            deposito(contas)
        elif escolha == 2:
            saque(contas)
        elif escolha == 3:
            transferencia(contas)
        else:
            print("🔙 Retornando ao menu principal...\n")
            return


def saquesRelatorio(clientes, contas):
    print("\n📊 Relatório de saldos por cliente...\n")
    sleep(1)
    if not clientes:
        print("⚠️ Nenhum cliente cadastrado!\n")
        return
    if not contas:
        print("⚠️ Nenhuma conta cadastrada!\n")
        return

    for cpf, cliente in clientes.items():
        print(f"👤 Cliente: {cliente['nome']}")
        for conta in contas:
            if contas[conta]['cpf'] == cpf:
                print(
                    f"Conta: {conta} | Saldo: R${contas[conta]['saldo']:.2f}")
        print("-------------------------------")


def totalEmCaixa(contas):
    print("\n💵 Total em caixa do banco...\n")
    sleep(1)
    if not contas:
        print("⚠️ Nenhuma conta cadastrada!\n")
        return

    total = sum(conta['saldo'] for conta in contas.values())
    print(f"🧾 Total em caixa: R${total:.2f}\n")


def movimentaçao(contas):
    print("\n📈 Histórico de movimentações...\n")
    sleep(1)
    if not contas:
        print("⚠️ Nenhuma conta cadastrada!\n")
        return

    for conta, dados in contas.items():
        print(f"Conta: {conta}")
        print(f"🔁 Total de movimentações: {dados['historico'][2]}")
        print("-------------------------------")


def subMenuRelatórios(clientes, contas):
    while True:
        print("\n--- SubMenu Relatórios ---")
        print("1. Mostrar saldo por cliente")
        print("2. Total em caixa no banco")
        print("3. Histórico de movimentações por conta")
        print("4. Voltar")
        print("--------------------------\n")

        escolha = opcao(1, 4)
        if escolha == 1:
            saquesRelatorio(clientes, contas)
        elif escolha == 2:
            totalEmCaixa(contas)
        elif escolha == 3:
            movimentaçao(contas)
        else:
            print("🔙 Retornando ao menu principal...\n")
            return


def main():
    clientes, contas = carregarDados()

    while True:
        print("\n=== 🏦 Sistema Bancário ===")
        print("1. Gerenciar clientes")
        print("2. Contas bancárias")
        print("3. Transações")
        print("4. Relatórios")
        print("5. Sair")
        print("===========================\n")

        escolha = opcao(1, 5)
        if escolha == 1:
            subMenuClientes(clientes)
        elif escolha == 2:
            subMenuContasBancarias(clientes, contas)
        elif escolha == 3:
            subMenutransaçoes(contas)
        elif escolha == 4:
            subMenuRelatórios(clientes, contas)
        else:
            salvarDados(clientes, contas)
            print("\n💾 Salvando dados...")
            print("🚪 Encerrando o programa...\n")
            sleep(2)
            break


main()
