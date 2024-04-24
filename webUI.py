import logging
import gradio as gr

from anime_dl import anime_dl
from anime_dl.utils.logger import Logger

# disable https logs
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = Logger()
logger.reset_webui_log()

with gr.Blocks(
    title="Anime-dl", analytics_enabled=False, theme=gr.themes.Soft()
) as webui:
    gr.Markdown("Anime-dl")
    with gr.Row():
        inp = gr.Textbox(label="URL", max_lines=1)
        btn = gr.Button("Download", scale=0)
        out = gr.Label(show_label=False, scale=0)
    btn.click(fn=anime_dl.main, inputs=inp, outputs=out)
    logs = gr.Code(
        label="Log",
        language="shell",
        interactive=False,
        container=True,
        lines=15,
    )
    webui.load(logger.read_webui_log, None, logs, every=1)

if __name__ == "__main__":
    webui.launch()
