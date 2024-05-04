# Script to format source code

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place --exclude=__init__.py ./src ./tests ./scripts
black ./src ./tests ./scripts
isort ./src ./tests ./scripts
