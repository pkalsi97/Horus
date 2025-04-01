# Horus - Personal AI Assistant

Horus is a command-line based personal AI assistant powered by Google's Gemini models. It provides a simple interface to interact with the Gemini language model, allowing you to have conversations, and manage your setup.

## Features

* **Interactive Chat:** Engage in conversations with the Gemini language model.
* **Configuration Management:** Easily set up and manage your API key and user name.
* **Command-Line Interface:** Simple and intuitive command-line interface.
* **Clear Command:** Clear the screen and return to the main menu.
* **Exit Command:** Safely exit the application.
* **API Key Validation:** Validates the provided Google Gemini API key.

## Prerequisites

* Python 3.6+
* Google Gemini API key
* Poetry for dependency management

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/pkalsi97/Horus.git
    cd Horus
    ```

2.  **Install Poetry (if you don't have it):**

    ```bash
    curl -sSL [https://install.python-poetry.org](https://install.python-poetry.org) | python3 -
    ```

3.  **Install dependencies using Poetry:**

    ```bash
    poetry install
    ```

4.  **Set up environment variables:**

    * Create a `.env` file in the root directory of the project.
    * Add the following line to the `.env` file, replacing `<your_data_file_path>` with the desired path for storing configuration data (e.g., `config.json`):

        ```
        DATA_FILE=<your_data_file_path>
        ```
5.  **Config.json:**
       ```
       {
           "name":"Your Name",
           "api_key":"API KEY"
       }
       ```


## Usage

1.  **Activate the Poetry shell:**

    ```bash
    poetry shell
    ```

2.  **Run the application:**

    ```bash
    python main.py
    ```

3.  **Main Menu Commands:**

    * `horus setup`: Configure your name and API key.
    * `horus chat`: Start a chat session with the Gemini model.
    * `horus clear`: Clear the screen.
    * `horus exit`: Exit the application.

4.  **Chat Session:**

    * In the chat session, type your messages and press Enter.
    * To end the chat, type `$END$` and press Enter.

## Configuration

* **`horus setup`:**
    * This command allows you to set your name and Google Gemini API key.
    * The application stores this information in the `DATA_FILE` specified in the `.env` file.
    * It also allows to update the data if it already exists.

## Code Structure

* **`horus/main.py`:** The main entry point of the application.
* **`horus/menu.py`:** Contains functions for displaying menus and validating commands.
* **`horus/chat_util.py`:** Contains utility functions for chat functionality, including API key validation.
* **`horus/colors.py`:** Provides ANSI escape codes for colored terminal output.

## Dependencies

* Dependencies are managed using `poetry`. See `pyproject.toml` for the list of dependencies.

## Notes

* Ensure your Google Gemini API key is valid and has the necessary permissions.
* The application stores your API key locally. Handle this information securely.
* The API Key validation makes a request to the google api.
* The application is designed for command-line use.

## Author

[PRANJUL KALSI/pkalsi97]
