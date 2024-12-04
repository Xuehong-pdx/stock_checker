FROM  python:3.13-slim-bullseye
WORKDIR /stock_checker
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3", "get_stock.py" ]