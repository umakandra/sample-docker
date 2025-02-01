FROM python:3.10-slim

WORKDIR /src

copy requirement.txt /src/

RUN pip install --upgrade pip  
RUN pip install -r requirement.txt

copy . /src

EXPOSE 5001

CMD ["python","api4.py"]

