FROM python:3.10.6-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./apiautomata ./apiautomata

# todo: non-root user

ENV PYTHONPATH="${PYTHONPATH}:/app/apiautomata"
CMD ["python", "-v"]
