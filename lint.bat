python -m autoflake --in-place --remove-all-unused-imports --ignore-init-module-imports -r units_calculator
python -m isort --profile black units_calculator tests setup.py
python -m black units_calculator tests setup.py
python -m mypy --strict units_calculator tests setup.py
python -m pylint units_calculator setup.py
