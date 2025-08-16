#!/bin/bash

# Show options using rofi (or wofi if you're on Wayland)
choice=$(printf "󰌓 English US\n󱌴 Japanese\n Configuration" | rofi -dmenu -p "Fcitx5 Menu")

case "$choice" in
  "󰌓 English US")
    fcitx5-remote -s keyboard-us
    ;;
  "󱌴 Japanese")
    fcitx5-remote -s mozc
    ;;
  " Configuration")
    fcitx5-configtool
    ;;
esac
