# Primeira maneira
def atualizar_dado(nome, valor):
    receita[nome] = valor


# Segunda maneira
def atualizar_dado2(nome, valor):
    receita.update({nome: valor})


contato = {'nome': 'Vinicius', 'sobrenome': 'Rocha'}

# Maneiras de acessar um dicionário
print(contato['nome'])
print(contato.get('nome'))

# Para verificar se há alguma chave no dicionario
print('nome' in contato)

# Percorrendo os dados do dicionário
for i in contato:
    print(contato[i])

# Atualizando um dado
receita = {'jan': (1000, 5000), 'fev': 2000, 'mar': 3000}

atualizar_dado('abr', 5000)
atualizar_dado2('mai', 7000)

print(receita)

# Remover dados de um dicionário
receita.pop('mai')
print(receita)

# É possivel retornar essa remoção para alguma variável
abril = receita.pop('abr')
print(abril)

# Maneira mais legal de criar um dicionario
contato2 = {}.fromkeys(['nome', 'sobrenome', 'endereço', 'salário'], 'desconhecido')
print(contato2)

# Pegar só as chaves de algum dict
print(contato2.keys())

# Pegar só os valors de algum dict
print(contato2.values())

# Transformando um dict em lista com tuplas
print(contato2.items())
lista = list()
for chave, item in contato2.items():
    print(chave, item)
    lista.append(chave)  # Para guardar chaves em alguma lista
    lista.append(item)  # Para guardar items em alguma lista

print(lista)

# Descobrindo valores maximos, minimos e a soma de todos de algum dicionario
print(receita.get('jan'))
print(sum(receita.get('jan')))
receita.pop('jan')

print(sum(receita.values()))
print(min(receita.values()))
print(max(receita.values()))


