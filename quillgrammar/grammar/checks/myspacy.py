import os
import spacy
from spacy.tokens.doc import Doc

from ..utils import Error

spacy_path = os.environ["SPACY_GRAMMAR_PATH"]
nlp = spacy.load(spacy_path)


class SpaCyGrammarChecker:

    # SpaCy's grammar labels are the NER labels that are not in allcaps
    candidate_checks = set([label for label in nlp.get_pipe("ner").labels if label != label.upper()])

    def __init__(self, config={}):
        self.unclassified = False
        self.name = "spaCy"
        self.config = config
        self.error_types = set([e for e in config.get("errors", [])
                                if e in self.candidate_checks])

        print("Initialized spaCy-based Error Check for these errors:")
        for error_check in self.candidate_checks:
            if error_check in self.error_types:
                print(f"[x] {error_check}")
            else:
                print(f"[ ] {error_check}")

    def check(self, doc: Doc, prompt=""):
        errors = []
        for entity in doc.ents:
            if not self.config or entity.label_ in self.error_types:
                error = Error(text=entity.text,
                              index=entity.start_char,
                              error_type=entity.label_,
                              model=self.name)

                errors.append(error)

        return errors
