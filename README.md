# EngageBot

EngageBot is an advanced AI chatbot designed to assist with various tasks, answer questions, and provide information. Built using Python's CustomTkinter module, EngageBot serves as an intelligent virtual assistant that can interact with users and perform actions based on user input.

## Features

- **Chat Functionality**: EngageBot allows users to chat and ask questions.
- **Open Websites and Applications**: Automatically opens specified websites or applications based on user commands.
- **Time and Date**: Provides the current time and date.
- **Weather Updates**: Fetches and displays weather information for a specified city.
- **News Updates**: Retrieves and displays the latest news articles based on user queries.
- **Information Queries**: Answers common questions about itself and other topics.
- **Clear Chat**: Clears the chat history when requested.

## Installation

To use EngageBot, you need to have Python installed on your system. Follow these steps to set up the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Soumya-the-programmer/EngageBot.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd EngageBot
   ```

3. **Install Required Packages**:
   Ensure you have `requests`, `huggingface_hub`, and `customtkinter` installed. You can install them using pip:
   ```bash
   pip install requests huggingface_hub customtkinter
   ```

4. **Set Up API Keys**:
   - **Weather API**: Replace `ENTER_YOUR_WEATHER_API_KEY` with your actual API key from [WeatherAPI](https://rapidapi.com).
   - **News API**: Replace `ENTER_YOUR_API_KEY_HERE` with your API key from [NewsAPI](https://newsapi.org).
   - **Hugging Face Token**: Replace `ENTER_YOUR_HUGGING_FACE_TOKEN` with your Hugging Face API token from [Hugging Face](https://huggingface.co).

## Usage

1. **Run the Application**:
   ```bash
   python engagebot.py
   ```

2. **Interact with EngageBot**:
   - **Type your message** into the search bar and press Enter or click the Send button.
   - **Ask questions** or give commands such as "open Google", "what's the time", "show me the news", etc.

3. **Available Commands**:
   - **Open Websites**: "open [website]" (e.g., "open Google").
   - **Open Applications**: "open [application]" (e.g., "open Word").
   - **Get Time**: "the time" or "the time?".
   - **Get Date**: "the date" or "the date?".
   - **Weather**: "weather in [city]" (e.g., "weather in New York").
   - **News**: "[topic] news" (e.g., "sports news").
   - **Clear Chat**: "clear chat" or "clear".
   - **Exit**: "close" or "exit".

## Code Explanation

- **Main Window Setup**: The `CTk` class is used to create the main window with a custom title, icon, and size constraints.
- **Functions**:
  - `s_bar_focus_in` and `s_bar_focus_out`: Manage the placeholder text in the search bar.
  - `user_message_send`: Handles user input, processes commands, and provides responses.
  - `ABOUT`: Displays information about EngageBot in a message box.
- **Frames and Widgets**:
  - `frame1`, `frame2`, `frame3`: Different sections of the UI for the heading, chat screen, and input area.
  - `chat_screen`: Text area for displaying chat history.
  - `search_bar`: Text area for user input.
  - `submit`: Button to send the user’s message.

## Contributing

Contributions are welcome! If you would like to contribute to the EngageBot project, please follow these steps:

1. **Fork the Repository**.
2. **Create a Feature Branch**.
3. **Commit Your Changes**.
4. **Push to the Branch**.
5. **Open a Pull Request**.

## Contact

For any questions or feedback, feel free to reach out to the project creator:

- **Name**: Soumyajeet Das
- **Email**: [soumyajeetdas5@gmail.com](mailto:soumyajeetdas5@gmail.com)
- **GitHub**: [Soumya-the-programmer](https://github.com/Soumya-the-programmer)

Thank you for using EngageBot!

      


