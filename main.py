from typing import List

import spacy


def ner(text: str, lang: str) -> List[dict]:
    model = spacy.load("xx_ent_wiki_sm")
    doc = model(text)
    entities = [
        {
            "text": ent.text,
            "type": ent.label_,
            "start_pos": ent.start_char,
            "end_pos": ent.end_char,
        } for ent in doc.ents
    ]
    return entities


if __name__ == '__main__':
    print(ner("Apple is looking at buying U.K. startup for $1 billion", "en"))
    print(ner("El sombrío Prudhon, imbuído, sin duda, en las ideas de los Santos "
              "Padres de la Iglesia que predicaban el desden por los bienes", "any"))
