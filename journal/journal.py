# TODO: add docstrings!

import os
import datetime

def load(name):
    data = []
    filename = get_path(name)

    if os.path.exists(filename):
        with open(filename, 'r') as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_path(name)
    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_path(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    entry_time = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    journal_data.append(f'[{entry_time}]  {text}')
