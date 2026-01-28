# Sysmon
#### Video Demo: https://youtu.be/xKauQzyXPyM
#### Description: 
This is a simple terminal-based system monitoring application. To run the app, download code files attached here and/or just run the exe file.

App opens up terminal and shows up your current CPU, RAM, disk storage load and uptime of your PC. For UI I added load percent for each system part and progress bar to show current workload. I used python with rich and psutil libraries and also some additional features used such importing like time and datetime. 

I cut my app into diffrent .py files to make it more organised. monitor.py is used to gather some information about PC (using psutils) to display it afterwards into tables. ui.py is responsible for UI design. I used rich to give it some style and put it beautifully into tables and progress bars. utils.py is used to store some additional utilities. In this case i used it for byte conversion into more bigger and readable chunks of memory (KB, MB, GB, TB). requirements.txt is of course to know which additional libraries are used in project. Finally, everything is gathered up in main.py to give it a finished look.

I was always interested into hardware power. I was frequently looking up into different stats in task manager. Happy that i could implement such thing by myself as before CS50x I thought I could not achieve this.

P.S. there is also fully functional .exe file in dist folder to run the programm.