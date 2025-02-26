# text-to-speech-anki
Convert text to speech files (from Google Translate) and put them into a Deck of Flashcards in the software Anki

First we want to open a .txt file, printing each line:

```python
with open("example.txt, "r") as file:
    for line in file:
        print(line.strip())
```
and create a `.txt` file with some lines in it.

---

Next, we want to change the language of the text, we'll use `gTTS`

**what is `gTTS'?**
- `gTTS` stands for 'Google Text-to-Speech'
- it is a Python library, it uses Google's technology to create audio from written text


First, install the gTTS library in Terminal:
`pip install gTTS`

however, a step before that is needed, need to create an isolated environment for Python projects, setting a safe space to work with them. (prevent conflicts, maintain system stability)

For my project I'll simply do this with the command:
`python3 -m venv myvenv`

and activating it:
`source myvenv/bin/activate` 

Now the terminal can use the Python and packages specific to that virtual environment!

*To exit the virtual environment, simply type `deactivate` in Terminal*

```python
from gtts import gTTS
```
imports `gTTS` from the `gtts` library


Next we want to use GoogleTranslator to translate the text into another language so:

1. install `deep_translator` 
    - `pip install deep_translator` in Terminal
    - need to also add ```python
    from deep_translator import GoogleTranslator
    ```

We'll make adjustments to the context manager `with...as file`, adding a `list`, looping through each line in the opened file, using `stripe()` to remove any leading or trailing whitespace (spaces, tabs, newlines).

```python
input_file="example.txt"

with open(input_file, "r,", encoding="utf-8") as file:
    words = [line.stripe() for line in file if line.stripe() # Remove empty lines]
```

Next we want to set up a text translator, to translate the text into our specified language, in this case German:

```python
language = "de"

translator = GoogleTranslator(source='auto', target=language)
```

1. `language = "de"` creates a variable names language and assigns the string value of `"de"` (the language code for German)
2. `translator = GoogleTranslator(source='auto', target=language)` creates an instance (object) of the GoogleTranslator class, which allows us to translate text using Google Translate.

Next we'll create an empty Dictionary called `translations = {}`, Dictionaries are data structures that store key-value pairs. This will be used later to display the `{key}=Original text` and the `{value}=Translation`, To do this, we'll:
- loop through `words`
- get the translated word using `translator`
- store them both as `{key}{value}` pairs into `translations` Dictionary.

```python
for word in words:
    translated_word = translator.translate(word)
    translations[word] = translated_word
```

Finally we want to display our results, so:
```python
print("\nTranslations:")
for original,translated in translations.items():
    print(f"{original}  → {translated}")
```
`.items()` is essential to iterate of *key-value* pairs! if you just used `translations` then you could only iterate and obtain the *keys*!