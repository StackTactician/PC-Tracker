# Configuration for Laptop Tracker
# Copy this file to config.py and fill in your own values

TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
YOUR_TELEGRAM_CHAT_ID = "YOUR_CHAT_ID_HERE"
OPENCAGE_API_KEY = "YOUR_OPENCAGE_API_KEY_HERE"  # Optional: https://opencagedata.com/
LOCATIONIQ_API_KEY = "YOUR_LOCATIONIQ_API_KEY_HERE"  # Optional: https://locationiq.com/
ENABLE_STEALTH_MODE = True

# Stealth configuration - customize these names to blend in
STEALTH_CONFIG = {
    'process': 'WindowsSecurityHealthService.exe',
    'folder': 'Microsoft\\Windows\\Security\\HealthCheck',
    'service': 'Windows Security Health Service',
    'registry_key': 'SecurityHealthService'
}
