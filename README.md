# Zootopia API Project

This project generates a dynamic animal website by fetching data from the API Ninja Animals API.  
Users can enter the name of an animal, and the program will generate an HTML page with information about that animal.

---

## Features

- Fetch animal data dynamically from the API Ninja Animals API.
- Display information such as name, diet, type, and locations.
- Friendly error message if the animal does not exist.
- Modular architecture: Data Fetcher and Website Generator are separated.
- Secure storage of API key using a `.env` file.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Zootopia-API.git
2. Navigate to the project folder:
   ```bash 
   cd Zootopia-API
3. Install dependencies:
   ```bash  
   pip install -r requirements.txt
4. Create a .env file in the project root and add your API key:
   ```bash  
   API_KEY=your_api_key_here
   
---

## Usage

1. Run the program:
    ```bash
   python animals_web_generator.py
2. Enter the name of an animal when prompted.
3. The program will generate animals.html containing all relevant information about the animal.
4. If the animal does not exist, a friendly error message will be displayed on the website.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Make your changes.
3. Create a pull request.