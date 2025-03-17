import spacy
import ast
from tabulate import tabulate
from nltk import Tree
from io import StringIO

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

        filtered_tokens = []
        token_info = []
        named_entities = []

        for token in doc:
            if not token.is_stop and not token.is_punct and not token.is_space:
                filtered_tokens.append(token.text)  # Store filtered tokens
                gender = token.morph.get("Gender", "N/A")
                number = token.morph.get("Number", "N/A")
                person = token.morph.get("Person", "N/A")
                tense = token.morph.get("Tense", "N/A")

                token_info.append({
                    "text": token.text,
                    "lemma": token.lemma_,
                    "pos": token.pos_,
                    "tag": token.tag_,
                    "gender": gender,
                    "number": number,
                    "person": person,
                    "tense": tense
                })
        
        # Extract named entities
        for ent in doc.ents:
            named_entities.append({
                "text": ent.text,
                "label": ent.label_
            })

        filtered_text = " ".join(filtered_tokens)
        return filtered_text, token_info, named_entities, doc

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
    Writes the original, filtered text, lemma, POS, tag information, and named entities to the output file
    """
    def writeToFile(self, output_filename, texts, filtered_texts, processed_texts, named_entities, dependency_trees):
        try:
            with open(output_filename, "w", encoding="utf-8") as output_file:
                for i, (original, filtered, processed, entities, dep_tree) in enumerate(zip(texts, filtered_texts, processed_texts, named_entities, dependency_trees)):
                    output_file.write(f"Text index is: {i+1}\n")
                    output_file.write(f"Original text: {original}\n")
                    output_file.write(f"Filtered text: {filtered}\n")

                    token_table = []
                    for token in processed:
                        token_table.append([token['text'], token['lemma'], token['pos'], token['tag'], token['gender'], token['number'], token['person'], token['tense']])

                    output_file.write(tabulate(token_table, headers=["Token", "Lemma", "POS", "Tag", "Gender", "Number", "Person", "Tense"], tablefmt="grid"))
                    output_file.write("\n" + "-" * 30 + "\n")

                    # Write Named Entities to the file
                    output_file.write(f"Named Entities: \n")
                    if entities:
                        for ent in entities:
                            output_file.write(f"- {ent['text']} ({ent['label']})\n")
                    else:
                        output_file.write("No named entities found.\n")
                    output_file.write("\n" + "-" * 30 + "\n")

                    # Write the dependency tree to the file
                    output_file.write(f"Dependency Tree for Sentence: {original}\n")
                    output_file.write(dep_tree)
                    output_file.write("\n" + "=" * 30 + "\n")
        except Exception as e:
            print(f"Error writing to file '{output_filename}': {e}")

    """
    Convert spaCy's dependency tree to an NLTK tree for visualization
    """
    def to_nltk_tree(self, token):
        # If the token has children, build the tree recursively
        if token.lefts or token.rights:
            return Tree(token.dep_, [self.to_nltk_tree(child) for child in token.children])
        else:
            return token.text

    """
    Convert NLTK tree to a string (for writing to the output file)
    """
    def tree_to_string(self, tree):
        # Capture the output of the pretty_print method in a string buffer
        buffer = StringIO()
        tree.pretty_print(stream=buffer)
        return buffer.getvalue()

    """
    Generate and return the dependency tree for each sentence
    """
    def generate_dependency_trees(self, doc):
        dependency_trees = []
        # Iterate over sentences in the doc
        for sent in doc.sents:
            nltk_tree = self.to_nltk_tree(sent.root)  # Convert root token to nltk tree
            tree_str = self.tree_to_string(nltk_tree)  # Get tree as a string
            dependency_trees.append(tree_str)
        return dependency_trees


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
    docs = []
    named_entities = []
    dependency_trees = []

    for text, lang in zip(texts, languages):
        filtered, processed, entities, doc = text_preprocessor.preprocessText(text, lang)
        filtered_texts.append(filtered)
        processed_texts.append(processed)
        named_entities.append(entities)
        docs.append(doc)

    # Generate dependency trees
    for doc in docs:
        dep_trees = text_preprocessor.generate_dependency_trees(doc)
        dependency_trees.extend(dep_trees)

    # Write the results to an output file
    text_preprocessor.writeToFile("output.txt", texts, filtered_texts, processed_texts, named_entities, dependency_trees)

    # Optionally, print the results in the same format to the console
    for i, (original, filtered, processed, entities, dep_tree) in enumerate(zip(texts, filtered_texts, processed_texts, named_entities, dependency_trees)):
        print(f"Text index is: {i+1}")
        print(f"Original text: {original}")
        print(f"Filtered text: {filtered}")
        print(f"Processed tokens:")
        token_table = []
        for token in processed:
            token_table.append([token['text'], token['lemma'], token['pos'], token['tag'], token['gender'], token['number'], token['person'], token['tense']])
        print(tabulate(token_table, headers=["Token", "Lemma", "POS", "Tag", "Gender", "Number", "Person", "Tense"], tablefmt="grid"))
        print("-" * 30)

        # Print Named Entities
        print("Named Entities:")
        if entities:
            for ent in entities:
                print(f"- {ent['text']} ({ent['label']})")
        else:
            print("No named entities found.")
        
        print(f"Dependency Tree for Sentence: {original}")
        print(dep_tree)
        print("=" * 30)
