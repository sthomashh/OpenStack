<h2>Python script that installs OpenStack Essex via puppet</h2>

Python script that installs OpenStack Essex all in one with puppet-modules from puppetlabs.com.  
Unlike the installation of DevStack this is a complete installation of OpenStack with everything in the right place. 
This installation of OpenStack Essex version is done via puppet. This script will do all the stuff for you. 
You will be asked for some network related stuff during installation. With this informations the script will 
create a puppet manifest and starts the installation process. 
After installation has been successfull, you can open the openStack Dashbord with http://your_public_ip/syspanel.


All you have to do is to start the script with 

>>> python installOpenStack.py

and follow the instructions...

