import csv
import os
import sqlite3

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Import users.csv to DB table users_user'

    def handle(self, *args, **options):
        base_dir = os.getcwd()
        csv_file = os.path.join(base_dir, 'data/users.csv')

        conn = sqlite3.connect('db.sqlite3')
        cur = conn.cursor()

        with open(csv_file, 'r') as fin:
            dr = csv.DictReader(fin)
            to_db = [
                (i['id'], i['username'], i['email'], i['role'])
                for i in dr
            ]

        cur.executemany(
            '''INSERT INTO users_user (id, username, email, role)
            VALUES (?, ?, ?, ?);''',
            to_db
        )
        conn.commit()
        conn.close()
