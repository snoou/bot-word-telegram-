from googletrans import Translator

translator = Translator()
text = ['iran']
mean = []
for word in text :
    translated = translator.translate(word, dest='fa')
    mean.append(word +' '+str(translated.text)) 
print(mean)
