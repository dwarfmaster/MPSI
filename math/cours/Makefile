FILE=cours.tex
TEX=pdflatex
OUT=output/
FLAGS=-no-shell-escape --output-directory=$(OUT)

all : $(FILE)
	$(TEX) $(FLAGS) $^

clean :
	@touch $(OUT)
	@rm -fr $(OUT)*
	@echo "Cleaned $(OUT)"

rec : clean all

.PHONY:all clean rec


