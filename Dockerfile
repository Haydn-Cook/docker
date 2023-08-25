FROM python:3.8
COPY inventory_2.py .
COPY inventory.txt .
run pip install tabulate
CMD python inventory_2.py
