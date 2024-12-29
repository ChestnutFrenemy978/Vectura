from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt, output_path="generated_image.png"):
    """
    Генерирует изображение по текстовому описанию.
    
    :param prompt: Описание для генерации изображения.
    :param output_path: Путь для сохранения сгенерированного изображения.
    """
    # Загрузка модели Stable Diffusion
    model_id = "CompVis/stable-diffusion-v1-4"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    
    # Генерация изображения
    image = pipe(prompt).images[0]
    
    # Сохранение изображения
    image.save(output_path)
    return output_path