# Extract Cited BibTeX Entries

This Python script extracts only the cited BibTeX entries from a `.bib` file based on citations found in a LaTeX document. It helps streamline your bibliography by including only the references you actually use in your paper.

## Features

- Parses LaTeX files to find all `\cite{}` commands.
- Ignores citations in commented lines.
- Extracts only the cited entries from a BibTeX file.
- Outputs a new `.bib` file containing only the used references.

## Requirements

- Python 3.x

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/extract-cited-bib.git
cd extract-cited-bib
```

## Usage

Run the script using the command line, specifying your LaTeX file, BibTeX file, and desired output file:

```bash
python extract_cited_bib.py <latex_file> <bib_file> <output_file>
```

### Example

```bash
python extract_cited_bib.py document.tex reference.bib cited_references.bib
```

This command will create `cited_references.bib`, containing only the BibTeX entries cited in `document.tex`.

## Acknowledgments
This tool was fully written with the assistance of ChatGPT by OpenAI.