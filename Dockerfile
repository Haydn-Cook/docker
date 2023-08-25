FROM pypy:latest
WORKDIR /app
COPY requirements.txt /app
RUN pypy -m pip install --no-cache-dir -r requirements.txt
COPY . /app
CMD pypy inventory_2.py
