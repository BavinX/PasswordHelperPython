class FileChecker:
    @staticmethod
    def count_word_occurrences(file_path, word):
        count = 0
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for w in words:
                    if w == word:
                        count += 1
        return count
