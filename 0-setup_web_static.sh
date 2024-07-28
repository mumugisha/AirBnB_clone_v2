#!/usr/bin/env bash
<<<<<<< HEAD
#Bash script that sets up your web servers for the deployment of web_static

apt-get update
=======
# Bash script that sets up your web servers for the 
# deployment of web_static

set -e

# Update package index and install nginx
echo "Updating package index..."
apt-get update
echo "Installing nginx..."
apt-get install -y nginx

# Create necessary directories
echo "Creating directories..."
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/

# Create a test index.html file
echo "Creating test index.html..."
cat << EOF > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School<br>
  </body>
</html>
EOF

# Create a symbolic link to the test release
echo "Creating symbolic link..."
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of the data directory
echo "Changing ownership of /data/..."
chown -R ubuntu:ubuntu /data/

# Update the nginx configuration to serve content from the symbolic link
echo "Updating nginx configuration..."
sed -i '/^\tlocation \/ {./i \\tlocation \/hnbn_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart nginx to apply the changes
echo "Restarting nginx..."
service nginx restart

echo "Setup complete."
>>>>>>> df9c719a454f1a75c542c900647b1a3ae44d4e91
