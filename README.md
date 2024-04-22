# anime-dl 動畫下載 ![GitHub last commit (branch)](https://img.shields.io/github/last-commit/rkwyu/anime-dl/main) [![Coverage Status](https://coveralls.io/repos/github/rkwyu/anime-dl/badge.svg?branch=main)](https://coveralls.io/github/rkwyu/anime-dl?branch=main)

[![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

## About ##
A tool to get anime from different websites with CLI (Command Line Interface).  
It currently supports following websites:  
- [x] [anime1.in](https://anime1.in/)  
- [x] [anime1.me](https://anime1.me/)  
- [x] [yhdm.one](https://yhdm.one/)  
- [x] [xgcartoon.com](https://www.xgcartoon.com/)

Pending to supports:  
- [ ] [kickassanime.mx](https://www1.kickassanime.mx/)
- [ ] [iyinghua.io](http://www.iyinghua.io/)

## Prerequisites ##
To running this tool, please make sure the following prerequisites are ready:
* [FFmpeg](https://www.ffmpeg.org/)

## Usage (CLI) ##
Before running the application, required packages need to be installed by following command:
```console
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
$ cd ./anime-dl
$ python -m pip install -r requirements.txt
$ python run.py {URL}
```

#### Example ####
鏈鋸人（電鋸人）第1季【日語】,  
series URL: https://www.xgcartoon.com/detail/dianjurenriyu-tengbenshu  
episode 1 URL: https://www.xgcartoon.com/user/page_direct?cartoon_id=dianjurenriyu-tengbenshu&chapter_id=vRsDVLPPou  
```console
# download all episodes in the series
$ python run.py https://www.xgcartoon.com/detail/dianjurenriyu-tengbenshu

# download a single episode
$ python run.py https://www.xgcartoon.com/user/page_direct?cartoon_id=dianjurenriyu-tengbenshu&chapter_id=vRsDVLPPou
```

## License ##
[GNU GPL v3.0](LICENSE.md)
