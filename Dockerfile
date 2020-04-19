FROM python:3

COPY bin/exe_covid.sh ./bin/
COPY main.py .
COPY src ./src
COPY resources ./resources
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["sh", "bin/exe_covid.sh"]
