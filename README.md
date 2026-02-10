# Password Generator

This is a simple password generator application built with `customtkinter`. It allows users to generate strong, customizable passwords with options for lowercase, uppercase, numbers, and symbols.

## Features

*   Generate passwords of varying lengths (8-32 characters).
*   Include/exclude lowercase letters.
*   Include/exclude uppercase letters.
*   Include/exclude numbers.
*   Include/exclude symbols.
*   Copy generated password to clipboard.
*   Modern and clean GUI with a dark theme.

## How to Run

1.  **Prerequisites:**
    *   Python 3.x installed on your system.
    *   `customtkinter` and `pyperclip` libraries. You can install them using pip:
        ```bash
        pip install customtkinter pyperclip
        ```

2.  **Run the application:**
    ```bash
    python app.py
    ```

## How to Build an Executable

You can create a standalone executable (`.exe` for Windows) using `PyInstaller`.

1.  **Install PyInstaller:**
    ```bash
    pip install pyinstaller
    ```

2.  **Build the executable:**
    Navigate to the project directory in your terminal and run the following command:
    ```bash
    pyinstaller --noconsole --onefile app.py
    ```
    This will create a `dist` folder containing the `app.exe` (or `app` on other OS) executable.

## License

This project is open-source. Feel free to modify and distribute.
