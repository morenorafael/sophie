#!/bin/bash

sudo pacman -S --noconfirm xorg-xinit feh xcb-util-cursor

if [ -e "/home/$USER/.xprofile" ]; then
  rm -rf /home/$USER/.xprofile
fi

ln -s /home/$USER/sophie/.xprofile /home/$USER/.xprofile

echo "Se instalo el archivo .xprofile"




# Instalar xcb-util-cursor
echo "Instalando el cursor..."
if [ -d "/usr/share/icons/Breeze" ] && [ "$(ls -A /usr/share/icons/Breeze)" ]; then
  echo "El directorio '/usr/share/icons/Breeze' ya existe y no está vacío."
  rm -rf Breeze
else
  tar -xf Breeze.tar.tar
  sudo mv Breeze /usr/share/icons
fi

echo "Instalando el tema..."
if [ -d "/usr/share/themes/Nordic" ] && [ "$(ls -A /usr/share/themes/Nordic)" ]; then
  echo "El directorio '/usr/share/themes/Nordic' ya existe y no está vacío."
  rm -rf Nordic
  rm -rf Nordic-v40
else
  tar -xf Nordic.tar.xz
  sudo mv Nordic /usr/share/themes
fi

echo "Instalando los iconos..."
if [ -d "/usr/share/icons/Zafiro-Nord-Dark-Black" ] && [ "$(ls -A /usr/share/icons/Zafiro-Nord-Dark-Black)" ]; then
  echo "El directorio '/usr/share/icons/Zafiro-Nord-Dark-Black' ya existe y no está vacío."
  rm -rf Zafiro-Nord-Dark-Black
else
  tar -xf Zafiro-Nord-Dark-Black.tar.xz
  sudo mv Zafiro-Nord-Dark-Black /usr/share/icons
fi


if [ -e "/home/$USER/.gtkrc-2.0" ]; then
  rm -rf /home/$USER/.gtkrc-2.0
fi

ln -s /home/$USER/sophie/.gtkrc-2.0 /home/$USER/.gtkrc-2.0

if [ -e "/home/$USER/.config/gtk-3.0" ]; then
  rm -rf /home/$USER/.config/gtk-3.0
fi

ln -s /home/$USER/sophie/.config/gtk-3.0 /home/$USER/.config/gtk-3.0