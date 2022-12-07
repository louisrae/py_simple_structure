#!/opt/homebrew/bin/zsh
echo What is your old virtual environment name
read old_virtual_environment

echo What is your new virtual environment name
read new_virtual_environment

$HOME/.pyenv/versions/3.10.6/envs/$old_virtual_environment/bin/pip freeze > $HOME/Documents/dev/requirements.txt
pyenv virtualenv $new_virtual_environment

echo Now run pyenv activate $new_virtual_environment

echo Then run pip3 install -r $HOME/Documents/dev/requirements.txt

echo Then run rm $HOME/Documents/dev/requirements.txt

