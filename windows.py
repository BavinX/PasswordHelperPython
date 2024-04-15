import tkinter as tk
from tkinter import filedialog
from checkerHelper import FileChecker

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Checker")
        
        self.file_label = tk.Label(root, text="Enter the file path:")
        self.file_label.pack()
        
        self.file_entry = tk.Entry(root, width=50)
        self.file_entry.pack()
        
        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.pack()
        
        self.edit_text = tk.Entry(root, width=50)
        self.edit_text.pack()
        
        self.search_button = tk.Button(root, text="Search", command=self.search_word)
        self.search_button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
        
    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(tk.END, file_path)
        
    def search_word(self):
        file_path = self.file_entry.get()
        word = self.edit_text.get()
        
        if file_path and word:
            word_count = FileChecker.count_word_occurrences(file_path, word)
            self.result_label.config(text=f"Word '{word}' found {word_count} times.")
        else:
            self.result_label.config(text="Please provide both file path and word.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
