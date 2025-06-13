CXX ?= g++
CXXFLAGS += -O2 -std=c++11
TARGET = marketdata_ingest
SRCS = $(wildcard src/*.cpp)

all: $(TARGET)

$(TARGET): $(SRCS)
$(CXX) $(CXXFLAGS) -o $@ $^

clean:
rm -f $(TARGET)
