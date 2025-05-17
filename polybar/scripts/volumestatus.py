import subprocess
import json
import os

command = "~/.cargo/bin/goxlr/goxlr-client"
command = os.path.expanduser(command)
args = [command, "--status-json"]
xlr_status = subprocess.check_output(args)

xlr_status = json.loads(xlr_status)

mixer_serial = list(xlr_status["mixers"].keys())[0]
mixer = xlr_status["mixers"][mixer_serial]
volumes = mixer["levels"]["volumes"]
system_volume = volumes["System"]
mic_volume = volumes["Mic"]
chat_volume = volumes["Chat"]
music_volume = volumes["Music"]
game_volume = volumes["Game"]


system_volume_pct = int(system_volume / 255 * 100)
mic_volume_pct = int(mic_volume / 255 * 100)
chat_volume_pct = int(chat_volume / 255 * 100)
music_volume_pct = int(music_volume / 255 * 100)
game_volume_pct = int(game_volume / 255 * 100)


faders = mixer["fader_status"]

system_muted = faders["D"]["mute_state"] != "Unmuted"
mic_muted = mixer["cough_button"]["state"] != "Unmuted"
chat_muted = faders["B"]["mute_state"] != "Unmuted"
music_muted = faders["C"]["mute_state"] != "Unmuted"
game_muted = faders["A"]["mute_state"] != "Unmuted"

system_icons = ""
mic_icons = ""
chat_icons = "󰭹󱐑"
music_icons = "󰟎"
game_icons = "󰖺󰖻"

if system_muted or system_volume == 0:
    system_icon = system_icons[2]
elif 1 <= system_volume_pct <= 50:
    system_icon = system_icons[1]
else:
    system_icon = system_icons[0]

if mic_muted or mic_volume == 0:
    mic_icon = mic_icons[1]
else:
    mic_icon = mic_icons[0]

if chat_muted or chat_volume == 0:
    chat_icon = chat_icons[1]
else:
    chat_icon = chat_icons[0]

if music_muted or music_volume == 0:
    music_icon = music_icons[1]
else:
    music_icon = music_icons[0]

if game_muted or game_volume == 0:
    game_icon = game_icons[1]
else:
    game_icon = game_icons[0]

print(
    system_icon,
    system_volume_pct,
    mic_icon,
    mic_volume_pct,
    chat_icon,
    chat_volume_pct,
    music_icon,
    music_volume_pct,
    game_icon,
    game_volume_pct,
)
