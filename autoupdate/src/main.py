import os
import time
import uuid
import zipfile
import requests
import shutil
from clint.textui import progress
import threading
from gui import *

gui = guiClass()

uplfoadThread = threading.Thread(target=gui.gui)
uplfoadThread.setDaemon(False)
uplfoadThread.start()
time.sleep(2)


def doneError():
    gui.doneF()
    sys.exit()


def doneEZ():
    gui.done()
    sys.exit()


if len(sys.argv) != 3:

    doneError()


oldmodfile = sys.argv[1]
url = sys.argv[2]

tempfile = f"bh-{str(uuid.uuid4())}"


r = requests.get(url, stream=True)
with open(tempfile, "wb") as f:
    header = r.headers.get("content-length")

    try:
        total_length = int(header)
    except:
        total_length = 2_600_000

    for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
        if chunk:
            f.write(chunk)
            f.flush()

if url.endswith(".zip"):
    with zipfile.ZipFile(tempfile, 'r') as zp:
        files = zipfile.ZipFile.infolist(zp)
        if len(files) > 0:
            unzippedfile = "bh-" + str(uuid.uuid4())

            with open(unzippedfile, 'wb') as f:
                f.write(zp.read(files[0].filename))
        else:
            doneError()

    os.remove(tempfile)
    tempfile = unzippedfile


firstLine = False
while True:
    if not gui.isOpen():
        sys.exit()
    try:
        os.remove(oldmodfile)

        break
    except Exception as e:
        if not os.path.exists(oldmodfile):
            break

        else:
            gui.minecraft()
            firstLine = True

        time.sleep(1)

try:
    shutil.move(tempfile, os.path.dirname(oldmodfile) + rf"\{os.path.basename(url)}")
except Exception as e:
    doneError()


doneEZ()
