
from whisper_mic import WhisperMic

# Initialize WhisperMic with your preferred settings
whisper = WhisperMic(model="base", english=True)

print("\nWelcome to Whisper CLI!")
print("Press Enter to speak. Speak clearly after the prompt. Press Ctrl+C to exit.\n")

try:
    while True:
        input("🎤 Press Enter to record... ")
        text = whisper.listen(timeout=5, phrase_time_limit=6)
        if text:
            print("📝 You said:", text)
        else:
            print("⚠️ No input detected. Try again.")
except KeyboardInterrupt:
    print("\n👋 Exiting. Bye!")
