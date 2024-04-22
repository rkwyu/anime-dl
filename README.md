# anime-dl 動畫下載
[![Coverage Status](https://coveralls.io/repos/github/rkwyu/anime-dl/badge.svg?branch=main)](https://coveralls.io/github/rkwyu/anime-dl?branch=main)

## About ##
A tool to get anime from different websites with CLI (Command Line Interface).  
It currently supports to download following websites:  
  
✅ [anime1.in](https://anime1.in/)  
✅ [anime1.me](https://anime1.me/)  
✅ [yhdm.one](https://yhdm.one/)  
✅ [xgcartoon.com](https://www.xgcartoon.com/)  

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
