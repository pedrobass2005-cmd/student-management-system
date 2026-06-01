import json

def salvar_dados():
    with open("alunos.json", "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, indent=4, ensure_ascii=False)

def carregar_dados():
    try:
        with open("alunos.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

alunos = carregar_dados()

while True:
    print('\n1 - Cadastrar aluno')
    print('2 - Listar alunos')
    print('3 - Mostrar média das notas')
    print('4 - Mostrar aprovados e reprovados')
    print('5 - Buscar aluno por nome')
    print('6 - Editar nota de um aluno')  # Nova funcionalidade
    print('7 - Remover aluno')             # Nova funcionalidade
    print('8 - Sair')
    
    try:
        op = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, digite apenas números.")
        continue

    if op == 1:
        nome = input("Nome: ")
        try:
            idade = int(input("Idade: "))
            nota = float(input("Nota: "))
        except ValueError:
            print("Erro: Idade deve ser número inteiro e Nota deve ser número decimal.")
            continue
            
        alunos.append({
            "nome": nome,
            "idade": idade,
            "nota": nota
        })
        salvar_dados()
        print("Aluno cadastrado e salvo com sucesso!")
        
    elif op == 2:
        print("\n--- LISTA DE ALUNOS ---")
        if not alunos:
            print("Nenhum aluno cadastrado.")
        for aluno in alunos:
            print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}")

    elif op == 3:
        print("\n--- MÉDIA DAS NOTAS ---")
        if not alunos:
            print("Nenhum aluno cadastrado para calcular a média.")
        else:
            total_notas = sum(aluno["nota"] for aluno in alunos)
            media = total_notas / len(alunos)
            print(f"A média geral da turma é: {media:.2f}")

    elif op == 4:
        print("\n--- SITUAÇÃO DOS ALUNOS ---")
        print("\nAprovados:")
        for aluno in alunos:
            if aluno["nota"] >= 7:
                print(f"- {aluno['nome']} (Nota: {aluno['nota']})")
                
        print("\nReprovados:")
        for aluno in alunos:
            if aluno["nota"] < 7:
                print(f"- {aluno['nome']} (Nota: {aluno['nota']})")

    elif op == 5:
        busca = input("Digite o nome para buscar: ")
        encontrado = False

        for aluno in alunos:
            if aluno["nome"].lower() == busca.lower():
                print(f"\nAluno encontrado: Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}")
                encontrado = True
                break
                
        if not encontrado:
            print("Aluno não encontrado.")
            
    elif op == 6:
        busca = input("Digite o nome do aluno para editar a nota: ")
        encontrado = False

        for aluno in alunos:
            if aluno["nome"].lower() == busca.lower():
                try:
                    nova_nota = float(input(f"Digite a nova nota para {aluno['nome']}: "))
                    aluno["nota"] = nova_nota
                    salvar_dados()
                    print("Nota atualizada e salva com sucesso!")
                except ValueError:
                    print("Erro: A nota deve ser um número decimal.")
                encontrado = True
                break
                
        if not encontrado:
            print("Aluno não encontrado.")

    elif op == 7:
        busca = input("Digite o nome do aluno para remover: ")
        encontrado = False

        for aluno in alunos:
            if aluno["nome"].lower() == busca.lower():
                alunos.remove(aluno)
                salvar_dados()
                print(f"Aluno {aluno['nome']} removido com sucesso!")
                encontrado = True
                break
                
        if not encontrado:
            print("Aluno não encontrado.")

    elif op == 8: 
        print("Saindo do sistema...")
        break
        
    else:
        print("Opção inválida! Tente novamente.")
