import re
import argparse

def extract_citations(latex_file):
    with open(latex_file, 'r') as f:
        text = f.read()

    # Remove comments
    text = re.sub(r'%.*', '', text)

    # Find citations
    citations = re.findall(r'\\cite\{([^}]+)\}', text)
    citation_list = set()
    for citation in citations:
        citation_list.update(citation.split(','))

    return citation_list

def extract_bib_items(bib_file, citations):
    with open(bib_file, 'r') as f:
        lines = f.readlines()

    output = []
    current_entry = []
    inside_entry = False
    entry_key = None

    for line in lines:
        if line.startswith('@'):
            if inside_entry:
                # End of the previous entry
                if entry_key in citations:
                    output.extend(current_entry)
                current_entry = []
            inside_entry = True
            entry_key = re.search(r'\{([^,]+),', line).group(1)

        if inside_entry:
            current_entry.append(line)

    # Check the last entry
    if inside_entry and entry_key in citations:
        output.extend(current_entry)

    return output

def write_output(output_file, bib_items):
    with open(output_file, 'w') as f:
        f.writelines(bib_items)

def main():
    parser = argparse.ArgumentParser(description='Extract cited BibTeX entries from a LaTeX file.')
    parser.add_argument('latex_file', help='The LaTeX file to process')
    parser.add_argument('bib_file', help='The BibTeX file to process')
    parser.add_argument('output_file', help='The output file for cited references')

    args = parser.parse_args()

    citations = extract_citations(args.latex_file)
    bib_items = extract_bib_items(args.bib_file, citations)
    write_output(args.output_file, bib_items)

if __name__ == '__main__':
    main()
