FROM rust:1.72
WORKDIR /app
COPY . .
RUN cargo build --release
CMD ["/app/target/release/pod-orderbook-svc"]
