# Qtile

### repositorio

```sh
git clone git@github.com:morenorafael/sophie.git
```

## Dependencias

```sh
sudo pacman -Syyu
```

```sh
sudo pacman -S pulseaudio-bluetooth bat exa docker docker-compose flameshot bluez bluez-utils nodejs npm neovim python-neovim ttf-ubuntu-mono-nerd ttf-font-awesome zip unzip neofetch zsh git firefox dunst gnu-netcat bind-tools picom wireless_tools
```

## zsh

```sh
sudo pacman -Syyu
```

```sh
sudo pacman -S zsh
```

### Oh My ZSH

```sh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### zsh-autosuggestions

```sh
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

### ZSH-Syntax-Highlighting

```sh
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

## Docker

```sh
sudo pacman -Syyu
```

```sh
sudo pacman -S docker docker-compose
```

```sh
sudo systemctl start docker.service
```

```sh
sudo systemctl enable docker.service
```

```sh
sudo usermod -aG docker $USER
```

## Bluetooth

```sh
sudo pacman -S bluez bluez-utils pulseaudio-bluetooth
```

```sh
pulseaudio --kill
```

```sh
pulseaudio --start
```

```sh
sudo usermod -aG lp,audio $USER
```

## Notifications

```sh
sudo pacman -S dunst
```

```sh
ln -s ~/sophie/.config/dunst ~/.config/dunst
```

## Picom

```sh
sudo pacman -S picom
```

```sh
 ln -s ~/sophie/.config/picom ~/.config/picom
```

```sh
picom -b --config ~/.config/picom/picom.conf
```

## GTK

```sh
ln -s ~/sophie/.gtkrc-2.0 ~/.gtkrc-2.0
```

```sh
ln -s ~/sophie/.config/gtk-3.0 ~/.config/gtk-3.0
```

## vscode

```sh
yay -S visual-studio-code-bin
```

#### settings.json

```json
{
  "workbench.colorTheme": "Nord",
  "editor.fontFamily": "Inconsolata, 'Droid Sans Mono', 'monospace', monospace",
  "editor.fontLigatures": true,
  "workbench.colorCustomizations": {
    "[Nord]": {
      "titleBar.activeBackground": "#3B4252"
    }
  },
  "window.titleBarStyle": "custom"
}
```
