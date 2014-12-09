PROG=gauss.prog
CC=ghc
FLAGS=
OBJS=gauss.o

all : $(PROG)

$(PROG) : $(OBJS)
	$(CC) $(FLAGS) $^ -o $@

%.o : %.hs
	$(CC) $(FLAGS) -c $< -o $@

clean :
	@touch $(OBJS) $(PROG)
	@rm -v $(OBJS) $(PROG)

rec : clean all

.PHONY:all clean rec


