FileBase := template
TEXFILE := $(FileBase).tex
PDFFILE := $(FileBase).pdf
BIBS := $(FileBase).aux #mybibliographyfile.bib
TEXENGINE=xelatex
BIBTEX=bibtex
BUILDTEX=$(TEXENGINE) $(TEXFILE)
DefaultOpen = xdg-open


all:
	$(BUILDTEX)
	$(BUILDTEX)
	$(BUILDTEX)

open: all
	$(DefaultOpen) $(PDFFILE)

clean:
	rm -f *.log *.dvi *.aux *.toc *.lof *.lot *.out *.bbl *.blg *.xmpi *.run.xml *.synctex.gz
	rm -f $(FileBase).pdf

