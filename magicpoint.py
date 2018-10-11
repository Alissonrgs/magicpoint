#!/usr/bin/env python
import argparse

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from prettytable import PrettyTable
from random import randint

parser = argparse.ArgumentParser(
    prog='magicpoint.py',
    description='Get magic point times!'
)
parser.add_argument(
    '-m', '--month', type=int, help='an integer for the month')
parser.add_argument(
    '-y', '--year', type=int, help='an integer for the year')
parse = parser.parse_args()

point_table = PrettyTable()
point_table.field_names = [
    "DATA",
    "ENTRADA",
    "INTERVALO SAIDA",
    "INTERVALO RETORNO",
    "SAIDA",
    "JUSTIFICATIVA"
]


def get_magic_point(month, year):
    date = datetime(day=1, month=month, year=year)
    end = date + relativedelta(months=1)
    date_format = "%d/%m/%Y"
    time_format = "%H:%M"

    while date < end:
        if date.weekday() == 5 or date.weekday() == 6:
            point_table.add_row([
                date.strftime(date_format),
                "", "", "", "",
                "FOLGA"
            ])
        else:
            entrada = datetime(
                day=date.day, month=date.month, year=date.year, hour=8)
            intervalo_saida = datetime(
                day=date.day, month=date.month, year=date.year, hour=12)
            intervalo_retorno = datetime(
                day=date.day, month=date.month, year=date.year, hour=13)
            saida = datetime(
                day=date.day, month=date.month, year=date.year, hour=18)
            if date.weekday() == 4:
                saida -= timedelta(hours=1)

            rand_atraso = randint(0, 1)
            rand_entrada = randint(1, 10)
            rand_saida = randint(0, 5)
            rand_intervalo_saida = randint(1, 10)
            rand_intervalo_retorno = randint(0, 3)

            if rand_atraso:
                minutes = rand_entrada
                entrada += timedelta(minutes=minutes)
                minutes += randint(0, 1) * rand_saida
                saida += timedelta(minutes=minutes)
            else:
                minutes = rand_entrada
                entrada -= timedelta(minutes=minutes)
                minutes += randint(0, 1) * rand_saida
                saida -= timedelta(minutes=minutes)

            minutes = rand_intervalo_saida
            intervalo_saida += timedelta(minutes=minutes)
            minutes += randint(0, 1) * rand_intervalo_retorno
            intervalo_retorno += timedelta(minutes=minutes)

            point_table.add_row([
                date.strftime(date_format),
                entrada.strftime(time_format),
                intervalo_saida.strftime(time_format),
                intervalo_retorno.strftime(time_format),
                saida.strftime(time_format),
                ""
            ])
        date += timedelta(days=1)
    print(point_table)


if __name__ == "__main__":
    get_magic_point(parse.month, parse.year)
