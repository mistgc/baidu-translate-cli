if [ "$1"z = "z" ];then
    echo "please input version"
    exit 0
fi

sed -i "s/version:.*/version:$1')/g" baidu_trans_cli/__init__.py
sed -i "s/version='.*/version='$1',/g" setup.py

rm -rf *.egg-info build dist && python3 setup.py bdist_wheel

if [ "$2" = "up" ];then 
	echo "prepare to upload"
    twine upload dist/*
fi
