from dataclasses import dataclass, field


@dataclass
class ProcessingOptions:
    export_option: str = "premiere"
    directory: str = ""
    track_thresholds: list[float] = field(default_factory=lambda: [-1.0])
    margin: float = 0.2
    files_into_folders: bool = False
    split_only: bool = False
    separate_tracks: bool = False
    max_parallel: int = 2
