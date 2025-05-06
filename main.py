import pandas as pd
import spacy
import scispacy
import json

# Load the biomedical NER model
nlp = spacy.load("en_ner_bionlp13cg_md")

# Color pool
COLOR_TAGS = ["red", "green", "blue", "orange", "purple", "teal", "yellow", "pink"]

def assign_colors(entities):
    unique_entities = sorted(set(ent.text for ent in entities), key=str.lower)
    color_map = {}
    for i, ent_text in enumerate(unique_entities):
        color_map[ent_text.lower()] = COLOR_TAGS[i % len(COLOR_TAGS)]
    return color_map

def get_annotated_markdown(text: str, nlp_model) -> str:
    doc = nlp_model(text)
    ents = list(doc.ents)
    color_map = assign_colors(ents)

    offset = 0
    annotated_text = text
    for ent in ents:
        start = ent.start_char + offset
        end = ent.end_char + offset
        color = color_map[ent.text.lower()]
        replacement = f'<span style="color:{color}; font-weight:bold">{ent.text}</span>'
        annotated_text = annotated_text[:start] + replacement + annotated_text[end:]
        offset += len(replacement) - len(ent.text)

    return annotated_text

def get_annotated_json(text: str, nlp_model) -> dict:
    doc = nlp_model(text)
    ents = list(doc.ents)
    color_map = assign_colors(ents)

    entities_info = []
    for ent in ents:
        entities_info.append({
            "text": ent.text,
            "label": ent.label_,
            "start_char": ent.start_char,
            "end_char": ent.end_char,
            "color": color_map[ent.text.lower()]
        })

    return {
        "original_text": text,
        "annotated_entities": entities_info
    }

# ---------- MAIN EXECUTION ----------

df = pd.read_excel("Data.xlsx")
annotated_md_lines = []
annotated_json_all = {}

for i, row in df.iterrows():
    for col in df.columns:
        cell_text = str(row[col])
        annotated_md = get_annotated_markdown(cell_text, nlp)
        annotated_json = get_annotated_json(cell_text, nlp)

        # Markdown output
        annotated_md_lines.append(f"**Row {i}, Column '{col}':**\n{annotated_md}\n")

        # JSON output
        annotated_json_all[f"Row_{i}_Col_{col}"] = annotated_json

# Save to Markdown
with open("Annotated_Text.md", "w", encoding="utf-8") as f_md:
    f_md.write("\n---\n".join(annotated_md_lines))

# Save to JSON
with open("Annotated_Text.json", "w", encoding="utf-8") as f_json:
    json.dump(annotated_json_all, f_json, indent=2)

print("Annotated all rows and columns. Outputs saved to Annotated_Text.md and Annotated_Text.json.")
