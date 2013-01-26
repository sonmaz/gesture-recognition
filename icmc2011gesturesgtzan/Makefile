all: clean icmc2011gesturesgtzan.pdf

clean:
	rm -f *toc *aux *out *log *bbl *blg

icmc2011gesturesgtzan.pdf: icmc2011gesturesgtzan.tex icmc2011gesturesgtzan.bib
	/usr/bin/pdflatex -file-line-error -halt-on-error icmc2011gesturesgtzan.tex && bibtex icmc2011gesturesgtzan && /usr/bin/pdflatex -file-line-error -halt-on-error icmc2011gesturesgtzan.tex && /usr/bin/pdflatex -file-line-error -halt-on-error icmc2011gesturesgtzan.tex
