from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        return GoogleTranslator(source=scr, target=dest).translate(text)
    except Exception as e:
        return f"Помилка: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        langs = detect_langs(text)  # список мов з ймовірностями
        main_lang = detect(text)
        if set == "lang":
            return main_lang
        elif set == "confidence":
            return str(langs[0].prob)
        return f"Мова: {main_lang}, впевненість: {langs[0].prob}"
    except Exception as e:
        return f"Помилка: {e}"

def CodeLang(lang: str) -> str:
    try:
        langs = GoogleTranslator().get_supported_languages(as_dict=True)
        if lang in langs:
            return langs[lang]
        elif lang in langs.values():
            for code, name in langs.items():
                if name == lang:
                    return code
        return "Немає у списку"
    except Exception as e:
        return f"Помилка: {e}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        langs = GoogleTranslator().get_supported_languages(as_dict=True)
        data = []
        i = 1
        for code, name in langs.items():
            if text:
                try:
                    translated = GoogleTranslator(source="auto", target=code).translate(text)
                except:
                    translated = "-"
                data.append((i, name, code, translated))
            else:
                data.append((i, name, code))
            i += 1

        if out == "screen":
            if text:
                print(f"{'N':<5}{'Language':<20}{'Code':<10}{'Text'}")
                for n, name, code, trans in data:
                    print(f"{n:<5}{name:<20}{code:<10}{trans}")
            else:
                print(f"{'N':<5}{'Language':<20}{'Code':<10}")
                for n, name, code in data:
                    print(f"{n:<5}{name:<20}{code:<10}")
        elif out == "file":
            with open("languages3.txt", "w", encoding="utf-8") as f:
                if text:
                    f.write(f"{'N':<5}{'Language':<20}{'Code':<10}{'Text'}\n")
                    for n, name, code, trans in data:
                        f.write(f"{n:<5}{name:<20}{code:<10}{trans}\n")
                else:
                    f.write(f"{'N':<5}{'Language':<20}{'Code':<10}\n")
                    for n, name, code in data:
                        f.write(f"{n:<5}{name:<20}{code:<10}\n")
        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"
