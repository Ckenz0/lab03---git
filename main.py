def buscar_livro(termo_busca, catalogo):
    """
    Simula a busca de um livro por título dentro do catálogo de uma livraria online.
    """
    termo_busca = termo_busca.lower()
    resultados = [livro for livro in catalogo if termo_busca in livro["titulo"].lower()]
    return resultados


if __name__ == "__main__":
    # Catálogo simulado de livros
    catalogo_livros = [
        {"titulo": "Estrutura de Dados em Python", "autor": "Carlos Silva", "preco": 59.90},
        {"titulo": "Engenharia de Software Moderna", "autor": "Marco Tulio", "preco": 89.90},
        {"titulo": "Clean Code", "autor": "Robert C. Martin", "preco": 75.00},
        {"titulo": "Introdução ao Git e GitHub", "autor": "Ana Souza", "preco": 42.50}
    ]

    termo = "Software"
    print(f"Buscando por: '{termo}'...")
    encontrados = buscar_livro(termo, catalogo_livros)
    
    if encontrados:
        for livro in encontrados:
            print(f"- {livro['titulo']} (R$ {livro['preco']:.2f})")
    else:
        print("Nenhum livro encontrado.")