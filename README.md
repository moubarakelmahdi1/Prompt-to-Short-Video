# Video Generator Application

## Description

This Video Generator Application is a Flask-based web service that allows users to generate videos from a text script using OpenAI's GPT and DALL-E APIs for content creation, and Eleven Labs for voice narration. This tool is perfect for creating educational content, storytelling, and much more, offering an innovative way to produce videos with synthetic media.

## Installation

To set up the project on your local machine, follow these steps:

1. Clone the repository to your local machine:

   ```sh
   git clone https://github.com/moubarakelmahdi1/Prompt-to-Short-Video.git
   ```

2. Navigate to the cloned repository directory:

   ```sh
   cd video-generator
   ```

3. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Set up the environment variables by creating a `.env` file based on the `.env.example` provided.

## Usage

To run the application, execute:

```sh
flask run
```

Navigate to `http://127.0.0.1:5000/` in your web browser to access the application.

To generate a video, fill in the title and script in JSON format in the provided form and submit. The application will process the request and provide a link to download the generated video.

Format of the JSON script :

```
  [
    {
      "description": "Text to read 1",
      "prompt": "Image to show with Text 1"
    },
     {
      "description": "Text to read 2",
      "prompt": "Image to show with Text 2"
    },
    {
      "description": "Text to read 3",
      "prompt": "Image to show with Text 3"
    },
   ...
  ]
```

You can generate such scripts using automated GPT applications.

You can use this prompt :

```
{
   "description":"Creation of scripts for TikTok videos targeted at a young and dynamic audience. The scripts should use contemporary language and cultural references.",
   "objectives":[
      {
         "Audience Understanding":"Adapt your messages to resonate with a young and dynamic audience on TikTok, using contemporary cultural references."
      },
      {
         "Value Content":"Each video should offer enriching or entertaining content, providing added value to the audience."
      },
      {
         "Engaging Hook":"Start each video with a captivating hook, consisting of a single sentence, lasting a maximum of 3 seconds, to instantly capture attention."
      },
      {
         "Engaging Main Content":"Develop your subject matter concisely and interactively, with anecdotes, demonstrations, or dialogues, to maintain engagement."
      },
      {
         "Conclusive Call to Action":"Conclude with a clear call to action, encouraging interactions and follow-up for more content."
      },
      {
         "Script Length":"The script should cover a video duration of 40 seconds to 1 minute 30 seconds, with a brisk pace to maintain engagement."
      }
   ],
   "formatting_guidelines":"Scripts should be concise, with a maximum duration of 1 minute 30 seconds, addressing the audience directly with direct and engaging language.",
   "response_format":{
      "description":"Each response should be formatted in JSON, including a list of objects with 'paragraph' and 'prompt'.",
      "paragraph":"Text for quick and captivating script, designed to maintain a brisk pace and avoid lingering on a single image for too long.",
      "prompt":"Detailed description for a static vertical image, complementing a specific section of the script. The image should enhance the content, be relevant, and reinforce the script's message without using videos, animations, text, or graphics. [ATTENTION] It must be clearly stated that the image is vertical in every prompt, and great care must be taken to ensure that it does NOT describe ANY textual content."
   },
   "final_description":"After the JSON response, include a concise and appealing description for the TikTok video, effectively summarizing the content and encouraging engagement."
}
```

## Configuration

The `.env` file must contain the following variables:

- `OPENAI_API_KEY`: Your OpenAI API key for GPT and DALL-E usage.
- `ELEVENLABS_API_KEY`: Your Eleven Labs API key for voice narration.

## Dependencies

- Flask
- OpenAI's GPT and DALL-E APIs
- Eleven Labs API
- MoviePy

Refer to `requirements.txt` for a complete list of dependencies.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any queries or further assistance, please contact the repository owner.
