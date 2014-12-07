
scott_siam14.pdf: max_eff.png scott_siam14.tex
	pdflatex scott_siam14.tex


scott_siam14_old.pdf: max_eff.png scott_siam14_old.tex
	pdflatex scott_siam14_old.tex


force:
	pdflatex scott_siam14.tex

max_eff.png: max_eff.py
	python max_eff.py

clean:
	rm -f *.aux *.toc *.bbl *.snm *.nav *.out *.log *.pdf
	rm -f max_eff.png
