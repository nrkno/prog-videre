import click


@click.command()
@click.option("--number", "-n", is_flag=True, help="Skriv linjenummer foran hver linje.")
@click.option("--min-length", metavar="LENGDE", default=0, help="Hopp over linjer med færre tegn enn LENGDE.")
@click.argument("filnavn")
@click.argument("prefiks", default="")
def les_fil(number, min_length, filnavn, prefiks):
    """
    Skriv PREFIKS + innholdet av fila med filstien FILNAVN til terminalen.

    Prefikset PREFIKS blir skrevet ut på starten av hver linje (etter ev.
    linjenummer), hvis angitt.
    """
    with open(filnavn) as fil:
        for linjenummer, linje in enumerate(fil, start=1):
            # Hopp over linjer med for få tegn
            antall_tegn_før_linjeskift = len(linje.rstrip())
            if antall_tegn_før_linjeskift < min_length:
                continue

            # Skriv linjenummer hvis aktivert
            if number:
                # Sørg for konsekvent venstremargin
                # (for filer på opptil 999 linjer)
                print(f"{linjenummer: 3d}: ", end="")
            # Skriv linja
            print(prefiks + linje, end="")

les_fil()
