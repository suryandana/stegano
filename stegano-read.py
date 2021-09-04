# from array import array
from pathlib import Path

stegano = b'kazuya-stegano'

# p = Path('.')

p = sorted(Path('folder').glob('**/*'))
for x in p:
  if x.is_file():
    print(x.read_bytes()[:len(stegano)])