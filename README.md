# Human Code Typer 🤖

A Python application that simulates human-like typing of code, making it appear as if you're typing code naturally during demonstrations, tutorials, or presentations. The app types at a realistic speed (approximately 80 WPM) with slight random variations to mimic human typing patterns.

## Features ✨

- 🎯 Simulates natural human typing with realistic speed variations
- ⌨️ Handles special characters and different keyboard layouts
- 🖥️ Cross-platform compatibility (Windows and Linux)
- 🔄 Clear and intuitive user interface
- ⚡ Quick activation with F2 hotkey
- 🎮 Full control with start/stop functionality
- 🔍 Real-time status and debug information

## Installation 🚀

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Windows Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/human-code-typer.git
   cd human-code-typer
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install keyboard pyautogui
   ```

**Note**: On Windows, the application needs to be run with administrator privileges due to keyboard library requirements.

### Linux Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/human-code-typer.git
   cd human-code-typer
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install keyboard pyautogui
   ```

**Note**: On Linux, you might need to run the following command first:
```bash
sudo apt-get install python3-tk python3-dev
```

## Usage 💻

### Quick Start Guide

1. Start the application:
   ```bash
   python human_typer.py
   ```

2. When the application opens, you'll see:
   - A large text area for pasting your code
   - A "Clear Input" button
   - A "Start Typing (F2)" button
   - Status labels showing the current state

3. Prepare your code:
   - Copy the code you want to type from anywhere
   - Paste it into the application's text area
   - The code can be any programming language or plain text

4. Start the typing simulation:
   - Method 1: Click the "Start Typing (F2)" button
   - Method 2: Press the F2 key on your keyboard
   - You'll see a "Starting to type in 3 seconds..." message

5. During the 3-second countdown:
   - Switch to your target application (e.g., VS Code, Notepad, etc.)
   - Place your cursor where you want the typing to begin
   - Make sure your target window is focused

6. Watch the magic happen:
   - The code will start typing automatically
   - You'll see real-time status updates in the application window
   - The typing speed will vary naturally to simulate human typing

### Control Features

- **Stop Typing**: Press F2 again at any time to stop the typing process
- **Clear Input**: Click the "Clear Input" button to remove all text from the input area
- **Monitor Progress**: Watch the status labels for real-time information about:
  - Current typing status
  - Line being typed
  - Any errors or issues

### Tips for Best Results

1. **Before Starting**:
   - Make sure your target editor is ready and focused
   - Ensure your cursor is at the correct starting position
   - Check that your input text is properly formatted

2. **During Typing**:
   - Don't move your mouse or keyboard
   - Let the application complete its typing
   - Watch the status labels for progress

3. **For Code Demonstrations**:
   - Start with smaller code snippets until you're comfortable
   - Test the typing in a blank document first
   - Keep the Human Typer window visible to monitor status

### Common Workflows

**For Live Coding Demos:**
1. Prepare your code snippets in advance
2. Keep the Human Typer window on a secondary monitor
3. Use F2 to seamlessly start typing during your presentation

**For Tutorial Recording:**
1. Set up your screen recording software
2. Position the Human Typer window off-screen
3. Use F2 to type code while explaining concepts

**For Pair Programming:**
1. Paste the code you want to share
2. Let your partner watch as the code types naturally
3. Use the clear button to prepare for the next snippet

## Features in Detail 🔍

### Special Character Handling
The application properly handles special characters including:
- Curly braces `{}`
- Angle brackets `<>`
- Quotes `""`
- Colons `:`
- Other special characters

### Speed and Timing
- Base typing speed: ~80 WPM
- Random delays between keystrokes for natural feel
- Configurable typing speed through code modification

### User Interface
- Clear, intuitive interface
- Status indicators
- Debug information
- One-click clear button
- F2 hotkey support

## Troubleshooting 🔧

### Windows Issues
- If you get permission errors, run the application as administrator
- Some antivirus software might block keyboard simulation - add the application to your whitelist

### Linux Issues
- If keyboard library fails to install, ensure you have Python development packages installed
- X server might require additional permissions for keyboard control

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- Thanks to the `keyboard` and `pyautogui` libraries
- Inspired by the need for natural-looking code demonstrations

## Safety Note ⚠️

This tool simulates keyboard input. Always be careful when running applications that control your keyboard, and make sure to:
- Review the code before running
- Use a virtual environment
- Run with appropriate permissions
- Be ready to force-quit if needed (Alt+F4 or equivalent) 
