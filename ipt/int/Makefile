NAME=cours
TEX=$(NAME).tex

all: $(TEX)
	pdflatex $<

clean:
	@touch $(NAME)-s.asy
	@rm -f $(NAME)-*
	@rm -f $(NAME)*.{asy,pre,aux,log,pdf}

rec: clean all

.PHONY:all clean rec

