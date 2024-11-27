# <img src="https://github.com/user-attachments/assets/e80e38cb-65ef-4aaf-b3a2-c6722c03cba2" alt="Mochi" width="35" height="35" style="border-radius: 50%;" /> Mochi

[![GitHub issues](https://img.shields.io/github/issues/upayanmazumder/Mochi)](https://github.com/upayanmazumder/Mochi/issues)
[![GitHub forks](https://img.shields.io/github/forks/upayanmazumder/Mochi)](https://github.com/upayanmazumder/Mochi/network)
[![GitHub stars](https://img.shields.io/github/stars/upayanmazumder/Mochi)](https://github.com/upayanmazumder/Mochi/stargazers)
[![GitHub license](https://img.shields.io/github/license/upayanmazumder/Mochi)](https://github.com/upayanmazumder/Mochi/blob/main/LICENSE)
[![Docker Image](https://img.shields.io/badge/Docker-GHCR%20Image-blue)](https://ghcr.io/upayanmazumder/mochi)

Mochi is a lightweight and containerized Discord bot designed for streamlined deployment and effortless management. With its simple and modular design, Mochi is the perfect choice for adding fun and functionality to your Discord server!

---

## Features

- **Lightweight Design**: Minimal dependencies for efficient performance.
- **Dockerized Deployment**: Quickly build and run with Docker.
- **Customizable**: Easily extend or modify the bot's functionality.

---

## Getting Started

### Prerequisites

- **Python 3.10+**
- **Docker (optional)** for containerized deployment
- **Discord Bot Token** (add it to a `.env` file)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/upayanmazumder/Mochi.git
   cd Mochi
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file with the following:

   ```
   BOT_TOKEN=your-discord-bot-token
   ```

4. **Run the Bot**:

   ```bash
   python bot.py
   ```

---

## Docker Deployment

1. **Build the Docker Image**:

   ```bash
   docker build -t ghcr.io/upayanmazumder/mochi:latest .
   ```

2. **Run the Docker Container**:

   ```bash
   docker run --env-file .env ghcr.io/upayanmazumder/mochi:latest
   ```

3. **Pull the Image from GHCR**:

   ```bash
   docker pull ghcr.io/upayanmazumder/mochi:latest
   ```

---

## Contributing

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add some feature"
   ```

4. Push to the branch:

   ```bash
   git push origin feature-name
   ```

5. Open a pull request.

---

## Repository Stats

![Code size](https://img.shields.io/github/languages/code-size/upayanmazumder/Mochi)
![Repo size](https://img.shields.io/github/repo-size/upayanmazumder/Mochi)
![Commit activity](https://img.shields.io/github/commit-activity/m/upayanmazumder/Mochi)
![Last commit](https://img.shields.io/github/last-commit/upayanmazumder/Mochi)

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

If you have any questions or suggestions, feel free to reach out:

- **GitHub**: [upayanmazumder](https://github.com/upayanmazumder)
- **Email**: [mochi.bot@upayan.dev](mailto:mochi.bot@upayan.dev)
