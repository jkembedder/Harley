clear
echo "Welcome to installation of programs "
echo " "
echo " "
echo "Updating system........................."
echo " "
echo " "
apt-get update && upgrade
echo " "
echo " "
echo "installing figlet, toilet and cowsay..."
echo " "
echo " "
apt-get install figlet toilet cowsay
echo " "
echo " "
figlet -f small Processing!
echo "Installing gcc..."
echo " "
echo " "
pkg install clang
echo "Installing python pkgs.................."
echo " "
echo " "
apt-get install python
apt-get install python2
echo " "
echo " "
echo "Compiling Scripts..."
echo " "
echo " "
cc Harley.c -o Harley
cd script
cc Password_Generator.c -o 1
cc Possible_combination_generator.c -o 2
echo " "
echo " "
echo "Finishing the installation............."
echo " "
echo " "
figlet -f small DONE!
echo "Installation Succesful [DONE!]"
echo " "
echo " "
