FROM  python:3
WORKDIR /get_stock
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3", "get_stock.py" ]

