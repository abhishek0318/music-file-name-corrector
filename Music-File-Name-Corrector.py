import os
import re

def corrected_file_name(FileName):
    """
    This function corrects filename of mp3 file.
    """
    # remove '.mp3', '%', Kbps
    FileName = FileName.replace(".mp3", "")
    FileName = FileName.replace("%", "")
    FileName = FileName.replace("Kbps", "")

    # replace %20, -, _ with space
    FileName = FileName.replace("%20", " ")
    FileName = FileName.replace("-", " ")
    FileName = FileName.replace("_", " ")

    # remove numbers
    FileName = ''.join(i for i in FileName if not i.isdigit())

    # remove URLs
    FileName = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', FileName)

    # remove brackets
    Temp = []
    BracketOpen = False
    for i in range(len(FileName)):
        if FileName[i] == '(' or FileName[i] == '[':
            BracketOpen = True
        elif FileName[i] == ')' or FileName[i] == ']':
            BracketOpen = False
        elif BracketOpen is False:
            Temp.append(FileName[i])
    FileName = ''.join(Temp)

    # remove extra whitespace
    FileName = " ".join(FileName.split())

    # capitalise each word
    FileName = FileName.title()

    # add ".mp3"
    FileName = FileName.strip()
    FileName = FileName + '.mp3'
    return FileName

for FileName in os.listdir():
    if FileName.endswith(".mp3"):
        os.rename(FileName, corrected_file_name(FileName))
