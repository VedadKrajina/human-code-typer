import tkinter as tk
from tkinter import scrolledtext
import random
import time
import keyboard
import pyautogui
import sys
import platform

class HumanTyper:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Human Code Typer")
        self.window.geometry("800x600")
        
        # Detect operating system
        self.os_type = platform.system().lower()
        
        # Configure pyautogui
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.02
        
        # Create and configure the input text area
        self.input_label = tk.Label(self.window, text="Paste your code here:")
        self.input_label.pack(pady=5)
        
        self.input_text = scrolledtext.ScrolledText(self.window, height=15)
        self.input_text.pack(pady=10, padx=10)
        
        # Create status label
        self.status_label = tk.Label(self.window, 
            text="Press F2 to start typing (make sure to focus your target editor)")
        self.status_label.pack(pady=5)
        
        # Create debug label
        self.debug_label = tk.Label(self.window, text=f"Running on {platform.system()}")
        self.debug_label.pack(pady=5)
        
        # Add clear button
        self.clear_button = tk.Button(self.window, text="Clear Input", command=self.clear_input)
        self.clear_button.pack(pady=5)
        
        # Add start button
        self.start_button = tk.Button(self.window, text="Start Typing (F2)", command=self.start_typing)
        self.start_button.pack(pady=5)
        
        # Bind F2 key
        self.window.bind('<F2>', self.on_f2_press)
        keyboard.on_press_key('f2', self.on_f2_press)
        
        # Initialize typing state
        self.is_typing = False

    def clear_input(self):
        self.input_text.delete("1.0", tk.END)
        self.status_label.config(text="Input cleared. Press F2 to start typing when ready.")
    
    def start_typing(self):
        if not self.is_typing:
            text = self.input_text.get("1.0", tk.END)
            self.simulate_human_typing(text)

    def type_special_char(self, char):
        """Type special characters based on OS"""
        if self.os_type == 'windows':
            # Windows-specific key combinations
            if char == '<':
                keyboard.press('shift')
                keyboard.press_and_release(',')
                keyboard.release('shift')
            elif char == '>':
                keyboard.press('shift')
                keyboard.press_and_release('.')
                keyboard.release('shift')
            elif char == '{':
                keyboard.press_and_release('shift+[')
            elif char == '}':
                keyboard.press_and_release('shift+]')
            elif char == ':':
                keyboard.press_and_release('shift+;')
            elif char == '"':
                keyboard.press_and_release('shift+\'')
            elif char == '*':
                keyboard.press_and_release('shift+8')
            else:
                return False
        else:
            # Linux/Mac key combinations
            if char == '<':
                keyboard.press('shift')
                keyboard.press_and_release(',')
                keyboard.release('shift')
            elif char == '>':
                keyboard.press('shift')
                keyboard.press_and_release('.')
                keyboard.release('shift')
            elif char == '{':
                keyboard.press('shift')
                keyboard.press_and_release('[')
                keyboard.release('shift')
            elif char == '}':
                keyboard.press('shift')
                keyboard.press_and_release(']')
                keyboard.release('shift')
            elif char == ':':
                keyboard.press('shift')
                keyboard.press_and_release(';')
                keyboard.release('shift')
            elif char == '"':
                keyboard.press('shift')
                keyboard.press_and_release("'")
                keyboard.release('shift')
            elif char == '*':
                keyboard.press('shift')
                keyboard.press_and_release('8')
                keyboard.release('shift')
            else:
                return False
        return True

    def type_char(self, char):
        """Type a single character with proper case handling"""
        try:
            # Try special character first
            if self.type_special_char(char):
                pass
            # Handle uppercase letters
            elif char.isupper():
                keyboard.press('shift')
                keyboard.write(char.lower())
                keyboard.release('shift')
            # Handle normal characters
            else:
                keyboard.write(char)
            time.sleep(0.02)
        except Exception as e:
            print(f"Error typing character '{char}': {str(e)}")
            raise

    def type_text(self, text):
        """Type text exactly as it appears"""
        for char in text:
            if not self.is_typing:
                break
            self.type_char(char)
            # Small random delay between characters
            time.sleep(random.uniform(0.02, 0.08))
    
    def simulate_human_typing(self, text):
        if not text.strip():
            self.status_label.config(text="Error: No text to type!")
            return
        
        self.status_label.config(text="Starting to type in 3 seconds... Switch to your target editor!")
        self.debug_label.config(text="Preparing to type...")
        self.window.update()
        time.sleep(3)
        
        try:
            self.is_typing = True
            
            # Process text line by line
            lines = text.splitlines(True)  # Keep the newlines
            for line in lines:
                if not self.is_typing:
                    break
                
                # Reset any auto-indentation by moving to start of line
                keyboard.press_and_release('home')
                time.sleep(0.02)
                
                # Type the line exactly as it appears
                self.type_text(line)
                self.debug_label.config(text=f"Typing line: {line.strip()}")
                self.window.update()
            
            self.is_typing = False
            self.status_label.config(text="Typing completed! Press F2 to start again.")
            self.debug_label.config(text="Typing completed successfully")
            
        except Exception as e:
            self.is_typing = False
            error_msg = f"Error during typing: {str(e)}"
            self.status_label.config(text="Error occurred while typing!")
            self.debug_label.config(text=error_msg)
            print(error_msg, file=sys.stderr)
    
    def on_f2_press(self, event=None):
        if not self.is_typing:  # Only start if not already typing
            self.debug_label.config(text="F2 detected - starting to type...")
            self.window.update()
            self.start_typing()
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = HumanTyper()
    app.run() 