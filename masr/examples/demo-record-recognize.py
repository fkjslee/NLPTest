import _init_path
from models.conv import GatedConv
import os
from pydub import AudioSegment

model = GatedConv.load("pretrained/gated-conv.pth")

testSetDir = "../../testSet"


def convertToWav(dirPath):
    for filename in os.listdir(dirPath):
        if filename.endswith(".m4a"):
            filepath = dirPath + '/' + filename
            (path, file_extension) = os.path.splitext(filepath)
            file_extension_final = file_extension.replace('.', '')
            try:
                track = AudioSegment.from_file(filepath, file_extension_final)
                wav_filename = filename.replace(file_extension_final, 'wav')
                if os.path.isfile(os.path.join(dirPath, wav_filename)):
                    continue
                wav_path = dirPath + '/' + wav_filename
                print('CONVERTING: ' + str(filepath))
                track.export(wav_path, format='wav')
            except:
                print("ERROR CONVERTING " + str(filepath))


def testWavToText(dirPath):
    for filename in os.listdir(dirPath):
        if filename.endswith(".wav"):
            text = model.predict(os.path.join(dirPath, filename))
            print("实际内容：%s" % text)
            print("预测结果：%s" % filename)
            print()


# convertToWav(testSetDir)
testWavToText(testSetDir)



# for filename in os.listdir(testSetDir):
#     text = model.predict(os.path.join(testSetDir, filename))
#     print("实际内容：%s" % text)
#     print("预测结果：%s" % filename)
