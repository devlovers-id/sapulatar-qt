#!/bin/bash

mainDir=$HOME/.local/share/devlovers-id


if [[ $1 == "--uninstall" ]]; then
    echo "Uninstalling"
    rm -rf $mainDir
    rm $HOME/.local/share/icons/sapulatar-qt.png
    rm $HOME/.local/bin/sapulatar-qt
    rm $HOME/.local/share/applications/sapulatar-qt.desktop
    exit
fi

# Checking dependencies
echo -e "Checking dependencies:"
git --version 
GITRESULT=$?
if [[ ! $GITRESULT -eq 0 ]]; then 
    echo "Git not found! Please install git first!" 
fi

## python version
python3.8 --version 
PYRESULT=$?
if [[ ! $PYRESULT -eq 0 ]]; then 
    if [[ $(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))') < 3.7.99  ]]; then  
        echo -e "Sapulatar need Python 3.8.x or newer \nexit now!"
        exit
    else
        PYVER="python3"
        echo -e "upgrading pip"
        $PYVER -m pip install --upgrade pip --user
    fi
else
    PYVER="python3.8"
    echo -e "Found: $(python3.8 --version)"
    echo -e "upgrading pip"
    $PYVER -m pip install --upgrade pip --user
fi




# Cloning repo
if [[ ! -d $mainDir ]]; then
    mkdir $mainDir
    git clone https://github.com/devlovers-id/sapulatar-qt.git $mainDir/sapulatar-qt
    cd $mainDir/sapulatar-qt
else
    cd $mainDir/sapulatar-qt
    git pull origin master
fi

# get rembg
echo "Checking PySide2 & Rembg"

pip list | grep PySide2
PYSIDERESULT=$?
if [[ ! $PYSIDERESULT -eq 0 ]]; then
    echo -e "PySide2 not installed! Get it now ..."
    $PYVER -m pip install pyside2
fi

pip list | grep rembg
PYSIDERESULT=$?
if [[ ! $PYSIDERESULT -eq 0 ]]; then
    echo -e "rembg not installed! Get it now ..."
    $PYVER -m pip install rembg
fi


# copiying files
echo "Copying files ..."
sleep 1
echo "Copying icon"
cp $mainDir/sapulatar-qt/assets/sapulatar-qt.png $HOME/.local/share/icons/sapulatar-qt.png

echo "Copying executable"
echo -e "#!/bin/bash\n" >> /$HOME/.local/bin/sapulatar-qt
echo -e "if [[ \$1 == \"--uninstall\" ]]; then\n    echo \"Uninstalling\"\n\trm -rf $mainDir\n\trm $HOME/.local/share/icons/sapulatar-qt.png\n\trm $HOME/.local/bin/sapulatar-qt\n\trm $HOME/.local/share/applications/sapulatar-qt.desktop\n\texit\nfi" >> $HOME/.local/bin/sapulatar-qt
echo "cd $(echo $mainDir/sapulatar-qt)" >> $HOME/.local/bin/sapulatar-qt
echo -e "\n$PYVER main.py" >> $HOME/.local/bin/sapulatar-qt
chmod +x $HOME/.local/bin/sapulatar-qt

echo "Copying launcher"
cp $mainDir/sapulatar-qt/assets/sapulatar-qt.desktop $HOME/.local/share/applications/sapulatar-qt.desktop

# checking installation
echo "Instalation complete!"
