# 📒 Smart Contact Book - GUI Edition

Welcome to the **Smart Contact Book**, a fully functional, interactive Desktop Application built using Python! 

This project upgrades the traditional terminal-based contact manager into a clean, user-friendly Graphical User Interface (GUI). It safely stores all your contacts in personalized JSON files, acting as your personal Digital Diary.

## ✨ Key Features
* **Personalized Diaries:** Enter your name on the home screen, and the app will automatically create a specific `[YourName]_contacts.json` file just for you. Multiple users can use the app without mixing their contacts!
* **Interactive UI:** Built using `tkinter` with dedicated pop-up (`Toplevel`) windows for different tasks.
* **Add Contacts:** Easily save a person's name and phone number.
* **Search Contacts:** Instant retrieval of phone numbers using the person's name.
* **Smart Storage:** Uses JSON for lightweight, fast, and permanent local data storage.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Frontend/GUI:** `tkinter` (Python's standard GUI library)
* **Backend/Database:** `json` (for data storage) and `os` (for file handling)

## 📂 Project Structure
This project follows a modular programming approach, separating the backend logic from the frontend interface:

1. `Digital_Diary_by_json.py`: The **Backend**. Contains the `ContactBook` class which handles all the core logic—creating JSON files, reading data, appending new contacts, and searching for existing ones.
2. `GUI_based_Diary.py`: The **Frontend**. Contains the `tkinter` code that creates the visual elements (Labels, Buttons, Entry boxes) and connects user inputs to the backend class.

## 🚀 How to Run the App
1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Keep both `Digital_Diary_by_json.py` and `GUI_based_Diary.py` in the same folder.
4. Run the frontend file using the terminal or your IDE:
   ```bash
   python GUI_based_Diary.py
