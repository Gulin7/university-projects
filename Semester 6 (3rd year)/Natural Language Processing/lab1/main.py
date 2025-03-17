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
        
        # Filtered text (without stopwords, punctuation, and spaces)
        filtered_text = " ".join([token.text for token in doc if not token.is_stop and not token.is_punct and not token.is_space])

        # Processed text (returning token text and POS)
        processed_text = [(token.text, token.pos_) for token in doc if not token.is_stop and not token.is_punct and not token.is_space]

        return filtered_text, processed_text

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

    """
    Writes the original, filtered, and processed texts to the output file
    """
    def writeToFile(self, output_filename, texts, filtered_texts, processed_texts):
        try:
            with open(output_filename, "w", encoding="utf-8") as output_file:
                for i, (original, filtered, processed) in enumerate(zip(texts, filtered_texts, processed_texts)):
                    output_file.write(f"Text index is: {i+1}\n")
                    output_file.write(f"Original text: {original}\n")
                    output_file.write(f"Filtered text: {filtered}\n")
                    output_file.write(f"Processed text: {processed}\n")
                    output_file.write("-" * 50 + "\n")
        except Exception as e:
            print(f"Error writing to file '{output_filename}': {e}")

if __name__ == "__main__":
    text_preprocessor = TextPreprocessor()

    # Read texts from files
    english_texts = text_preprocessor.readTextsFromFile("english.txt")
    romanian_texts = text_preprocessor.readTextsFromFile("romanian.txt")

    # Assign languages
    texts = english_texts + romanian_texts
    languages = ["en"] * len(english_texts) + ["ro"] * len(romanian_texts)

    # Process texts
    filtered_texts = []
    processed_texts = []

    for text, lang in zip(texts, languages):
        filtered, processed = text_preprocessor.preprocessText(text, lang)
        filtered_texts.append(filtered)
        processed_texts.append(processed)

    # Write the results to an output file
    text_preprocessor.writeToFile("output.txt", texts, filtered_texts, processed_texts)

    # Optionally, print the results
    for i, (original, filtered, processed) in enumerate(zip(texts, filtered_texts, processed_texts)):
        print(f"Text index is: {i+1}")
        print(f"Original text: {original}")
        print(f"Filtered text: {filtered}")
        print(f"Processed text: {processed}")
        print("-" * 50)
