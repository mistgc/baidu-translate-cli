# baidu-trans-cli

Fork from: [baidu-trans-cli](https://gitee.com/gin9/baidu-trans-cli)

## install 

```bash
git clone --depth 1 https://github.com/zaiic/baidu-translate-cli.git

cd baidu-translate-cli

python setup.py sdist

cd dist

pip install baidu-translate-cli-0.2.3.tar.gz
```

## uninstall

```bash
pip uninstall baidu-translate-cli
```

## get a key 

1. register a account on [this site](http://api.fanyi.baidu.com/api/trans/product/index) `1000,000 characters per month is free.`

1. get 'appid' and 'secretKey', write into `~/.config/baidu-trans-cli/main.json`


## Use
> trans -h 
> 
> trans "hello, world."
