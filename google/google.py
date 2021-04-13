import speech_recognition as sr
import os


def wav2Text(filePath):
    r = sr.Recognizer()
    with sr.AudioFile(filePath) as source:
        audio = r.record(source)
    return r.recognize_bing(audio, "", language='zh-CN')


# testSet = "../testSet"
# for filename in os.listdir(testSet):
#     if filename.endswith(".wav"):
#         text = wav2Text(os.path.join(testSet, filename))
#         print("实际内容：%s" % filename)
#         print("预测结果：%s" % text)
#         print()
