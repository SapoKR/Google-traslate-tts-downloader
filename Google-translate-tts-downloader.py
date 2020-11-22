import os
import subprocess
from googletrans import Translator
import time
import pydub
s = input('>')
a = list(s)
b = 0
while True:
    if ' ' in a:
        a.remove(' ')
    else:
        if os.path.isfile('result/.mp3'):
            os.remove('result/.mp3')
        if not os.path.isdir('result'):
            os.mkdir('result')
        try:
            time.sleep(0.5)
            translator = Translator()
            name = translator.translate(a[b], dest="ja").pronunciation.lower()
            if os.path.isfile(f'result/{name}.wav'):
                b += 1
            else:
                subprocess.run(f'curl -o result/{name}.mp3 "https://www.google.com/speech-api/v1/synthesize?lang=ja-jp&speed=0.4&text={a[b]}"')
                sound = pydub.AudioSegment.from_mp3(f"result/{name}.mp3")
                sound.export(f"result/{name}.wav", format="wav")
                os.remove(f'result/{name}.mp3')
                b += 1
        except AttributeError:
            time.sleep(2.5)
        except IndexError:
            print("End.")
            break