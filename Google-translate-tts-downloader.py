import os #외부 프로그램 실행,파일 삭제
import subprocess #음성 다운로드 역할(os로 하면 안됨)
from googletrans import Translator #구글 번역기
import time #시간 기다리는거
import pydub #파일 변환
s = input('>') #문자열 받기
a = list(s) #받은 발음은 1글자씩 쪼갬
b = 0 #파이썬은 list가 0부터 시작하기 떄문에 0부터 시작
translator = Translator() # 번역기 불러오기
locate = os.path.join(os.getcwd(), "result") #경로 불러오기
while True: #루프 시작
    if ' ' in a: #만약 공백이 있으면
        a.remove(' ') # 삭제
    else: #없으면
        if os.path.isfile(): # 이상한 파일이 있으면
            os.remove(os.path.join(os.getcwd(), "result",".mp3")) #이상한 파일 삭제
        if not os.path.isdir(locate): #result라는 폴더가 없으면
            os.mkdir(locate) # result 폴더 생성
        try: #오류 체크
            time.sleep(0.5) # 0.5초 쉬기
            lang = translator.detect(a[b]).lang #a[b]의 언어 찾기
            name = translator.translate(a[b], dest=lang).pronunciation.lower() #a[b]의 발음을 찾아 lower로 소문자로 받아 name에 저장
            if os.path.isfile(os.path.join(os.getcwd(), "result",f"{name}.wav")): #파일이 있으면
                b += 1 #b만 1 더 더하고 넘김
            else: #아니면
                subprocess.run(f'curl -o {os.path.join(os.getcwd(), "result",f"{name}.mp3")} f"https://www.google.com/speech-api/v1/synthesize?lang={lang}&speed=0.4&text={a[b]}"') #name에 저장되있는 문자열을 파일 이름으로 이용, a[b]를 lang에 저장되있는 나라로 음성을 다운
                sound = pydub.AudioSegment.from_mp3(os.path.join(os.getcwd(), "result",f"{name}.mp3")) #mp3를 가져옴
                sound.export(os.path.join(os.getcwd(), "result", f"{name}.wav"), format="wav") #mp3 -> wav 변환 작업
                os.remove(os.path.join(os.getcwd(), "result",f"{name}.mp3")) #작업이 다되면 mp3 삭제
                b += 1 #b를 1더함
        except AttributeError: #name에 저장하는 과정중 과도한 트래픽 사용하면 잠시 정지되어 오류작업
            time.sleep(2.5)# 2.5초 쉬고 다시 시도
        except IndexError: #다 끝나고 IndexError가 나면
            print("End.") #End. 를 출력하고
            os.system("PAUSE") #콘솔을 멈추고
            break #루프를 끝냄