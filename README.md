# 🔐 Local Crypter

```text
                                             ░██    
                                             ░██    
 ░███████  ░██░████ ░██    ░██ ░████████  ░████████ 
░██    ░██ ░███     ░██    ░██ ░██    ░██    ░██    
░██        ░██      ░██    ░██ ░██    ░██    ░██    
░██    ░██ ░██      ░██   ░███ ░███   ░██    ░██    
 ░███████  ░██       ░█████░██ ░██░█████      ░████ 
                           ░██ ░██                  
                     ░███████  ░██                  
                                             
  by camzzz · github.com/cameleonnbss
```

> Simple local encryption tool with multiple encryption modes,
> persistent key storage and built-in key generation.

---

## ✨ Features

- 🔐 Multiple encryption modes
  - XOR
  - Stream
  - Double encryption
- 🔑 Built-in secure key generator
- 💾 Saved session key
- ⚡ Fast local encryption
- 📦 No external dependencies
- 🖥️ Simple terminal interface
- 🧩 Lightweight project structure
- 🛠️ Works on Windows, Linux, macOS and Termux

---

## 📦 Installation

### 🪟 Windows

```batch
git clone https://github.com/cameleonnbss/Crypter.git
Crypter

python main.py
```

---

### 🐧 Linux / 🍎 macOS

```bash
git clone https://github.com/cameleonnbss/Crypter.git
cd Crypter

python3 main.py
```

---

### 📱 Termux (Android)

```bash
pkg update && pkg upgrade
pkg install git python

git clone https://github.com/cameleonnbss/Crypter.git
cd Crypter
python main.py
```

---

## ⚡ Quick Start

```bash
git clone https://github.com/cameleonnbss/Crypter.git
cd Crypter

python main.py
```

---

## 🔐 Encryption Modes

| Mode | Description |
|------|-------------|
| `XOR` | Fast basic XOR encryption |
| `Stream` | SHA256-based stream encryption |
| `Double` | XOR + Stream combined |

---

## 🔑 Key Generator

The tool includes a built-in random key generator.

Features:
- Custom key length
- Random symbols
- Auto-save generated key
- Reuse previous key instantly

---

## 📁 Files

```text
main.py            Main application
crypto.py          Encryption functions
session.json       Saved session
README.md          Documentation
requirements.txt   Optional requirements file
```

---

## 🖥️ Interface

```text
[1] Encrypt
[2] Decrypt
[3] Generate key
[4] Settings
[Q] Exit
```

---

## ⚠️ Notes

- This tool is designed for local/private usage.
- Generated keys are stored in `session.json`.
- No internet connection is required.
- No external Python modules are needed.

---

## ⚖️ Legal

For educational, local security testing and personal use only.

---

<div align="center">
made by <a href="https://github.com/cameleonnbss">camzzz</a>
</div>
