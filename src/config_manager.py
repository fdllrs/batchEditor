from pathlib import Path
from PySide6 import QtCore

# Built-in defaults — used when no saved config exists.
_DEFAULT_CONFIG: dict = {
    "export_option": "premiere",
    "track_thresholds": [4.0, 4.0, 2.0, -1.0],
    "margin": 0.2,
    "split_only": False,
}

_APP_NAME = "batchEditor"
_LAST_SAVED_FILENAME = "last_saved_config.txt"


def last_saved_config_path() -> Path:
    """Return the OS-appropriate path for the auto-saved config file.

    Uses QStandardPaths so the location is always inside the user's
    application-data directory (e.g. %APPDATA%\\batchEditor on Windows).
    """
    data_dir = QtCore.QStandardPaths.writableLocation(
        QtCore.QStandardPaths.StandardLocation.AppDataLocation
    )
    return Path(data_dir) / _APP_NAME / _LAST_SAVED_FILENAME


CONFIG_KEYS = [
    "export_option",
    "track_thresholds",
    "margin",
    "split_only",
]


def save_config(path: Path, config: dict) -> None:
    """Write a config dict to a plain key=value text file."""
    with open(path, "w", encoding="utf-8") as f:
        for key in CONFIG_KEYS:
            value = config.get(key, "")
            if isinstance(value, bool):
                value = "true" if value else "false"
            elif isinstance(value, list):
                value = ";".join(str(v) for v in value)
            f.write(f"{key}={value}\n")


def last_saved_config() -> dict | None:
    """Load the last auto-saved config, or return None if it doesn't exist."""
    path = last_saved_config_path()
    if path.exists():
        return load_config(path)
    return None


def default_config() -> dict:
    """Return a copy of the built-in default configuration."""
    return dict(_DEFAULT_CONFIG)


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
    bool_keys = {"split_only"}
    if key in bool_keys:
        return raw.lower() == "true"
    if key == "track_thresholds":
        return [float(x) for x in raw.split(";") if x.strip()]
    if key == "margin":
        return float(raw)
    return raw
