# Config Nginx with web_static

$config = "/usr/bin/env printf %s 'server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.html index.htm;
    add_header X-Served-By ${hostname};

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /usr/share/nginx/html;
        internal;
    }

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
}' > /etc/nginx/sites-available/default"

exec { 'update_ppa':
  command  => 'sudo apt-get update',
  provider => shell,
}

package { 'Install nginx':
  ensure   => installed,
  name     => 'nginx',
  provider => apt,
  require  => Exec['update_ppa'],
}

file { '/data/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/shared/':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => 'Test HTML file Airbnb_v2'
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  force  => yes,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

exec { 'printf':
  command => $config,
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
