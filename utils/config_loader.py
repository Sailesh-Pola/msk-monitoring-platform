# utils/config_loader.py
import yaml
import os

def load_config(config_path="config/config.yaml"):
    # Anchor to project root (one level up from utils/)
    utils_dir    = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(utils_dir)
    config_abs   = os.path.join(project_root, config_path)

    if not os.path.exists(config_abs):
        raise FileNotFoundError(f"Config file not found: {config_abs}")

    with open(config_abs, "r") as f:
        config = yaml.safe_load(f)

    return config