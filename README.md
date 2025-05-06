# Biomedical NER Annotation

This repository contains a Python script that performs Named Entity Recognition (NER) on biomedical text stored in an Excel file and outputs the annotated results in both Markdown and JSON formats. Entities are colored for easy visualization.

## Features

* **Biomedical NER** using the `en_ner_bionlp13cg_md` model from ScispaCy.
* **Markdown Annotation**: Text spans are wrapped in HTML `<span>` tags with inline colors for preview in Markdown viewers.
* **JSON Export**: Detailed entity information (text, label, character offsets, color) saved in JSON.
* **Batch Processing**: Iterates over all rows and columns in an input Excel file.

## Requirements

* Python 3.7 or higher
* [pandas](https://pandas.pydata.org/)
* [spacy](https://spacy.io/)
* [scispacy](https://allenai.github.io/scispacy/)
* ScispaCy model: `en_ner_bionlp13cg_md`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/biomedical-ner-annotation.git
   cd biomedical-ner-annotation
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install pandas spacy scispacy openpyxl
   python -m spacy download en_ner_bionlp13cg_md
   ```

## Usage

1. Place your input Excel file in the repository root and name it `Data.xlsx` (or modify the script to point to your file).
2. Run the annotation script:

   ```bash
   python annotate_biomedical_entities.py
   ```
3. After execution, two files will be generated:

   * `Annotated_Text.md` – Annotated text with colored entities in Markdown format.
   * `Annotated_Text.json` – Structured JSON with entity details.

## Example

```markdown
**Row 0, Column 'Abstract':**
This study investigates the role of <span style="color:red; font-weight:bold">BRCA1</span> mutations in breast cancer progression.
```

## Markdown Preview

Below is a screenshot of the annotated Markdown rendered in a compatible viewer (e.g., VS Code, GitHub, or a Markdown preview extension).

![Markdown Preview](./assets/markdown_preview.png)

## Output Files

* **Annotated\_Text.md**: Contains sections for each row and column, separated by horizontal rules (`---`).
* **Annotated\_Text.json**: JSON object where each key corresponds to a cell (e.g., `Row_0_Col_Abstract`) and its value contains entity metadata.
