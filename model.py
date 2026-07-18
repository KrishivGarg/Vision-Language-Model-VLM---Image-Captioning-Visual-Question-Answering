from transformers import Blip2Processor, Blip2ForConditionalGeneration
import torch
from PIL import Image

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
DTYPE  = torch.float16 if DEVICE == "cuda" else torch.float32

print(f"[VLM] Loading on {DEVICE} ...")

processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained(
    "Salesforce/blip2-opt-2.7b",
    torch_dtype=DTYPE
).to(DEVICE)
model.eval()

def caption_image(image: Image.Image) -> str:
    inputs = processor(images=image, return_tensors="pt").to(DEVICE, DTYPE)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=80)
    return processor.decode(out[0], skip_special_tokens=True).strip()

def answer_question(image: Image.Image, question: str) -> str:
    prompt = f"Question: {question} Answer:"
    inputs = processor(
        images=image, text=prompt, return_tensors="pt"
    ).to(DEVICE, DTYPE)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=60)
    raw = processor.decode(out[0], skip_special_tokens=True)
    # Strip the echoed prompt from the output
    answer = raw.replace(prompt, "").strip()
    return answer