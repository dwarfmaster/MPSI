NAME=main
TEX=$(NAME).tex
EXT=pdf
OUTPUT=build/
OUTNAME=$(OUTPUT)$(NAME)
DEST=$(OUTNAME).pdf
TEXARG=-output-directory $(OUTPUT)

all : remove $(DEST)

$(OUTNAME).dvi : $(TEX) *.tex
	latex $(TEXARG) $<

$(OUTNAME).ps : $(NAME).dvi
	dvips $<

$(OUTNAME).pdf : $(TEX) *.tex
	pdflatex $(TEXARG) $<

clean :
	rm -rv $(OUTPUT)/*

rec : clean all

remove :
	@touch $(OUTNAME).tmp
	rm $(OUTNAME).*

re : remove all

.PHONY: all clean rec remove re


