import spacy
from spacy import displacy

nlp_en = spacy.load("en_core_web_sm")
nlp_ro = spacy.load("ro_core_news_sm")

def preprocess_text(text, lang="en"):
    if lang == "en":
        nlp = nlp_en
    elif lang == "ro":
        nlp = nlp_ro
    else:
        raise ValueError("Unsupported language. Choose 'en' or 'ro'.")

    doc = nlp(text.lower())

    processed_tokens = [
        (token.text, token.pos_)
        for token in doc
        if not token.is_stop and not token.is_punct and not token.is_space
    ]

    return processed_tokens

texts = [
    # English texts
    "Artificial intelligence is rapidly evolving, with machine learning models becoming more sophisticated. Researchers are constantly exploring new algorithms to improve accuracy and efficiency.",
    "Quantum computing has the potential to revolutionize cryptography, enabling secure communication through principles of quantum mechanics that prevent data interception.",
    "Climate change remains one of the most pressing global issues, as rising temperatures contribute to extreme weather events, biodiversity loss, and economic instability.",
    "The philosophical debate between determinism and free will has persisted for centuries, with neuroscientific research offering new perspectives on human decision-making processes.",
    "In the digital age, data privacy has become a critical concern, as corporations collect vast amounts of user information to enhance predictive analytics and targeted advertising.",

    # Romanian texts
    "Inteligența artificială evoluează rapid, iar modelele de învățare automată devin din ce în ce mai sofisticate. Cercetătorii explorează constant noi algoritmi pentru a îmbunătăți acuratețea și eficiența.",
    "Calculul cuantic are potențialul de a revoluționa criptografia, permițând comunicarea securizată prin principii ale mecanicii cuantice care împiedică interceptarea datelor.",
    "Schimbările climatice rămân una dintre cele mai presante probleme globale, deoarece creșterea temperaturilor contribuie la fenomene meteorologice extreme, pierderea biodiversității și instabilitate economică.",
    "Dezbaterea filozofică dintre determinism și liberul arbitru persistă de secole, iar cercetările în neuroștiințe oferă perspective noi asupra proceselor de luare a deciziilor umane.",
    "În era digitală, confidențialitatea datelor a devenit o preocupare esențială, deoarece corporațiile colectează cantități uriașe de informații despre utilizatori pentru a îmbunătăți analiza predictivă și publicitatea direcționată."
]

languages = ["en"] * 5 + ["ro"] * 5

processed_texts = [preprocess_text(text, lang) for text, lang in zip(texts, languages)]

for i, (original, processed) in enumerate(zip(texts, processed_texts)):
    print(f"Original: {original}")
    print(f"Processed: {processed}")
    print("-" * 50)
