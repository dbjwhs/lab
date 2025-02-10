# Claude Translation CLI

A command-line tool for translating English to Chinese using the Claude API. This tool provides quick and easy access to Claude's translation capabilities directly from your terminal.

## Features

- Translate English text to Chinese (Simplified)
- Support for both single-line and multi-line input
- Automatic clipboard integration for easy copying of translations
- Secure API key storage
- Pipe support for integration with other commands

## Prerequisites

- Python 3.x
- pip3
- An Anthropic API key (get one at https://console.anthropic.com)

## Installation

1. Install required Python packages:
```bash
pip3 install requests pyperclip
```

2. Create a directory for the tool:
```bash
mkdir ~/translate-tool
cd ~/translate-tool
```

3. Download the script files:
   - Save `translate.py` and `translate` shell script to the created directory
   - Make both files executable:
```bash
chmod +x translate.py translate

# On macOS, you'll need to remove the quarantine attribute:
xattr -d com.apple.quarantine translate
xattr -d com.apple.quarantine translate.py
```

4. Create a symbolic link to make the command globally available:
```bash
sudo mkdir -p /usr/local/bin
sudo ln -s ~/translate-tool/translate /usr/local/bin/translate
```

## Configuration

On first run, the tool will prompt you for your Anthropic API key. The key will be stored securely in `~/.translate-cli-config.json` with appropriate file permissions.

## Usage

Basic translation:
```bash
translate "Hello, how are you?"

Translation:
-----------
你好，你好吗？

Translation copied to clipboard!
```

Multi-line translation (press Ctrl+D when done):
```bash
translate
Enter text to translate:
Hello,
How are you today?
I hope you're doing well.

Translation:
-----------
你好，
今天你好吗？
希望你一切都好。

Translation copied to clipboard!
```

Pipe text from another command:
```bash
echo "Hello" | translate

Translation:
-----------
你好

Translation copied to clipboard!
```

## Arguments

- `text`: The text to translate (optional)
- `-h, --help`: Show help message

## File Locations

- Main script: `~/translate-tool/translate.py`
- Shell wrapper: `~/translate-tool/translate`
- Config file: `~/.translate-cli-config.json`
- Symbolic link: `/usr/local/bin/translate`

## Uninstallation

To remove the tool:

```bash
# Remove symbolic link
sudo rm /usr/local/bin/translate

# Remove tool directory
rm -rf ~/translate-tool

# Remove config file
rm ~/.translate-cli-config.json
```

## Security

- The API key is stored in your home directory with read-only permissions for the current user
- The config file permissions are set to 600 (user read/write only)
- API calls are made over HTTPS

## Troubleshooting

1. If you get "operation not permitted" on macOS and don't feel like wasting
an hour of your life like I did when then keep reading :-)
   - This is due to macOS security features (Gatekeeper)
   - Remove the quarantine attribute:
   ```bash
   xattr -d com.apple.quarantine translate
   xattr -d com.apple.quarantine translate.py
   ```
2. If you get "command not found: python":
   - Make sure you have Python 3 installed: `python3 --version`
   - Install Python 3 if needed: `brew install python3`

2. If clipboard copying doesn't work:
   - Ensure pyperclip is installed: `pip3 install pyperclip`
   - On some systems, you may need to install xclip: `brew install xclip`

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License - feel free to modify and reuse this tool as needed.