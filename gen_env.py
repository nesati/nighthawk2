from django.core.management.utils import get_random_secret_key
import argparse

parser = argparse.ArgumentParser(description="Automatically generate and save a .env file")
parser.add_argument('--debug', action='store_true', dest='debug',
                    help="generate a development (DEBUG=True) environment")

args = parser.parse_args()

with open('.env', 'w') as file:
    file.write(f"DEBUG={args.debug}\n")
    file.write(f"SECRET_KEY={get_random_secret_key()}")
    file.write('ALLOWED_HOSTS=["localhost", "127.0.0.1", "za.gjk.cz"]')
