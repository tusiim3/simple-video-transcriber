import whisper
import tkinter as tk

# Load Whisper model
model = whisper.load_model("small")

def upload_video():
    global video_path
    video_path = tk.filedialog.askopenfilename(
        filetypes=[("Video Files", "*.mp4*.mov*.avi*.mkv")]
    )
    if video_path:
        status_label.config(text=f"Selected: {video_path}")

def transcribe_video():
    if not video_path:
        status_label.config(text="No video selected!")
        return
    
    staus_label.config(text="Transcribing... this might take a while!")
    window.update()

    result = model.transcribe(video_path)
    transcript_text.delete("1.0", tk.END)
    transcript_text.insert(tk.END, result["text"])
    status_label.config(text="Transcription done!")

# GUI Setup
window = tk.Tk()
window.title("Video Transcription")

upload_btn = tk.Button(window, text="Upload Video", command=upload_video)
upload_btn.pack(pady=10)

transcribe_btn = tk.Button(window, text="Transcribe", command=transcribe_video)
transcribe_btn.pack(pady=10)

status_label = tk.Label(window, text="No video selected")
status_label.pack(pady=5)

transcript_text = tk.Text(window, height=20, width=60)
transcript_text.pack(pady=10)

video_path = None
window.mainloop()

