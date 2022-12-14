from datasets import Dataset, Image, concatenate_datasets
from pathlib import Path
from tqdm import tqdm
import time
import sys

root = Path(__file__).resolve().parent
warmup = 100
decode = "--decode" in sys.argv[1:]

ds = concatenate_datasets([
    Dataset.from_file(str(root / "arrow" / f"dataset_0000{i}_of_00004.arrow"))
    for i in range(4)
]).cast_column("image", Image(decode=decode))

for i, example in tqdm(enumerate(ds), unit="ex", total=10_000):
    if i == 0:
        print("First example: \t", str(example)[:500], "...")
    if i == warmup:
        _start = time.time()

_end = time.time()
total = i + 1
print(f"Done in {_end - _start:.1f}sec")
print(f"Average speed on {total} examples:\t{total / (_end - _start):.1f}examples/sec")
