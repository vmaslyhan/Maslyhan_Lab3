from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        result = translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Помилка: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        result = translator.detect(text)
        lang = result.lang
        if set == "lang":
            return lang
        else:
            return f"Мова: {lang}"
    except Exception as e:
        return f"Помилка: {e}"

def CodeLang(lang: str) -> str:
    try:
        if lang.lower() in LANGUAGES.values():
            for code, name in LANGUAGES.items():
                if name == lang.lower():
                    return code
        elif lang.lower() in LANGUAGES:
            return LANGUAGES[lang.lower()]
        return "Помилка: мова не знайдена"
    except Exception as e:
        return f"Помилка: {e}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        data = []
        for code, name in LANGUAGES.items():
            if text:
                try:
                    translated = translator.translate(text, dest=code).text
                except:
                    translated = "-"
                data.append((code, name, translated))
            else:
                data.append((code, name))

        if out == "screen":
            if text:
                print(f"{'Code':<10}{'Language':<20}{'Translated text'}")
                for code, name, trans in data:
                    print(f"{code:<10}{name:<20}{trans}")
            else:
                print(f"{'Code':<10}{'Language':<20}")
                for code, name in data:
                    print(f"{code:<10}{name:<20}")
        elif out == "file":
            with open("languages.txt", "w", encoding="utf-8") as f:
                if text:
                    f.write(f"{'Code':<10}{'Language':<20}{'Translated text'}\n")
                    for code, name, trans in data:
                        f.write(f"{code:<10}{name:<20}{trans}\n")
                else:
                    f.write(f"{'Code':<10}{'Language':<20}\n")
                    for code, name in data:
                        f.write(f"{code:<10}{name:<20}\n")
        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"