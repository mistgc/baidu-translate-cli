rm -rf *.egg-info build dist &&
	python3 setup.py bdist_wheel

if [ "$1" = "up" ];then 
	echo "prepare upload"
    twine upload dist/*
fi
