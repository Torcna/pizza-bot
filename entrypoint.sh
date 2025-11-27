#!/bin/sh
set -e

python -m bot.recreate_db_postgres
exec python -m bot