# Redkit - All-in-One Penetration Testing Toolkit
![Redkit Splash](https://b.top4top.io/p_3588vuhtj1.png)

[![Platform](https://img.shields.io/badge/platform-Kali%20Linux-blue)](https://www.kali.org/)
[![Language](https://img.shields.io/badge/language-Python%203-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)


## Overview

**Redkit** is a professional, feature-rich all-in-one penetration testing and information security toolkit designed specifically for Kali Linux. It automates the installation, management, and execution of a wide range of hacking and security tools from multiple specialized categories such as Information Gathering, Exploitation, Sniffing, Web Attacks, Phishing, and more.

Redkit provides a simple, intuitive, and colorful command-line interface with multi-language support (English and Arabic), professional ASCII splash screen, dependency checking, and smart management of tools, making it ideal for both beginners and experienced penetration testers.

## Features

- **Multi-Category Support:** Organizes a large collection of security tools into categories, such as Information Gathering, Exploitation, Sniffing & Spoofing, Web Attacks, Phishing, Vulnerability Analysis, and more.
- **Automated Tool Management:** Automatically clones tools from GitHub, checks and installs dependencies (including Python packages via `requirements.txt`), and updates them as needed.
- **Interactive & Colorful CLI:** User-friendly terminal interface powered by `colorama` and `pyfiglet` libraries for enhanced usability and aesthetics.
- **Multi-Language Support:** Switch easily between English and Arabic interfaces.
- **Dependency Checks:** Verifies required system dependencies (`python3`, `git`, etc.) and assists users in installing missing components.
- **Seamless Execution:** Automatically detects how to launch tools by running standard scripts (`install.sh`, `run.sh`, etc.) or Python scripts, or opens the tool directory when automatic execution is not available.
- **Extensible:** Easily extensible to add more tools or categories by updating the configuration file.

## Installation

1. Ensure you are running **Kali Linux** or a Debian-based Linux distribution.
2. Install Python 3 and Git if not already installed:
3. Clone this repository:
4. Run the tool:


## Usage

- On launch, select your preferred language (English or Arabic).
- The tool will perform initial dependency checks and prompt to install any missing essentials.
- Navigate through organized categories via numeric menus to select desired security tools.
- Install tools automatically with one key press; Redkit will clone repositories and install required dependencies.
- Run installed tools directly from Redkit’s interface.
- Use options to return to previous menus or exit cleanly.

## Requirements

- Python 3.6+
- Git
- Bash shell
- Internet connection for downloading tools and dependencies

## Supported Categories and Example Tools

- Information Gathering (e.g., AstraNmap, EvilURL, OSIF)
- Exploitation Tools (e.g., RouterSploit, Commix)
- Sniffing and Spoofing (e.g., Hack-Gmail, KnockMail)
- Web Attack Tools (e.g., AdminHack, SqlMap)
- Cam Hacking Tools
- Remote Trojan RAT
- SQL Injection Tools
- SocialMedia Bruteforce
- SMS Spamming Tools
- Vulnerability Analysis
- DarkSearch Tools
- Phishing And IpHack
- Hash Cracking Tools
- Wordlist Generator Tools
- XSS Attack Tools

*(Full list included in the tool’s configuration and menus.)*

## Contribution

Contributions are welcome! Please fork the repository and open pull requests for bug fixes, new features, or tools.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Author

**MASA**

---

*Redkit empowers cybersecurity professionals and enthusiasts by bringing hundreds of powerful security tools under one robust, easy-to-use interface.*
