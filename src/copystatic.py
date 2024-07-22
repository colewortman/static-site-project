import os
import shutil

def copy_contents(copy_path, target_path):
    if os.path.exists(target_path):
        shutil.rmtree(target_path)
    os.makedirs(target_path)

    for item in os.listdir(copy_path):
        source_item_path = os.path.join(copy_path, item)
        target_item_path = os.path.join(target_path, item)

        if os.path.isfile(source_item_path):
            shutil.copy(source_item_path, target_item_path)
        elif os.path.isdir(source_item_path):
            copy_contents(source_item_path, target_item_path)
        
        print(f"Copied {source_item_path} to {target_item_path}")