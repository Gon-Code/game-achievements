# Game Achievements
Game Achievements is a web page that allows players to integrate all their achievements from different gaming platforms into a single profile. With this application, users can view and manage their achievements in one place.

## Features
- User authentication with login.
- Integration of achievements from various gaming platforms.
- User profile with achievement display.

## Installation and Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/Gon-Code/game-achievements.git
   cd game-achievements
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Start the server:
   ```sh
   python manage.py runserver
   ```

## Contributing
Contributions are welcome. If you want to collaborate, follow these steps:
1. Fork the repository.
2. Create a branch with your feature or improvement (`git checkout -b feature-new-functionality`).
3. Make changes and commit 
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

