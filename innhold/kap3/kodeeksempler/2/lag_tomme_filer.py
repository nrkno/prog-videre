import os

import click


@click.command()
@click.argument("filnavn", nargs=-1)
def lag_tomme_filer(filnavn):
    for enkeltfil in filnavn:
        if os.path.exists(enkeltfil):
            prompt = f"{enkeltfil} finnes fra før. Vil du slette innholdet i fila?"
            if not click.confirm(prompt, default=True):
                print(f"Hopper over {enkeltfil}")
                continue
        with open(enkeltfil, "w"):
            pass


lag_tomme_filer()
