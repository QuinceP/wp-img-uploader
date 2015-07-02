from datetime import datetime
import xmlrpclib
import PIL
import os
from PIL import Image

###################################
#       EDIT FOR YOUR BLOG        #                                                                         
###################################
#enter the url of your site here. for example, "http://www.example.com/" (include the slash at the end)
site = "http://www.example.com/"
#
#your wordpress username
wp_username = "USERNAME"
#
#your Wordpress password
wp_password = "PASSWORD"
#
#this is the folder you wish to upload. for example, /site/cats/browncats/
folder = "/site/cats/browncats/"
#
#enter post details here
title = "Post Title"
categories = ["text"]
tags = ["article", "blog"]
##################################
#You shouldn't have to edit anything past this point.


#change the directory to the folder
os.chdir(folder)

#this is to access the Wordpress xmlrpc API. no need to edit anything here.
wp_url = site +"xmlrpc.php"

#leave this blank
wp_blogid = ""

status_draft = 0
status_published = 1

#the server
server = xmlrpclib.ServerProxy(wp_url)

#for every file in the folder,
for i in os.listdir(os.getcwd()):
    if i.endswith(".jpg"): #if the file is a jpg image, then
        img = os.path.basename(os.getcwd()) + "/" + i #get the full path of the image
        im = Image.open(i)  #open the image
        width, height = im.size #get the dimensions of the image for html formatting purposes
        
        #embeds the image in the post
        content = "<a href=\"" + site + img + "\"><img class=\"alignnone size-full wp-image-30\" src=\"" + site + img + "\" width=\"" + str(width) + "\"height=\"" + str(height) + "\" /></a>"
        
        #get the current date and time for the post
        date_created = xmlrpclib.DateTime(datetime.strptime(datetime.today().strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M"))
        
        #data for the post using the fields edited
        data = {'title': title, 'description': content, 'dateCreated': date_created, 'categories': categories, 'mt_keywords': tags, 'custom_fields': [{'value': site + img, 'key': 'thumb'}]}
        
        #publish the post
        post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)
        continue
    else: #not a jpg image, move to the next file.
        continue

