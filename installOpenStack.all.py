#!/usr/bin/python
#
# @author:    Sven Thomas, sthomas@gwdg.de
#             Installation script for OpenStack single node installation via puppet
#             with OpenStack puppet modules from puppetlabs.com 
#             start installation with command: "./installOpenStack.py"
#             preconditions: 2 Network-Interfaces (maybe virtual); blank installation of ubuntu precise 12.04 LTS
#

import re
import os
import sys

debug = 0
#####################################################################################

def replaceit(message,defaultval,content):   
    prompt = raw_input(message+" (default "+defaultval+")\n\n:-> ")    
    sys.stdout.flush()    
    if prompt == "":
        prompt = defaultval
    print 'Your input: '+prompt+"\n\n"
    return re.sub("'"+defaultval+"'","'"+prompt+"'",content)





# get git, puppet, rake and checkout openstack-repo:
stack = list()
if debug == 1:
    debugflag = '-s '
else:
    debugflag = ''
stack.append('apt-get -y '+debugflag+'update')
stack.append('apt-get -y '+debugflag+'install puppet git rake')
stack.append('git clone git://github.com/puppetlabs/puppetlabs-openstack /etc/puppet/modules/openstack')
stack.append('cd /etc/puppet/modules/openstack')
stack.append('git checkout essex')
for cmd in stack:
    print os.system(cmd)


# wechsele standort 
os.chdir('/etc/puppet/modules/openstack/examples/')
filename = 'site.pp'
f = open(filename)
fileasstring = ""
try:
    for line in f:
        fileasstring += line
finally:
    f.close()



# fixed network
message = 'Please enter the fixed network-range'
defaultval = '10.0.0.0/24'
string = fileasstring
fileasstring = replaceit(message,defaultval,string)


# floating network
message = 'Please enter the floating network-range'
defaultval = '192.168.101.64/28'
string = fileasstring
fileasstring = replaceit(message,defaultval,string)


# networkdevice 1
message = 'Please enter first network interface (public interface with already allocated ipaddress)'
defaultval = 'eth0'
string = fileasstring
fileasstring = replaceit(message,defaultval,string)


# networkdevice 2
message = 'Please enter second network interface (private interface without allocated ipaddress; for vm-network)'
defaultval = 'eth1'
string = fileasstring
fileasstring = replaceit(message,defaultval,string)


# Libvirt Typ
message = 'Please enter virtualization infrastructure/emulator (kvm or qemu)'
defaultval = 'kvm'
string = fileasstring
fileasstring = replaceit(message,defaultval,string)


os.chdir('/etc/puppet/modules/openstack/examples/')
install_file_name = "myinstall.pp"
try:
    file = open(install_file_name, 'w')
    file.write(fileasstring)
finally:
    file.close()
    
print "File " + install_file_name + " successfully written"



stack = list()
stack.append('rake modules:clone')

if debug == 1:
    debugflag = '--noop '
else:
    debugflag = ''
    
stack.append('puppet apply --verbose '+debugflag + os.getcwd() + "/" + install_file_name+' --certname openstack_all')

for cmd in stack:
    print cmd+"\n"
    print os.system(cmd)



