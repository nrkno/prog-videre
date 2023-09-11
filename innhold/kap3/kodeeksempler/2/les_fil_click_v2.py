import click


@click.command()
@click.argument("filnavn")
def les_fil(filnavn):
    """
    Skriv innholdet av fila med filstien FILNAVN til terminalen.
    """

    with open(filnavn) as fil:
        for linje in fil:
            print(linje, end="")

les_fil()
