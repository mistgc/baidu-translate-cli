rm -rf *.egg-info build dist && python3 setup.py bdist

if [ "$1" = "up" ];then 
	echo "prepare to upload"
    twine upload dist/*
fi
