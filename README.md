<h2>Python script that installs OpenStack Essex via puppet</h2>

Python-Script that installs OpenStack Essex all in one with Puppet-Modules from puppetlabs.com.  
Unlike the installation of DevStack this is a complete installation of OpenStack with everything in the right place. 
This installation of OpenStack essex version is done via puppet. Tis script will do all the stuff for you. 
You will be asked for some network related stuff during installation. With this informations the script will 
create a puppet manifest and starts the installation process. 
After installation has been successfull, you can open the openStack Dashbord with http://your_public_ip/syspanel.


All you have to do ist to start the script with 

>>> python installOpenStack.py

and follow the instructions...



https://github.com/sthomashh/OpenStack.git
oder
git@github.com:sthomashh/OpenStack.git


# Create a new repository on the command line:
touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:sthomashh/OpenStack.git
git push -u origin master



# Push an existing repository from the command line:
git remote add origin git@github.com:sthomashh/OpenStack.git
git push -u origin master
