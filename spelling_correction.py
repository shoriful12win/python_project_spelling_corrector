from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()
    
    def correct_text(self, text):
        words = text.split()
        corrected_words = []
        
        for word in words:
           
            corrected_word = self.spell.correction(word)
            
            
            if corrected_word is None:
                corrected_word = word
                
           
            if corrected_word != word.lower():
                print(f'correcting "{word}" to "{corrected_word}"')
            
          
            corrected_words.append(corrected_word)

        
        return ' '.join(corrected_words)


    def run(self):
        print("\n_____SpellChecker___")

        while True:
            text = input('ENTER TEXT TO CHECK(or type "exit" to quit): ')
            if text.lower() == 'exit':
                print("CLOSING THE APP____")
                break
            
            correct_text = self.correct_text(text)  
            print(f'Corrected text: {correct_text}\n')          

if __name__ == '__main__':
    SpellCheckerApp().run()