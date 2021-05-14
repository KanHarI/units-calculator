python -m autoflake --in-place --remove-all-unused-imports --ignore-init-module-imports -r units_calculator --exclude all.py
python -m isort --profile black units_calculator tests setup.py
python -m black units_calculator tests setup.py
python -m mypy --strict --implicit-reexport units_calculator tests setup.py
python -m pylint units_calculator setup.py
