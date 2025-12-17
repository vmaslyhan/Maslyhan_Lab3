import os
import json
import re
from package import module1, module2, module3

def count_stats(text: str):
    chars = len(text)
    words = len(text.split())
    sentences = len(re.split(r'[.!?]', text)) - 1
    return chars, words, sentences

def load_module(name: str):
    if name == "module1":
        return module1
    elif name == "module2":
        return module2
    elif name == "module3":
        return module3
    else:
        raise ValueError("Невідомий модуль")

def main():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)

        filename = config["filename"]
        lang = config["language"]
        module_name = config["module"]
        output = config["output"]
        max_chars = config["max_chars"]
        max_words = config["max_words"]
        max_sentences = config["max_sentences"]

        if not os.path.exists(filename):
            print("Помилка: файл не знайдено")
            return

        with open(filename, "r", encoding="utf-8") as f:
            full_text = f.read()

        file_size = os.path.getsize(filename)
        chars, words, sentences = count_stats(full_text)

        detected_lang = module3.LangDetect(full_text, "lang")

        print("\nІнформація про файл")
        print(f"Назва файлу: {filename}")
        print(f"Розмір файлу: {file_size} байт")
        print(f"Кількість символів: {chars}")
        print(f"Кількість слів: {words}")
        print(f"Кількість речень: {sentences}")
        print(f"Мова тексту: {detected_lang}")

        selected_text = ""
        char_count, word_count, sent_count = 0, 0, 0

        for sentence in re.split(r'(?<=[.!?]) +', full_text):
            if (char_count + len(sentence) > max_chars or
                word_count + len(sentence.split()) > max_words or
                sent_count + 1 > max_sentences):
                break
            selected_text += sentence + " "
            char_count += len(sentence)
            word_count += len(sentence.split())
            sent_count += 1

        module = load_module(module_name)

        translated = module.TransLate(selected_text.strip(), "auto", lang)

        if output == "screen":
            print("\nРезультат перекладу")
            print(f"Мова перекладу: {lang}")
            print(f"Модуль: {module_name}")
            print("Текст перекладу:")
            print(translated)
        elif output == "file":
            new_filename = f"{os.path.splitext(filename)[0]}_{lang}.txt"
            with open(new_filename, "w", encoding="utf-8") as f:
                f.write(translated)
            print(f"\nПереклад записано у файл {new_filename}")
        else:
            print("Помилка: невідомий параметр output")

    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()
