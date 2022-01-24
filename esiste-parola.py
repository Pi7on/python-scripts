# Checks if an italian word exists or not by looking it up on the Treccani vocabulary.
# Returns 1 if the words exists, 0 if it doesn't.

import requests as r
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('parola', type=str)
args = parser.parse_args()

url = "https://www.treccani.it/vocabolario/ricerca/"+args.parola+"/"
response = r.get(url)
print(("SI" if response.status_code == 200 else "NO"))
sys.exit((1 if response.status_code == 200 else 0))
