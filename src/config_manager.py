from pathlib import Path

# Resolved relative to this file: src/ -> project root -> default_config.txt
DEFAULT_CONFIG_PATH: Path = Path(__file__).parent.parent / "default_config.txt"


CONFIG_KEYS = [
    "export_option",
    "threshold",
    "margin",
    "files_into_folders",
    "split_only",
    "separate_tracks",
]


def save_config(path: Path, config: dict) -> None:
    """Write a config dict to a plain key=value text file."""
    with open(path, "w", encoding="utf-8") as f:
        for key in CONFIG_KEYS:
            value = config.get(key, "")
            if isinstance(value, bool):
                value = "true" if value else "false"
            f.write(f"{key}={value}\n")


def default_config() -> dict:
    """Load the default config if it exists, otherwise return an empty dict."""
    if DEFAULT_CONFIG_PATH.exists():
        return load_config(DEFAULT_CONFIG_PATH)
    return {}


def load_config(path: Path) -> dict:
    """Read a plain key=value text file and return the config dict."""
    config = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip()
            if key in CONFIG_KEYS:
                config[key] = _parse_value(key, value)
    return config


def _parse_value(key: str, raw: str):
    bool_keys = {"files_into_folders", "split_only", "separate_tracks"}
    if key in bool_keys:
        return raw.lower() == "true"
    if key == "threshold" or key == "margin":
        return float(raw)
    return raw
