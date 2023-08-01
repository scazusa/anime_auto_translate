import whisper
from whisper.tokenizer import *
model_path = r"E:\ai\models\whisper\medium.pt"
audio_path = r"E:\ai\whisper\whisper\sym1018\说书人.mp3"

model = whisper.load_model(model_path)
audio = whisper.load_audio(audio_path)
'''
# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio(audio_path)
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)
'''

result = model.transcribe(audio,language="zh")
for i in range(len(result)):
    print(result["start"][i],result["end"][i],result["text"][i])
    print("\n")