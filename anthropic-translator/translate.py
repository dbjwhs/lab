# MIT License
# Copyright (c) 2025 dbjwhs

import os
import sys
import argparse
import json
import requests
from pathlib import Path
import pyperclip  # for clipboard functionality

class TranslationCLI:
    def __init__(self):
        self.config_file = Path.home() / '.translate-cli-config.json'
        self.api_key = self.load_api_key()

    def load_api_key(self):
        """Load API key from config file or prompt user"""
        if self.config_file.exists():
            with open(self.config_file) as f:
                return json.load(f)['api_key']
        return self.setup_api_key()

    def setup_api_key(self):
        """First-time setup to save API key"""
        print("Welcome to Translate CLI!")
        print("Please enter your Anthropic API key (it will be saved securely):")
        api_key = input().strip()

        with open(self.config_file, 'w') as f:
            json.dump({'api_key': api_key}, f)

        # Set file permissions to be readable only by the user
        self.config_file.chmod(0o600)
        return api_key

    def translate(self, text):
        """Translate text using Claude API"""
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': self.api_key,
            'anthropic-version': '2023-06-01'
        }

        payload = {
            'model': 'claude-3-5-sonnet-20241022',
            'max_tokens': 1024,
            'messages': [{
                'role': 'user',
                'content': f'Translate the following English text to Chinese (Simplified). Only provide the translation, no explanations:\n\n{text}'
            }]
        }

        response = requests.post(
            'https://api.anthropic.com/v1/messages',
            headers=headers,
            json=payload
        )

        if response.status_code != 200:
            raise Exception(f"Translation failed: {response.text}")

        return response.json()['content'][0]['text']

def main():
    parser = argparse.ArgumentParser(description='Translate English to Chinese using Claude API')
    parser.add_argument('text', nargs='?', help='Text to translate. If not provided, will read from stdin')
    args = parser.parse_args()

    # Initialize translator
    translator = TranslationCLI()

    # Get input text
    if args.text:
        text = args.text
    else:
        print("Enter text to translate (Ctrl+D when done):")
        text = sys.stdin.read().strip()

    if not text:
        print("No text provided")
        return

    try:
        # Get translation
        translation = translator.translate(text)

        # Print translation
        print("\nTranslation:")
        print("-----------")
        print(translation)

        # Copy to clipboard
        pyperclip.copy(translation)
        print("\nTranslation copied to clipboard!")

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
