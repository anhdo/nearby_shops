#!/bin/sh

# Stop if there is any error in the pipeline
set -e
# The first arg is the db host
host="$1"
# Get the rest of the arguments
shift
cmd="$@"

until PGPASSWORD="docker" psql -h "$host" -U "docker" -c '\q' gis; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
