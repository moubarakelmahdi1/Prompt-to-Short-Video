from elevenlabs import set_api_key, generate
from openai import OpenAI
from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_videoclips
import requests
from tempfile import NamedTemporaryFile
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration des API clients
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
set_api_key(os.getenv("ELEVENLABS_API_KEY"))


# Fonctions pour générer la voix et l'image
def generate_voice(text):
    audio = generate(text=text, voice='Adam', model="eleven_multilingual_v2")
    return audio


def generate_image(prompt):
    try:
        response = client.images.generate(
            prompt=prompt, model="dall-e-3", size="1024x1792")
        image_url = response.data[0].url
        return image_url
    except Exception as e:
        print("Erreur lors de la génération de l'image:", e)
        return None


# Fonction principale


def generate_video(title, script):
    logger.info("Début de la génération de la vidéo")
    clips = []

    for item in script:
        logger.info(
            "Génération de la voix et de l'image pour un élément du script", item["prompt"])
        audio_binary = generate_voice(item["description"])
        image_url = generate_image(item["prompt"])

        with NamedTemporaryFile(delete=False, suffix='.mp3') as audio_file:
            audio_file.write(audio_binary)
            audio_path = audio_file.name

        img_response = requests.get(image_url)
        with NamedTemporaryFile(delete=False, suffix='.png') as img_file:
            img_file.write(img_response.content)
            img_path = img_file.name

        video_clip = ImageSequenceClip([img_path], fps=1)
        audio_clip = AudioFileClip(audio_path)
        video_clip = video_clip.set_audio(
            audio_clip).set_duration(audio_clip.duration)
        clips.append(video_clip)

    logger.info("Concaténation des clips")
    final_clip = concatenate_videoclips(clips, method="compose")

    output_dir = 'static/videos'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, f"{title}.mp4")
    final_clip.write_videofile(output_path, codec="libx264")
    logger.info("Vidéo générée et enregistrée : %s", output_path)

    return output_path
