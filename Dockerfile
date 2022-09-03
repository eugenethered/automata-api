FROM python:3.10.6-alpine AS BUILDER
LABEL stage=BUILDER
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10.6-alpine
RUN addgroup apprunner && adduser apprunner -D -H -G apprunner
USER apprunner
WORKDIR /app
COPY --from=BUILDER /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --chown=apprunner:apprunner ./apiautomata ./apiautomata

ENV PYTHONPATH="${PYTHONPATH}:/app/apiautomata" \
    REDIS_SERVER_ADDRESS=127.0.0.1 \
    REDIS_SERVER_PORT=6379 \
    API_SERVER_HOST=0.0.0.0 \
    API_SERVER_PORT=8000 \
    MISSING_KEY=binance:mv:missing \
    INSTRUMENT_EXCHANGES_KEY=binance:exchange:mv:instruments \
    EXCHANGE_TRANSFORMATIONS_KEY=binance:transformation:mv:exchange \
    TRADE_TRANSFORMATIONS_KEY=binance:transformation:mv:trade \
    EXCHANGE_RATE_TIMESERIES_KEY=binance:ts:exchange-rate:{} \
    EXCHANGE_RATE_TIMESERIES_RETENTION=360000

CMD ["python", "apiautomata/__main__.py"]
