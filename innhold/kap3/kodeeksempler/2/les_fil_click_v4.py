import click


@click.command()
@click.option("--number", "-n", is_flag=True, help="Skriv linjenummer foran hver linje.")
@click.argument("filnavn")
@click.argument("prefiks", default="")
def les_fil(number, filnavn, prefiks):
    """
    Skriv PREFIKS + innholdet av fila med filstien FILNAVN til terminalen.

    Prefikset PREFIKS blir skrevet ut på starten av hver linje (etter ev.
    linjenummer), hvis angitt.
    """
    with open(filnavn) as fil:
        for linjenummer, linje in enumerate(fil, start=1):
            # Skriv linjenummer hvis aktivert
            if number:
                # Sørg for konsekvent venstremargin
                # (for filer på opptil 999 linjer)
                print(f"{linjenummer: 3d}: ", end="")
            # Skriv linja
            print(prefiks + linje, end="")

les_fil()
