red='\033[0;31m'
green='\033[0;32m'
yellow='\033[0;33m'
blue='\033[0;34m'
purple='\033[0;35m'
cyan='\033[0;36m'
white='\033[0;37m'
end='\033[0m'

help(){
    printf "Run：$red sh repackage.sh $green<verb> $yellow<args>$end\n"
    format="  $green%-6s $yellow%-12s$end%-20s\n"
    printf "$format" "" "" "打包"
    printf "$format" "-v" "<version>" "更改版本"
    printf "$format" "-up" "" "上传"
    printf "$format" "-h" "" "帮助"
}
package(){
    rm -rf *.egg-info build dist && python3 setup.py bdist_wheel
}
case $1 in 
    -h)
        help ;;
    -v)
        if [ "$2"z = "z" ];then
            version=`cat setup.py | grep version=`
            printf "$yellow current%s $end\n" "$version"
            exit 0
        fi
        sed -i "s/version:.*/version: $2')/g" baidu_trans_cli/__init__.py
        sed -i "s/version='.*/version='$2'/g" setup.py
        printf "$green change version to %s $end\n" "$2"
    ;;
    -up)
        package
        echo "prepare to upload"
        twine upload dist/*
    ;;
    *)
        package
    ;;
esac