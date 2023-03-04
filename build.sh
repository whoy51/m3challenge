#!/usr/bin/env bash

# this script is a replacement for the Makefile script for those who don't have
# it already installed.
#
# Usage:
#       buid.sh [command]
# Commands:
#       clean   Removes any generated files
#       docs    Generates a PDF file along with auxiliary files

DOC_DIR="latex"
LATEX="latexmk"
LATEX_FLAGS="-pdf -no-shell-escape -auxdir=$DOC_DIR -outdir=$DOC_DIR -quiet"
IN_FILE="$DOC_DIR/main.tex"
OUT_FILE="solution.pdf"


if [[ $# == 0 || $1 == "docs" ]]; then
    $LATEX $LATEX_FLAGS $IN_FILE
    exit
fi

if [[ "$1" == "clean" ]]; then
    rm -rf $DOC_DIR/*.aux   \
    $DOC_DIR/*.cpt        \
    $DOC_DIR/*.log        \
    $DOC_DIR/*.lol        \
    $DOC_DIR/*.out        \
    $DOC_DIR/*.toc        \
    $DOC_DIR/*.fls        \
    $DOC_DIR/*.pdf        \
    $DOC_DIR/*.fdb_latexmk
else
    echo "Unexpected argument"
    exit 1
fi

exit
