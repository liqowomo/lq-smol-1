# This is for image generation
# Imagen in private beta so cant use this

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

GA_KEY1 = os.environ.get("GAKE")
client = genai.Client(GA_KEY1)
prompt_1 = "Ultra realistic extremely detailed image of a band of cyborg foods in a synthwave cyberpunk ambience"


def img1():
    response = client.models.generate_image(
        model="imagen-3.0-generate-002",
        prompt=prompt_1,
        config=types.GenerateImageConfig(
            negative_prompt="people",
            number_of_images=1,
            include_rai_reason=True,
            output_mime_type="image/jpeg",
        ),
    )

    response.generated_images[0].image.show()
