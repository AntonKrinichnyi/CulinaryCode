#!/user/bin/env bash
#Exit on error

set -o errexit

pip install -r requirements.txt

# Convert static assert files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate