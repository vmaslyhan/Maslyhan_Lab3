from package import module1 as m1

print("Демонстрація роботи module1")

print("\nПереклад:")
text = "Добрий день"
translated = m1.TransLate(text, "uk", "en")
print(f"Оригінал: {text}")
print(f"Переклад: {translated}")

print("\nВизначення мови:")
detected = m1.LangDetect("Bonjour", "all")
print(detected)

print("\nКод/назва мови:")
print("uk -", m1.CodeLang("uk"))
print("english -", m1.CodeLang("english"))

print("\nСписок мов (екран):")
m1.LanguageList("screen", "Привіт")

print("\nСписок мов (у файл):")
m1.LanguageList("file", "Привіт")
print("Таблиця мов записана у файл languages.txt")