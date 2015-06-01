ansible-scaleio
======================
ansible-scaleio is a way to manage ScaleIO through [Ansible](http://www.ansible.com/home "Ansible").

## Description

ansible-scaleio let's you do the following with ansible and scaleio:

- Install ScaleIO

- Configure the different roles:
  - mdm
  - sds
  - tb
  - lia
  - gateway (to be used for API gateway mainly)

- For the sds you can setup different type of storage.

## Installation

To install ansible-scaleio just clone the repo and see site.yml as a generic playbook. If you are using Vagrant you can actually use the Vagrantfile to launch an environment to play with.

## Usage Instructions

Customize the roles and playbooks to your environment, you can use this to either to install ScaleIO or just enable the different modules on the nodes.
```
  ansible-playbook -i hosts site.yml
```

## Future
- Enable the SDC client installation
- Add other roles
  - callhome
- Extend to do more special setup with cache
- Clean up the code


## Contribution
Create a fork of the project into your own reposity. Make all your necessary changes and create a pull request with a description on what was added or removed and details explaining the changes in lines of code. If approved, project owners will merge it.

Licensing
---------
The MIT License (MIT)
Copyright (c) [2015], [EMC Corporation)]
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.”


Support
-------
Please file bugs and issues at the Github issues page. For more general discussions you can contact the EMC Code team at <a href="https://groups.google.com/forum/#!forum/emccode-users">Google Groups</a> or tagged with **EMC** on <a href="https://stackoverflow.com">Stackoverflow.com</a>. The code and documentation are released with no warranties or SLAs and are intended to be supported through a community driven process.
===============
