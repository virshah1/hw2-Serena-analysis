




.PHONY: all clean

all: data/serena.csv outputs/serena_plot.png outputs/report.html outputs/report.pdf

data/SerenaWilliamsCareer.js: scripts/download.py
	python3 scripts/download.py

data/serena.csv: data/SerenaWilliamsCareer.js scripts/clean.py
	python3 scripts/clean.py

outputs/serena_plot.png: data/serena.csv scripts/plot.py
	python3 scripts/plot.py

serena_plot.png: outputs/serena_plot.png
	cp outputs/serena_plot.png serena_plot.png

outputs/report.html outputs/report.pdf &: report.qmd serena_plot.png
	/usr/local/bin/quarto render report.qmd --to all --output-dir outputs

clean:
	rm -f data/SerenaWilliamsCareer.js
	rm -f data/serena.csv
	rm -f outputs/serena_plot.png
	rm -f serena_plot.png
	rm -f outputs/report.html
	rm -f outputs/report.pdf
	rm -rf outputs/report_files

