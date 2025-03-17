import spacy
import ast

class TextPreprocessor:
    def __init__(self):
        self.nlp = {
            "en": spacy.load("en_core_web_sm"),
            "ro": spacy.load("ro_core_news_sm")
        }

    """
    Process text by removing: stopwords, spaces, punctuation.
    text: String - text to be processed
    lang: String - language of the text
    """
    def preprocessText(self, text, lang="en"):
        if lang in self.nlp.keys():
            nlp = self.nlp[lang]
        else:
            raise ValueError("Input language is not supported.")

        doc = nlp(text.lower())

        return [(token.text, token.pos_) for token in doc if not token.is_stop and not token.is_punct and not token.is_space]

    """
    Reads comma-separated quoted texts from a file and returns a list.
    filename: String - file to read from
    """
    def readTextsFromFile(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = file.read().strip()
                return ast.literal_eval(f"[{data}]")
        except (SyntaxError, ValueError) as e:
            print(f"Error reading file '{filename}': {e}")
            return []

if __name__ == "__main__":
    textPreprocessor = TextPreprocessor()

    # Read texts from files
    english_texts = textPreprocessor.readTextsFromFile("english.txt")
    romanian_texts = textPreprocessor.readTextsFromFile("romanian.txt")

    # Assign languages
    texts = english_texts + romanian_texts
    languages = ["en"] * len(english_texts) + ["ro"] * len(romanian_texts)

    # Process texts
    processed_texts = [textPreprocessor.preprocessText(text, lang) for text, lang in zip(texts, languages)]

    # Display results
    for i, (original, processed) in enumerate(zip(texts, processed_texts)):
        print(f"Text index is: {i+1}")
        print(f"Original text: {original}")
        print(f"Processed text: {processed}")
        print("-" * 50)
