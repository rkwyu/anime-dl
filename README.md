# Anime-dl 動畫下載 [![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org) ![GitHub last commit (branch)](https://img.shields.io/github/last-commit/rkwyu/anime-dl/main) [![Coverage Status](https://coveralls.io/repos/github/rkwyu/anime-dl/badge.svg?branch=main)](https://coveralls.io/github/rkwyu/anime-dl?branch=main)  

<a href="https://buymeacoffee.com/abe0" target="_blank">
<img style="border-radius: 20px" src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174">
</a>

## Difference ##
This fork allowed you to choose specific seasons and episodes to download. What's more is that it support cc subtitles from xgcartoon.

## About ##
A tool to get anime from different websites with [CLI (Command Line Interface)](#usage-cli) and [WebUI](#usage-webui).  
It currently supports following websites:  
- [x] [anime1.in](https://anime1.in/)  
- [x] [anime1.me](https://anime1.me/)  
- [x] [yhdm.one](https://yhdm.one/)  
- [x] [xgcartoon.com](https://www.xgcartoon.com/)
- [x] [lincartoon.com](https://www.lincartoon.com/)
- [x] [agdm.tv](https://www.agdm.tv/)

Pending to supports:  
- [ ] [kickassanime.mx](https://www1.kickassanime.mx/)
- [ ] [iyinghua.io](http://www.iyinghua.io/)

## Prerequisites ##
Please make sure the following tool(s) / application(s) are properly setup and ready to use:
- FFmpeg ([https://www.ffmpeg.org/](https://www.ffmpeg.org/))

## Setup ##
1. Download repository  
```console
git clone https://github.com/rkwyu/anime-dl
```
2. Install dependencies
```console
cd ./anime-dl
python -m pip install -r requirements.txt
```

## Configuration ##
Output directory can be configured in `config.ini`
```ini
[DIRECTORY]
output=./output
```

## Usage (CLI) ##
```console
python run.py {URL}
```

#### Example 1: Download all episodes of 《Chainsaw Man Season 1》 ####
```console
python run.py https://www.xgcartoon.com/detail/dianjurenriyu-tengbenshu
```
#### Example 1: Download episode 01 of 《Chainsaw Man Season 1》 ####
```console
python run.py https://www.xgcartoon.com/video/dianjurenriyu-tengbenshu/vRsDVLPPou.html
```

## Usage (WebUI) ##
```console
python webUI.py
```
After the logs are shown as below, go to [http://127.0.0.1:7860](http://127.0.0.1:7860)
```console
Running on local URL:  http://127.0.0.1:7860

To create a public link, set `share=True` in `launch()`.
```
![anime-al screenshot](docs/screenshot.png?raw=true "anime-al")


## License ##
This project is licensed under the [MIT License](LICENSE.md)

