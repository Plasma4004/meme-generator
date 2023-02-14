from typing import List
from pathlib import Path
from pil_utils import BuildImage

from meme_generator import add_meme
from meme_generator.utils import make_jpg_or_gif
from meme_generator.exception import TextOverLength


img_dir = Path(__file__).parent / "images"


def learn(images: List[BuildImage], texts: List[str], args):
    text = texts[0] if texts else "偷学群友数理基础"
    frame = BuildImage.open(img_dir / "0.png")
    try:
        frame.draw_text(
            (100, 1360, frame.width - 100, 1730),
            text,
            max_fontsize=350,
            min_fontsize=200,
            weight="bold",
        )
    except ValueError:
        raise TextOverLength(text)

    def make(img: BuildImage) -> BuildImage:
        return frame.copy().paste(
            img.resize((1751, 1347), keep_ratio=True), (1440, 0), alpha=True
        )

    return make_jpg_or_gif(images[0], make)


add_meme(
    "learn",
    ["偷学"],
    learn,
    min_images=1,
    max_images=1,
    min_texts=0,
    max_texts=1,
    default_texts=["偷学群友数理基础"],
)
