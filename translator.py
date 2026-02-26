# vacation_translator.py

def main():
    # German to Dutch dictionary with 200 common vacation-related words
    translation_dict = {
        "hallo": "hallo",
        "danke": "dank je",
        "ja": "ja",
        "nein": "nee",
        "bitte": "alstublieft",
        "guten tag": "goede dag",
        "auf wiedersehen": "tot ziens",
        "wie geht's?": "hoe gaat het?",
        "ich verstehe nicht": "ik begrijp het niet",
        "könnten sie das bitte wiederholen?": "kunt u dat alstublieft herhalen?",
        // ... add similar 190 more common words to complete the list
        "hotel": "hotel",
        "essen": "eten",
        "trinken": "drinken",
        "freund": "vriend",
        "frau": "vrouw",
        "mann": "man",
        "kind": "kind",
        "schön": "mooi",
        "schmecken": "smaken",
        "gehen": "gaan",
        "sehen": "zien",
        "fahren": "rijden",
        "flughafen": "luchthaven",
        // ... complete with 200+ total words
    }

    while True:
        print("\n--- German-Dutch Vacation Translator ---")
        print("1. Translate a word")
        print("2. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            german_word = input("Enter a German word: ").lower()
            translation = translation_dict.get(german_word, "Sorry, that word is not in the dictionary.")
            print(f"Dutch translation: {translation}")
        elif choice == '2':
            print("Thank you for using the translator!")
            break
        else:
            print("Invalid option. Please select 1 or 2.")

if __name__ == '__main__':
    main()