DOC_DIR := latex
LATEX = latexmk
LATEX_FLAGS = -pdf -no-shell-escape -auxdir=$(DOC_DIR) -outdir=$(DOC_DIR) -quiet
MAIN_FILE = $(DOC_DIR)/main.tex
OUT_FILE = solution.pdf


.PHONY: all clean docs
all:
	@$(MAKE) docs
docs:
	@$(MAKE) $(OUT_FILE)
clean:
	-rm -rf $(addprefix $(DOC_DIR)/, \
		*.aux 	\
		*.cpt 	\
		*.log 	\
		*.lol 	\
		*.out 	\
		*.toc  	\
		*.fls 	\
		*.pdf 	\
		*.fdb_latexmk)

$(OUT_FILE): $(DOC_DIR)/*.tex
	$(LATEX) $(LATEX_FLAGS) $(MAIN_FILE) 
