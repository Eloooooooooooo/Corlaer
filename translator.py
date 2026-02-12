class Translator:
    def __init__(self):
        # A dictionary for German-Dutch translations
        self.translations = {
            "Hallo": "Hallo",
            "Guten Morgen": "Goedemorgen",
            "Wie geht's?": "Hoe gaat het?",
            "Danke": "Dank je",
            "Bitte": "Alsjeblieft",
            "Ich liebe dich": "Ik hou van jou",
            "Urlaub": "Vakantie",
            "Strand": "Strand",
            "Aussicht": "Uitzicht",
            "Berge": "Bergen",
            # ... add 190 more vacation-themed words
        }

    def translate(self, word):
        return self.translations.get(word, "Ich weiß es nicht, entschuldigen Sie")

# Example of usage
if __name__ == "__main__":
    translator = Translator()
    words_to_translate = ["Hallo", "Guten Morgen", "Unbekanntes Wort"]
    for word in words_to_translate:
        print(f"{word} -> {translator.translate(word)}")
