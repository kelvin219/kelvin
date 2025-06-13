FROM ubuntu:22.04
RUN apt-get update && apt-get install -y build-essential
COPY . /app
WORKDIR /app
RUN make
CMD ["./marketdata_ingest"]
