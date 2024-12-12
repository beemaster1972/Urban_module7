import re


class WordsFinder:

    def __init__(self, *args):
        self.file_names = []
        for fn in args:
            if isinstance(fn, str):
                self.file_names.append(fn)

    def get_all_words(self) -> dict:
        self.all_words = {}
        # delimiters = [',', '.', '=', '!', '?', ';', ':', ' - ']
        pattern = r"[,.=!?;:\s\n-]"
        for fn in self.file_names:
            with open(fn, 'r', encoding='utf-8') as f:
                self.all_words[fn] = re.split(pattern, f.read().lower())
        return self.all_words

    def find(self, word: str):
        result = {}
        for key, val in self.all_words.items():
            result[key] = val.index(word.lower())
        return result

    def count(self, word: str):
        result = {}
        for key, val in self.all_words.items():
            result[key] = val.count(word.lower())
        return result


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего