import subprocess

# -s125 -p75
def say(something, language=' ', voice=' '):
    subprocess.call(['espeak', language + voice + ' ' + something])

