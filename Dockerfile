FROM python:3

ADD src /src
ADD csv /csv

RUN pip install coverage

CMD [ "python", "./src/TestCalculator.py" ]