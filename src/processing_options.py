from dataclasses import dataclass


@dataclass
class ProcessingOptions:
    export_option: str = "premiere"
    directory: str = ""
    threshold: float = 0.04
    margin: float = 0.2
    files_into_folders: bool = False
    split_only: bool = False
    separate_tracks: bool = False
