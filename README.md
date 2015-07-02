# wp-img-uploader
### by Christen Ward christenward@christenward.com


CONTENTS OF THIS FILE
---------------------
   
 1. Introduction
 2. Requirements
 3. Recommended Wordpress Plugins
 4. Configuration
 
INTRODUCTION
------------
Wordpress Image Uploader bulk uploads each jpeg picture in a directory to 
your Wordpress blog, and creates it as a separate post using the Worpress
API. Works great for photography blogs or any type of blog that requires 
quick uploading of a single directory without having to blog each one manually.

REQUIREMENTS
------------
This script requires the following:
 * Python 2.7 (https://www.python.org/download/releases/2.7/)
 * Python Imaging Library - (http://www.pythonware.com/products/pil/)
 * A Wordpress blog, of course.
 * Wordpress xmlrpc API. Should be on by deafult in most Wordpress installs.
 
RECOMMENDED PLUGINS FOR WORDPRESS
-------------------
 * Auto Thumbnailer - Automatically create thumbnails for posts when images are uploaded and the 
   post is saved. (https://wordpress.org/plugins/auto-thumbnailer/)
   

CONFIGURATION
-------------
 * Edit the fields in wp-image-uploader.py, under the heading EDIT FOR YOUR BLOG:
   * site - this is the address of your wordpress site. For example, http://www.heyahh.me.
   * wp_username - your Wordpress blog username.
   * wp_password - your Wordpress blog password.
   * folder - the folder of images on your server of which you choose to upload. For example, /site/cats/browncats/
   * title - the title of your posts
   * categories - categories for your posts.
   * tags - tags for the posts.