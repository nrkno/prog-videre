import click


@click.command()
@click.argument("filnavn")
@click.argument("prefiks", default="")
def les_fil(filnavn, prefiks):
    """
    Skriv PREFIKS + innholdet av fila med filstien FILNAVN til terminalen.

    Prefikset PREFIKS blir skrevet ut på starten av hver linje, hvis angitt.
    """

    with open(filnavn) as fil:
        for linje in fil:
            print(prefiks + linje, end="")

les_fil()
