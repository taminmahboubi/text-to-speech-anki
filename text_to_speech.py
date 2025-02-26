from gtts import gTTS
from deep_translator import GoogleTranslator

input_file="example.txt"


with open(input_file, "r", encoding="utf-8") as file:
    words = [line.strip() for line in file if line.strip()] # Remove empty lines

language = "de" # German 

translator = GoogleTranslator(source='auto', target=language)

translations = {}

for word in words:
    translated_word = translator.translate(word)
    translations[word] = translated_word


print("\nTranslations:")
for original, translated in translations.items():
    print(f"{original} →  {translated}")

    