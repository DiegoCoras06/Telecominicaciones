from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.tools' / 'image-optimizer'))
from PIL import Image

source = ROOT / 'mapeo_red_ftth.png'
output = ROOT / 'src' / 'assets'
output.mkdir(parents=True, exist_ok=True)
with Image.open(source) as image:
    image = image.convert('RGB')
    print(f'Original: {image.width} x {image.height}, {source.stat().st_size:,} bytes')
    for width, quality, name in [(960, 85, 'mapa-ftth-960.webp'), (image.width, 90, 'mapa-ftth-full.webp')]:
        width = min(width, image.width)
        resized = image.resize((width, round(image.height * width / image.width)), Image.Resampling.LANCZOS)
        target = output / name
        resized.save(target, 'WEBP', quality=quality, method=6)
        with Image.open(target) as check:
            check.load()
            assert check.size == resized.size
        size = target.stat().st_size
        print(f'{name}: {resized.width} x {resized.height}, {size:,} bytes ({100 * (1 - size / source.stat().st_size):.1f}% menos)')
