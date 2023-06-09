import os
import gradio as gr
import whisper
import certifi
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
ssl._create_default_https_context(cafile=certifi.where())


def transcribe_audio(audio_file):
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    return result["text"]


def main():
    audio_input = gr.inputs.Audio(source="upload", type="filepath")
    output_text = gr.outputs.Textbox()

    iface = gr.Interface(fn=transcribe_audio, inputs=audio_input,
                         outputs=output_text, title="Eduardo's Audio Transcription App",
                         description="Upload an audio file and hit the 'Submit' button")

    iface.launch(server_port=int(os.getenv('PORT', 7860)))  # get the port from environment variable PORT


if __name__ == '__main__':
    main()
