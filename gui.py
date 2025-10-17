#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from passwd_gen import gen_passwd
import os

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('default')
        
        # Main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="Password Generator", 
                                font=('Arial', 16, 'bold'))
        title_label.pack(pady=(0, 20))
        
        # Number of words input
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(pady=10)
        
        ttk.Label(input_frame, text="Number of words:").pack(side=tk.LEFT, padx=(0, 10))
        
        self.num_words_var = tk.StringVar(value="3")
        self.num_words_entry = ttk.Entry(input_frame, textvariable=self.num_words_var, 
                                          width=10)
        self.num_words_entry.pack(side=tk.LEFT)
        
        # Generate button
        self.generate_button = ttk.Button(main_frame, text="Generate Password", 
                                          command=self.generate_password)
        self.generate_button.pack(pady=20)
        
        # Password display
        password_frame = ttk.LabelFrame(main_frame, text="Generated Password", 
                                        padding="10")
        password_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.password_text = tk.Text(password_frame, height=3, width=50, 
                                     font=('Courier', 12), wrap=tk.WORD)
        self.password_text.pack(fill=tk.BOTH, expand=True)
        self.password_text.config(state=tk.DISABLED)
        
        # Copy button
        self.copy_button = ttk.Button(main_frame, text="Copy to Clipboard", 
                                      command=self.copy_to_clipboard, 
                                      state=tk.DISABLED)
        self.copy_button.pack(pady=(0, 10))
    
    def generate_password(self):
        """Generate a password using the passwd_gen module"""
        try:
            num_words = int(self.num_words_var.get())
            if num_words < 1:
                self.display_password("Error: Please enter a positive number")
                return
            
            # Get the wordlist path
            script_dir = os.path.dirname(os.path.abspath(__file__))
            wordlist_path = os.path.join(script_dir, "assets", "wordlist.txt")
            
            # Generate password using modified logic from passwd_gen
            import random
            words = []
            with open(wordlist_path) as f:
                wordlist = f.read().split('\n')
            
            for _ in range(num_words):
                word = random.choice(wordlist) + str(random.randrange(0, 9))
                words.append(word)
            
            password = '-'.join(words)
            self.display_password(password)
            self.copy_button.config(state=tk.NORMAL)
            
        except ValueError:
            self.display_password("Error: Please enter a valid number")
        except FileNotFoundError:
            self.display_password("Error: Wordlist file not found")
        except Exception as e:
            self.display_password(f"Error: {str(e)}")
    
    def display_password(self, password):
        """Display the generated password in the text widget"""
        self.password_text.config(state=tk.NORMAL)
        self.password_text.delete(1.0, tk.END)
        self.password_text.insert(1.0, password)
        self.password_text.config(state=tk.DISABLED)
    
    def copy_to_clipboard(self):
        """Copy the password to clipboard"""
        password = self.password_text.get(1.0, tk.END).strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        self.root.update()
        
        # Show feedback
        original_text = self.copy_button.cget("text")
        self.copy_button.config(text="Copied!")
        self.root.after(1500, lambda: self.copy_button.config(text=original_text))

def main():
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
