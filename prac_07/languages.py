from prac_07.ProgrammingLanguage import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
list_of_languages = [ruby, python, visual_basic]

print(python)
for language in list_of_languages:
    if language.is_dynamic() is True:
        print(language.name)

