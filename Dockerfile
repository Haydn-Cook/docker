FROM python:3.8
COPY Task_manager_2.py .
COPY tasks.txt .
COPY user.txt .
run pip install datetime
CMD python inventory_2.py