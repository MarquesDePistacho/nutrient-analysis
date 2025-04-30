# src/nutrient_analysis/main.py

import click

@click.group()
def cli():
    """Инструмент для анализа нутриентов"""
    pass

@cli.command()
@click.argument('name')
def hello(name):
    """Приветствие по имени"""
    click.echo(f"Привет, {name}! Добро пожаловать в nutrient-analysis!")

@cli.command()
def version():
    """Выводит версию проекта"""
    click.echo("nutrient-analysis version 0.0.1")
