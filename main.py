import os
import logging

from TelegramInterface import TelegramInterface

def main():

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    token = os.environ['TELEGRAM_TOKEN']
    admin_id = os.environ['TELEGRAM_ADMIN_ID']
    Bot = TelegramInterface(token,admin_id)

if __name__ == "__main__":
    main()
