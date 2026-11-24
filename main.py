"""News-image entry: copy the pre-rendered entry.png to the output dir.

Standard library only. The program runs with no network and a read-only
repository, so it copies the image shipped beside it, byte for byte.
"""
import os
import shutil

IMAGE_NAME = "entry.png"


def entry_paths():
    """Resolve (source, destination) for the image to ship."""
    here = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return (os.path.join(here, IMAGE_NAME),
            os.path.join(out_dir, IMAGE_NAME))


def main():
    src, dest = entry_paths()
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copyfile(src, dest)
    # Both runs must write the same bytes: fail loudly if the copy
    # did not land complete.
    if os.path.getsize(src) != os.path.getsize(dest):
        raise SystemExit("entry.png copy incomplete")


if __name__ == "__main__":
    main()
