FROM golang:1.23
WORKDIR /app
COPY . .
RUN go build -o pod-risk-gate ./cmd
CMD ["/app/pod-risk-gate"]
