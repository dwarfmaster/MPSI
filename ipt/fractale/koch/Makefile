
OUTPUT=output.asy
SCRIPT=./koch.pl
ASY=asy -noV -noprc -f pdf

all :
	exec $(SCRIPT)
	$(ASY) $(OUTPUT)

clean :
	@touch $(OUTPUT)
	rm $(OUTPUT)

rec : clean all

.PHONY: all clean rec


