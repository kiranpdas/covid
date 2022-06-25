FROM python:3.7

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/kpra_covid"

CMD ["python", "kpra_covid/main.py", "-c=kpra_covid/resources/config.json"]
