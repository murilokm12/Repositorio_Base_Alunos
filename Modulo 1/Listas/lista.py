# lista inicial
nomes = ["joaquim","Maria","Ana"]
print("lista inicial:",nomes)

# Adicionadno elementos
nomes.append("Carlos") # Adicionando ao final
print("Após append:",nomes)

nomes.insert(1,"Fernanda") # Isere "Fernanda" na posição 1
print("Após insert:", nomes)

# Modificando elementos
nomes[2] = "Paulo" # Modifica o elemento no índice 2
print("Após modificação:", nomes)

# Removendo elementos
del nomes[3] # Remove o elemento da índice 3
print("Após del:", nomes)

nomes.remove("Maria") # Remove a primeira ocorrência da "Maria"
print("Após remove:", nomes)

Removido = nomes.pop(2) # Remove e retorna o elemento no índice 2
print(f"Após pop (removido) '(removido)'):", nomes)

nomes.clear() # Esvazia a lista
print("Após clear:", nomes)



