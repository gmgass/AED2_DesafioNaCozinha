from cozinha_classes import CozinhaDoJacquin, Receita

if __name__ == "__main__":
    sistema = CozinhaDoJacquin()

    receitas = [
        Receita("R01", "Bolo de Cenoura", 45, 4.8),
        Receita("R02", "Omelete", 5, 4.0),
        Receita("R03", "Macarrao", 15, 4.2),
        Receita("R04", "Bife Wellington", 120, 5.0)
    ]
    for r in receitas:
        sistema.adicionar(r)

    print("=== SISTEMA INICIADO ===")
    
    # Teste Algoritmo Guloso
    print("\n--- Modo Chef (Tempo Máximo: 60 min) ---")
    menu, tempo_total = sistema.montar_menu_guloso(60)
    for prato in menu:
        print(f"-> {prato}")
    print(f"Tempo total gasto: {tempo_total} min")

    # Teste Investigação (Simulando uma sabotagem)
    print("\n--- Modo Investigação ---")
    receitas[0].tempo = 180
    sistema.investigar()