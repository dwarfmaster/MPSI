
OUTPUT=output.pdf
ASYSCRIPT=func.asy
ASY=asy -noV -noprc -f pdf

all : $(OUTPUT)

$(OUTPUT) : $(ASYSCRIPT)
	$(ASY) $(ASYSCRIPT) -o $@

clean :
	@touch $(OUTPUT)
	rm $(OUTPUT)

rec : clean all

.PHONY: all clean rec


