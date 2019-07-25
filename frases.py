
from googletrans import Translator

text=("Análise de dados do arquivo")
destination_language = {
    "Spanish": "es",
    "Chinese":"zh-CN",
    "Italian":"it",
    "Portuguese":"pt"
}
translator=Translator()
for key, value in destination_language.items():
    print(translator.translate(text, dest=value).text)
