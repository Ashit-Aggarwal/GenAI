from diffusers import StableDiffusionPipeline
import torch, os
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    use_auth_token=HF_TOKEN
).to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt, output_path="static/images/generated.png"):
    image = pipe(prompt).images[0]
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path)
    return output_path
