#!/bin/bash

log_file="$HOME/.config/waybar/update_counts.log"

repo_updates=$(checkupdates 2>/dev/null | wc -l)

aur_updates=$(yay -Qua 2>/dev/null | wc -l)

flatpak_updates=$(flatpak remote-ls --updates 2>/dev/null | wc -l)

total=$((repo_updates + aur_updates + flatpak_updates))

echo "{\"text\": \" $total\", \"tooltip\": \"Pacman: $repo_updates\\nAUR: $aur_updates\\nFlatpak: $flatpak_updates\"}"
