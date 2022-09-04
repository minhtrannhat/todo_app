FROM python:3.10

WORKDIR /app/
# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Install  dependencies
COPY pyproject.toml poetry.lock /app/
# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=true
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

# Copy content
COPY . /app

ARG SQLALCHEMY_DB_URL
ENV SQLALCHEMY_DB_URL $SQLALCHEMY_DB_URL

EXPOSE 8000
