FROM python:3.8
ADD invertory_2.py
run pip install tabulate
CMD["python", ./inventory_2.py]
