#!/bin/bash

declare -A icons=(
  ["keyboard-us"]="󰌓"
  ["mozc"]="󱌴"
)

method=$(fcitx5-remote -n)

icon="${icons[$method]:-󰌓}"

echo "{\"text\":\"$icon\", \"tooltip\":\"$method\"}"
