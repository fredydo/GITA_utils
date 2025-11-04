import os
import argparse
import pandas as pd
import ffmpeg

def cut_audio_segments(csv_path, base_dir, output_folder, sep=";", decimal=","):
    df = pd.read_csv(csv_path, sep=sep, decimal=decimal)
    print(f"Loaded {len(df)} rows from {csv_path}\n")

    for idx, row in df.iterrows():
        input_path = os.path.join(base_dir, row["Path"]).replace("\\", "/")
        start = float(row["Start"])
        end = float(row["End"])
        duration = end - start

        if not os.path.exists(input_path):
            print(f"[{idx+1}/{len(df)}] File not found: {input_path}")
            continue

        # Build output path
        input_filename = os.path.basename(input_path)
        output_name = "_".join(input_filename.split("_")[:3]) + "_" + row["Task"].split()[0] + ".wav"

        # Create output directory
        output_dir = os.path.dirname(input_path).replace("/original", f"/{output_folder}")
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, output_name).replace("\\", "/")

        print(f"[{idx+1}/{len(df)}] Cutting {input_filename}: {start:.2f} - {end:.2f}s → {output_name}")

        try:
            (
                ffmpeg
                .input(input_path, ss=start, t=duration)
                .output(output_path, acodec="copy")
                .overwrite_output()
                .run(capture_stdout=True, capture_stderr=True)
            )
            print(f"Saved: {output_path}\n")
        except ffmpeg.Error as e:
            print(f"ffmpeg error for {input_filename}")
            print(e.stderr.decode())
            print("-" * 60)

def main():
    parser = argparse.ArgumentParser(
        description="Cut audio segments from a CSV file using ffmpeg."
    )
    parser.add_argument("--csv", default="AtHome segments.csv", help="Path to the CSV file with segments info")
    parser.add_argument("--base-dir", default=os.getcwd(), help="Base directory for relative audio paths")
    parser.add_argument("--output-folder", default="segmented", help="Name of output folder (replaces 'original')")
    parser.add_argument("--sep", default=";", help="CSV separator (default=';')")
    parser.add_argument("--decimal", default=",", help="Decimal separator (default=',')")

    args = parser.parse_args()

    cut_audio_segments(
        csv_path=args.csv,
        base_dir=args.base_dir,
        output_folder=args.output_folder,
        sep=args.sep,
        decimal=args.decimal,
    )

if __name__ == "__main__":
    main()
