# stock checker

  This is a simple for checking selected stocks using a Dash interface.  Results contains information on previous closing value, current opening value, today's high and today's low for each selected stock. 
  
## **Built with:**

* [![Python](https://img.shields.io/badge/python-3.10.6-blue.svg)](https://www.python.org/downloads/release/python-3106/)

## **Getting Started**

### **Clone repository**

    $ git clone https://github.com/Xuehong-pdx/stock_checker

* Navigate to the project folder

      $ cd stock_checker/app

* Build Docker container

      $ docker build -t stock_checker .

* Run container

      $  docker run -itp 8050:8050 stock_checker  

View page at http://localhost:8050/
