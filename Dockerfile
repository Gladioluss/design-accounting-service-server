FROM python:3.11.4-alpine

EXPOSE 8000

WORKDIR /src

COPY ./pyproject.toml ./poetry.lock /migrations/ /src/

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry export -f requirements.txt --output requirements.txt --without-hashes && \
    pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY . ./

CMD ["sh", "-c", "yoyo develop && poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000"]
