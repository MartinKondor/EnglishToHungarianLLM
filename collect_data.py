"""
## Source of data:
```
D. Varga, L. Németh, P. Halácsy, A. Kornai, V. Trón, V. Nagy (2005).
Parallel corpora for medium density languages
In Proceedings of the RANLP 2005, pages 590-596.
(pdf)
```
"""
import os
import subprocess
from bs4 import BeautifulSoup
from tqdm import tqdm


# Create directories
os.makedirs("hu_raw", exist_ok=True)
os.makedirs("en_raw", exist_ok=True)

# Download the list of files
hu_url = "ftp://ftp.mokk.bme.hu/Hunglish2/classic.lit/hu/"
en_url = "ftp://ftp.mokk.bme.hu/Hunglish2/classic.lit/en/"

subprocess.run(["wget", "-O", "hu.html", hu_url])
subprocess.run(["wget", "-O", "en.html", en_url])

hu_soup = BeautifulSoup(open("hu.html", "r").read(), 'html.parser')
en_soup = BeautifulSoup(open("en.html", "r").read(), 'html.parser')

# Download the files one by one
links = hu_soup.find_all("a") + en_soup.find_all("a")

for link in tqdm(links, desc="Downloading sources from links"):
    filelink = link.get("href")
    if filelink.split(".")[-1] != "raw":
        continue

    subprocess.run(["wget", "-q", filelink])

    if "/hu/" in filelink:
        filename = filelink.split("/hu/")[-1]
        subprocess.run(["mv", filename, os.path.join("hu_raw", filename)])
    elif "/en/" in filelink:
        filename = filelink.split("/en/")[-1]
        subprocess.run(["mv", filename, os.path.join("en_raw", filename)])
