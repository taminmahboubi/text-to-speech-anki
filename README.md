# text-to-speech-anki
Convert text to speech files (from Google Translate) and put them into a Deck of Flashcards in the software Anki

First we want to open a .txt file, printing each line:

```python
with open("example.txt, "r") as file:
    for line in file:
        print(line.strip())
```
and create a `.txt` file with some lines in it.

