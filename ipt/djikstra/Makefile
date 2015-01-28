OBJS=main.o graph.o
CXXFLAGS=-Wall -Wextra
LDFLAGS=
PROG=graph.prog
CC=g++

all: $(PROG)

$(PROG) : $(OBJS)
	$(CC) $(CXXFLAGS) $^ -o $@ $(LDFLAGS)

%.o : %.cpp
	$(CC) $(CXXFLAGS) -c $< -o $@

clean:
	rm $(OBJS)

rec : clean all

.PHONY:all clean rec


