#!/bin/bash

sudo pacman -S --noconfirm which alacritty qtile rofi ttf-dejavu ttf-liberation noto-fonts pulseaudio pavucontrol pamixer brightnessctl udiskie dunst picom pulseaudio-bluetooth bat exa flameshot bluez bluez-utils ttf-ubuntu-mono-nerd ttf-font-awesome zip unzip neofetch zsh git gnu-netcat bind-tools wireless_tools base-devel libmtp thunar ranger




# Instalar AUR helper
if [ -d "/opt/yay-git" ]; then
  echo "AUR helper ya esta instalado"
else
  cd /opt/
  sudo git clone https://aur.archlinux.org/yay-git.git
  sudo chown -R $USER:$USER yay-git/
  cd yay-git
  makepkg -si
  cd
fi


# Instalar alacritty
if [ -e "/home/$USER/.config/alacritty" ]; then
  rm -rf /home/$USER/.config/alacritty
fi

ln -s /home/$USER/sophie/.config/alacritty /home/$USER/.config/alacritty

echo "Se instalo alacritty"




# Instalar qtile
rm -rf /home/$USER/.config/qtile
ln -s /home/$USER/sophie/.config/qtile /home/$USER/.config/qtile

echo "Se instalo qtile"




# Instalar rofi
echo "Se instalo rofi"




# Instalar zsh
# sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-/home/$USER/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
# git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-/home/$USER/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

if [ -e "/home/$USER/.zshrc" ]; then
  rm -rf /home/$USER/.zshrc
fi

ln -s /home/$USER/sophie/.zshrc /home/$USER/.zshrc

echo "Se instalo zsh"




# Instalar dunst
if [ -e "/home/$USER/.config/dunst" ]; then
  rm -rf /home/$USER/.config/dunst
fi

ln -s /home/$USER/sophie/.config/dunst /home/$USER/.config/dunst

echo "Se instalo dunst"




# Instalar picom
if [ -e "/home/$USER/.config/picom" ]; then
  rm -rf /home/$USER/.config/picom
fi

ln -s /home/$USER/sophie/.config/picom /home/$USER/.config/picom
picom -b --config /home/$USER/.config/picom/picom.conf

echo "Se instalo picom"

cd resources && ./install.sh

reboot