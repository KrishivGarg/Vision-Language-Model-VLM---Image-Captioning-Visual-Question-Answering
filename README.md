Vision-Language Model (VLM) — Image Captioning & Visual Question Answering

A Gradio-powered web application that uses **Salesforce BLIP-2 (2.7B)** to perform **Image Captioning** and **Visual Question Answering (VQA)**. Upload an image to automatically generate a descriptive caption or ask natural-language questions about the image.

---

## Features

*  Automatic image caption generation
*  Visual Question Answering (VQA)
*  GPU acceleration with CUDA (falls back to CPU automatically)
*  Interactive Gradio web interface
*  Powered by the BLIP-2 Vision-Language Model from Hugging Face

---

## Demo

### Image Captioning

Upload an image and receive a natural language description.

**Example**

**Input:** Street scene with cars and pedestrians

**Output:**

> A busy city street with several cars and people walking on the sidewalk.

---

### Visual Question Answering

Ask questions about an uploaded image.

**Example Questions**

* What is the main object in the image?
* How many people are present?
* What colour is the car?
* What is the weather like?
* What emotion does the person show?

---

## Project Structure

```text
.
├── app.py              # Gradio interface
├── model.py            # BLIP-2 model loading & inference
├── requirements.txt
└── README.md
```

---

## How It Works

1. Upload an image.
2. Choose one of two modes:

   * **Image Captioning**
   * **Visual Question Answering**
3. For VQA mode, enter a question.
4. The image is processed by the BLIP-2 model.
5. The generated caption or answer is displayed in the interface.

---

## Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* BLIP-2 (Salesforce)
* Gradio
* Pillow

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Vision-Language-Model.git
cd Vision-Language-Model
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python app.py
```

The application will launch locally in your browser.

---

## Requirements

* Python 3.10+
* PyTorch
* Transformers
* Accelerate
* Gradio
* Pillow

---

## Model

This project uses:

**BLIP-2 (OPT-2.7B)**

* Vision-Language Transformer
* Pretrained by Salesforce
* Available via Hugging Face Transformers

---

## Future Improvements

* Support multiple Vision-Language Models
* Batch image processing
* OCR integration
* Object detection and grounding
* Streaming token generation
* Chat-style multimodal interface
* Image comparison and reasoning

---

## License

This project is intended for educational and research purposes.
Please refer to the BLIP-2 model license for usage restrictions.

---

## Acknowledgements

* Salesforce Research
* Hugging Face
* Gradio
* PyTorch
