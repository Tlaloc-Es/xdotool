import subprocess
from typing import List, Optional


def key(
    keysequence: List[str],
    clearmodifiers: Optional[bool] = None,
    delay: Optional[float | str] = None,
    repeat: Optional[int | str] = None,
    repeat_delay: Optional[float | str] = None,
    window: Optional[str] = None,
) -> None:
    command = ["xdotool", "key"]

    if clearmodifiers:
        command.append("--clearmodifiers")

    if delay:
        command.extend(["--delay", str(delay)])

    if repeat:
        command.extend(["--repeat", str(repeat)])

    if repeat_delay:
        command.extend(["--repeat-delay", str(repeat_delay)])

    if window:
        command.extend(["--window", str(window)])

    command.extend(keysequence)

    print(" ".join(command))

    subprocess.call(command)


def selectwindow():
    result = subprocess.check_output(
        ["xdotool", "selectwindow", "getmouselocation", "--shell"]
    )
    result = result.decode("utf-8").splitlines()
    return {
        "X": result[0].replace("X=", ""),
        "Y": result[1].replace("Y=", ""),
        "SCREEN": result[2].replace("SCREEN=", ""),
        "WINDOW": result[3].replace("WINDOW=", ""),
    }


def windowactivate(window: str | int):
    subprocess.call(["xdotool", "windowactivate", str(window)])
