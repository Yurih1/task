#!/bin/bash
# wait-for-it.sh

set -e

host="$1"
shift
cmd="$@"

for i in {1..30}; do
  if mysql -h "$host" -u "$DB_USER" -p"$DB_PASSWORD" -e "SELECT 1" >/dev/null 2>&1; then
    >&2 echo "MySQL is up - executing command"
    exec $cmd
  fi
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 2
done

>&2 echo "MySQL did not become available in time"
exit 1