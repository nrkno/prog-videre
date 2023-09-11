import click


@click.command()
@click.argument("filnavn")
@click.argument("prefiks")
def les_fil_med_prefiks(filnavn, prefiks):
    """
    Skriv PREFIKS + innholdet av fila med filstien FILNAVN til terminalen.

    Prefikset PREFIKS blir skrevet ut på starten av hver linje.
    """

    with open(filnavn) as fil:
        for linje in fil:
            print(prefiks + linje, end="")

les_fil_med_prefiks()
