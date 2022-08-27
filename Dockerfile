FROM python:3.10.6-alpine as build-stage
ENV PYTHONUNBUFFERED 1
WORKDIR /opt/venv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip3 install persuader-technology-automata-api

FROM python:3.10.6-alpine as container-stage
WORKDIR /opt/venv
COPY --from=build-stage /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
CMD ["automata-api-start"]


