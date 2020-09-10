echo "PROGRAMS."
echo "updateing Programs........."
git stash
git pull --rebase origin master
git stash pop
figlet -f small updated !
bash install.sh
echo "[ updating Finished..]"
