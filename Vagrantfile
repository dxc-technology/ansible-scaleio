# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

scaleio_nodes = [{:hostname => "node0", :ip => "192.168.33.50"}, {:hostname => "node1", :ip => "192.168.33.51"}, {:hostname => "node2", :ip => "192.168.33.52"}]
# vagrant box
vagrantbox="centos_6.5"
# vagrant box url
vagrantboxurl="https://github.com/2creatives/vagrant-centos/releases/download/v6.5.3/centos65-x86_64-20140116.box"
# domain
domain = 'scaleio.local'



Vagrant.configure(2) do |config|
    scaleio_nodes.each do |node|
    config.vm.define node[:hostname] do |node_config|
      node_config.vm.box = "#{vagrantbox}"
      node_config.vm.box_url = "#{vagrantboxurl}"
      node_config.vm.host_name = "#{node[:hostname]}.#{domain}"
      node_config.vm.network "private_network", ip: "#{node[:ip]}", virtualbox__intnet: true
      node_config.vm.provision "shell", inline: 'mkdir /root/.ssh/ && chmod 0700 /root/.ssh/ && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA9ItmH73JMyCYAfI5MGq5484Fqq8Kdvo8tfQf3BbdQUcJ2ZQIOvk/NfC+7ClBChoo6TyJkcbNDcgc0j+wN349FgRP6BKCedAJlJLHehHWcT+sSaVj8gZjwxiqPMn/5DlNDWyc+1Fw6KhnwHe/3cm+VtJfAZX98xRzkcTvACmNkGxZX2kqdlAbOGLsS22HCEsquuZdwon/SO4a4glyx8jQYxAMiuE3LZsu4Sj/jxoKgWNgYOByGVEH5teTeUU6YuO0NeWTLZSwkfoOZZTyrJbkgyAtMoALZ+3ZD7eC4XZ3PPCbSRZY8uLE32yTMm8efp9eLB5KfrpM+u0udj4eeq1ZKw== sebasp@omnios" > /root/.ssh/authorized_keys  && chmod 644 /root/.ssh/authorized_keys && cat /root/.ssh/authorized_keys && echo "Removing useless bridge netfilters in /etc/sysctl.conf" && cp /etc/sysctl.conf /tmp/sysctl.conf && grep -v bridge /tmp/sysctl.conf > /etc/sysctl.conf && rm /tmp/sysctl.conf && cat  /etc/sysctl.conf && truncate -s 100GB /home/vagrant/scaleio1'
    end
  end
end
