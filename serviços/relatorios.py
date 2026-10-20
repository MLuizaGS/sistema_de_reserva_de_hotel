def relatorio_quartos(quartos):
    """Exibe um resumo dos quartos cadastrados."""

    total = len(quartos)

    disponiveis = sum(
        1 for quarto in quartos
        if quarto.status == "DISPONIVEL"
    )

    ocupados = sum(
        1 for quarto in quartos
        if quarto.status == "OCUPADO"
    )

    manutencao = sum(
        1 for quarto in quartos
        if quarto.status == "MANUTENCAO"
    )

    print("\n=== RELATÓRIO DE QUARTOS ===")
    print(f"Total de quartos: {total}")
    print(f"Disponíveis: {disponiveis}")
    print(f"Ocupados: {ocupados}")
    print(f"Em manutenção: {manutencao}")

    if total:
        taxa = ocupados / total * 100
        print(f"Ocupação atual: {taxa:.2f}%")
    else:
        print("Ocupação atual: 0.00%")