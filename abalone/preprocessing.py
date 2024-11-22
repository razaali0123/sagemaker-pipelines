
import os
import shutil

def copy_files(input_dir, output_dir):
    """
    Copies all files and subdirectories from input_dir to output_dir.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for item in os.listdir(input_dir):
        src_path = os.path.join(input_dir, item)
        dest_path = os.path.join(output_dir, item)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
            print(f"Copied directory {src_path} to {dest_path}")
        else:
            shutil.copy2(src_path, dest_path)
            print(f"Copied file {src_path} to {dest_path}")

if __name__ == "__main__":
    base_dir = "/opt/ml/processing/input/train"
    base_dir2 = "/opt/ml/processing/input/test"
    train_output_dir = "/opt/ml/processing/output/train"
    test_output_dir = "/opt/ml/processing/output/test"

    # Copy files for train
    copy_files(base_dir, train_output_dir)

    # Copy files for test
    copy_files(base_dir2, test_output_dir)

    print("File copying completed.")


    print("######################### PROCESSING ENDED ... ################################")
