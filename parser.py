import spacy

# Load a small English model (install via `python -m spacy download en_core_web_sm`)
try:
    # Attempt to load the small English model; fallback to blank model if unavailable
    _nlp = spacy.load("en_core_web_sm")
except (ImportError, OSError):
    _nlp = spacy.blank("en")

def parse_event_description(text: str) -> list:
    """
    Use NLP to extract named entities from unstructured event description text.
    Returns a list of dicts with 'text' and 'label'.
    """
    doc = _nlp(text)
    return [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]