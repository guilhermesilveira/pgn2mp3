import subprocess
import shlex
from cache import Cache


def slowdown(name: str, file:str, slow_cache: Cache):
    # ffmpeg file to slow down to 74% with same file name but folder same_folder/74/
    new_name = slow_cache.get_key_path(name, 'mp3')
    silence_it = "-hide_banner -loglevel panic"
    command_string = f"ffmpeg -y {silence_it} -i {shlex.quote(file)} -filter:a \"atempo=0.74\" -vn {shlex.quote(new_name)}"

    # runs it, if fails, stop
    result = subprocess.run(command_string, shell=True,
                            text=True, stderr=subprocess.PIPE)

    if result.returncode:
        logging.error(f"Failed to run ffmpeg command: {command_string}")
        logging.error(f"Error message: {result.stderr}")
        exit(1)

    return new_name
