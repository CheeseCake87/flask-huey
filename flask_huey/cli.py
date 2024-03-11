import click


@click.group()
def cli():
    pass  # Entry Point


@cli.command()
def not_implemented():
    click.echo('No commands implemented yet')
