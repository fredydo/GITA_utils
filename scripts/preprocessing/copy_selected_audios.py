import argparse
import shutil
from pathlib import Path

def copy_selected_audios(source, dest, keywords, preserve_structure=False):
    keywords = [k.lower() for k in keywords]
    src_path = Path(source)
    dst_path = Path(dest)
    dst_path.mkdir(parents=True, exist_ok=True)

    wav_files = list(src_path.rglob("*.wav"))
    print(f"Found {len(wav_files)} .wav files in {source}\n")

    copied = 0
    for wav_file in wav_files:
        filename_lower = wav_file.name.lower()
        if not any(k in filename_lower for k in keywords):
            continue

        # Build destination path
        if preserve_structure:
            relative = wav_file.relative_to(src_path)
            out_path = dst_path / relative
            out_path.parent.mkdir(parents=True, exist_ok=True)
        else:
            out_path = dst_path / wav_file.name

        try:
            shutil.copy2(wav_file, out_path)
            copied += 1
            print(f"[{copied}] Copied: {wav_file} → {out_path}")
        except Exception as e:
            print(f"Error copying {wav_file}: {e}")

    print(f"\nDone! Copied {copied} files matching {keywords}.\n")

def main():
    parser = argparse.ArgumentParser(
        description="Copy .wav files containing given keywords."
    )
    parser.add_argument("--source", required=True, help="Source directory to search recursively")
    parser.add_argument("--dest", required=True, help="Destination directory for copied files")
    parser.add_argument("--keywords", nargs="+", required=True, help="Keywords to match (case-insensitive)")
    parser.add_argument("--preserve-structure", action="store_true", help="Preserve folder structure")

    args = parser.parse_args()

    copy_selected_audios(
        source=args.source,
        dest=args.dest,
        keywords=args.keywords,
        preserve_structure=args.preserve_structure,
    )

if __name__ == "__main__":
    main()
