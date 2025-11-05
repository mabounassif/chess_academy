#!/bin/bash
# Wait for PostgreSQL to be ready

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD=$PASSWORD psql -h "$host" -U "$USER" -c '\q' 2>/dev/null; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd

