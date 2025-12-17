from package import module3 as m3

print("Демонстрація роботи module3")

print("\nПереклад:")
text = "Добрий день, як справи?"
translated = m3.TransLate(text, "uk", "en")
print(f"Оригінал: {text}")
print(f"Переклад: {translated}")

print("\nВизначення мови:")
detected = m3.LangDetect("Bonjour", "all")
print(detected)

print("\nКод/назва мови:")
print("fr -", m3.CodeLang("fr"))
print("spanish -", m3.CodeLang("spanish"))

print("\nСписок мов (екран):")
m3.LanguageList("screen", "Привіт")

print("\nСписок мов (у файл):")
m3.LanguageList("file", "Привіт")
print("Таблиця мов записана у файл languages3.txt")