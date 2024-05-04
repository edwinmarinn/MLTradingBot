# Script to check Lint

# Enable exit on error
set -e

mypy ./src
black ./src ./tests --check
isort --check-only ./src ./tests
