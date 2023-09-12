import click


@click.command()
def fortsette():
    # Vi gjør oss litt dramatiske, for eksemplets skyld
    print("Alle filene vil bli slettet!!")
    click.confirm("Vil du fortsette?", default=False, abort=True)
    print("Dett var dett. Alle filene er slettet.")

fortsette()
