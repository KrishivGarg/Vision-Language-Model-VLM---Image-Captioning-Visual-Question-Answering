import gradio as gr
from PIL import Image
from model import caption_image, answer_question

def run(image, question, mode):
    if image is None:
        return "Please upload an image."
    img = Image.fromarray(image).convert("RGB")

    if mode == "Image Captioning":
        return caption_image(img)
    else:
        if not question.strip():
            return "Please enter a question for VQA mode."
        return answer_question(img, question)

with gr.Blocks(title="VLM — Captioning & VQA") as demo:
    gr.Markdown("## Vision-Language Model — Image Captioning & VQA")
    gr.Markdown("Upload an image. Choose **Caption** to auto-describe it, or **VQA** to ask a question about it.")

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(label="Input Image", type="numpy")
            mode = gr.Radio(
                ["Image Captioning", "Visual Question Answering"],
                value="Image Captioning",
                label="Mode"
            )
            question = gr.Textbox(
                label="Question (VQA mode only)",
                placeholder="e.g. What colour is the car?"
            )
            submit_btn = gr.Button("Run", variant="primary")

        with gr.Column():
            output = gr.Textbox(label="Output", lines=5)
            gr.Markdown("### Sample questions to try")
            gr.Markdown(
                "- What is the main object in the image?\n"
                "- How many people are in the image?\n"
                "- What is the weather like?\n"
                "- What emotion does the person show?"
            )

    submit_btn.click(fn=run, inputs=[image_input, question, mode], outputs=output)

if __name__ == "__main__":
    demo.launch()