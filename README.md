# Anime-dl 動畫下載 [![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org) ![GitHub last commit (branch)](https://img.shields.io/github/last-commit/rkwyu/anime-dl/main) [![Coverage Status](https://coveralls.io/repos/github/rkwyu/anime-dl/badge.svg?branch=main)](https://coveralls.io/github/rkwyu/anime-dl?branch=main)  

<a href="https://buymeacoffee.com/r1y5i" target="_blank">
<img style="border-radius: 20px" src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174">
</a>

---

A command-line and web UI tool for downloading anime and animation content where legally permitted.

## ⚠️ Legal & Ethical Notice ##

Use this tool only on content you are authorized to download, such as:
- Anime you uploaded yourself
- Publicly available or officially free releases
- Creative Commons or licensed animation content

The authors __do not verify licenses__ and are __not responsible for misuse__.

Downloading copyrighted content without permission may violate copyright law.

## About ##

__anime-dl__ allows you to download anime and animation content from supported websites efficiently, using either CLI or a WebUI interface.

> This tool does __not__ bypass protections or provide access to content without authorization.

## Prerequisites ##

- Python 3.10+
- FFmpeg (https://www.ffmpeg.org)

Check installation:
```console
python --version
ffmpeg -version
```

## Setup ##
```console
git clone https://github.com/rkwyu/anime-dl
cd anime-dl
python -m pip install -r requirements.txt
```

## Configuration ##
Set the output directory in `config.ini`
```ini
[DIRECTORY]
output=./output
```

## Usage (CLI) ##
```console
python run.py [options] <URL>
```

__Note__: Ensure you have the legal right to download content from the given URL.

## Usage (WebUI) ##
```console
python webUI.py
```
Visit the local URL shown in logs (usually http://127.0.0.1:7860) to use the WebUI.

![anime-al screenshot](docs/screenshot.png?raw=true "anime-al")

> Only use the WebUI for content you have the right to download.

## Supported Sites ##

The tool can work with multiple anime and animation sites.

> The README does not list specific sites to avoid promoting potentially infringing sources. Users are responsible for ensuring they are authorized to download content.

To see the current list of supported sites, run:
```console
python run.py --list-sites
```

Output example:
```console
Supported extractors:
- SiteA
- SiteB
- SiteC
```

> We do not guarantee legality of any site. Users must ensure they are authorized to download content.

## Why This Matters ##

Tools like this can be misused to download content without authorization. This README clarifies that __anime-dl__ is intended only for content users are legally permitted to download.

## Disclaimer ##

- Not affiliated with any anime site.
- All trademarks and copyrights belong to their respective owners.

## License ##
This project is licensed under the [MIT License](LICENSE.md)

