
OUTPUT=output.asy
SCRIPT=./sierp.pl
ASYSCRIPT=sierp.asy
ASY=asy -noV -noprc -f pdf

RESULTASY=output.asy.pdf
RESULTPL=output.perl.pdf

all : $(RESULTPL) $(RESULTASY)

$(RESULTPL) : $(SCRIPT)
	exec $(SCRIPT)
	$(ASY) $(OUTPUT) -o $@

$(RESULTASY) : $(ASYSCRIPT)
	$(ASY) $(ASYSCRIPT) -o $@

clean :
	@touch $(OUTPUT)
	rm $(OUTPUT)

rec : clean all

.PHONY: all clean rec


