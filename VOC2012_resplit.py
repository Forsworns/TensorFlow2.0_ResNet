# /bin/python3

from pathlib import Path
import os
import shutil

if __name__ == "__main__":
    print("build the dataset for exp, negelect the original splitting")
    label_p = Path("./ImageSets/Main")
    for p in label_p.glob("*_*.txt"):
        print(p)
        stem = p.stem
        label = stem[:stem.find("_")]     
        target_dir = f"./original_dataset/{label}"
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        with p.open() as f:
            for line in f:
                fig_name = line.split(' ')[0]
                fig_path = f"./JPEGImages/{fig_name}.jpg"
                target_path = f"{target_dir}/{fig_name}.jpg"
                shutil.copy(fig_path, target_path)
                    