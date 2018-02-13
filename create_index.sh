#!/bin/sh

pandoc -f markdown index.md -c github-pandoc.css -o index.html
