from package import module2 as m2

print("Демонстрація роботи module2")

text = "Добрий день, як справи?"
translated = m2.TransLate(text, "uk", "en")
print(f"Оригінал: {text}")
print(f"Переклад: {translated}")

print("\nВизначення мови:")
detected = m2.LangDetect("Hello", "all")
print(detected)

print("\nКод/назва мови:")
print("en -", m2.CodeLang("en"))
print("german -", m2.CodeLang("german"))

print("\nСписок мов (екран):")
m2.LanguageList("screen", "Привіт")

print("\nСписок мов (у файл):")
m2.LanguageList("file", "Привіт")
print("Таблиця мов записана у файл languages2.txt")