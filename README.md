# Udacity Full Stack Web Developer Nanodegree

## Item-Catalog Project

#### Objective
Create a restaurant menu app where users can add, edit, and delete restaurants and menu items in the restaurants.

#### Directions
1. Download [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to install and manage your virtual machine.

2. Install VirtualBox and Vagrant

3. Download and unzip the `Item-Catalog_Project.zip`

4. Place the `Item-Catalog_Project` folder in your Vagrant directory

5. Launch Vagrant by using the `vagrant up` command

6. Login to Vagrant by using the `vagrant ssh` command

7. Change directory to `vagrant`

8. Type `Python database_setup.py` to initialize the database

9. Type `Python menus.py` to populate the database with some initial data

10. Type `dos2unix project.py` to convert this file to UNIX format

11. Now type `Python project.py` to execute the application file

12. Open the browser and go to http://localhost:5000

### JSON endpoints

Enter `/restaurants/JSON` on your browser to return JSON of all restaurants

Enter `/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON` on your browser to return JSON of specific menu item

Enter `/restaurants/<int:restaurant_id>/menu/JSON` on your browser to return JSON of menu
