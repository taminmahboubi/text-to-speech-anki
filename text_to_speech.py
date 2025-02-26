import os
from gtts import gTTS
from deep_translator import GoogleTranslator

GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[0m'

# Step 1: Opening and printing the contents of a .txt file

input_file="example.txt"


with open(input_file, "r", encoding="utf-8") as file:
    words = [line.strip() for line in file if line.strip()] # Remove empty lines

# Step 2: Translate words to another language

language = "de" # English 

translator = GoogleTranslator(source='auto', target="en")

translations = {}

for word in words:
    translated_word = translator.translate(word)
    translations[word] = translated_word


print("\nTranslations:")
for original, translated in translations.items():
    print(f"{original} →  {translated}")

    
# Step 3: Generate Audio files from translations

output_folder = "output_audio"
os.makedirs(output_folder, exist_ok=True)

for original, translated in translations.items():
    tts = gTTS(original, lang=language)
    filename = os.path.join(output_folder, original.replace(" ", "_") + ".mp3")
    tts.save(filename)
    print(f"\nAudio file: {translated}.mp3 → {GREEN}Created successfully!{RESET}")

