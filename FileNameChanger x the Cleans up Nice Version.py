import os
import time
from dateutil.relativedelta import relativedelta
from datetime import datetime
from calendar import month_name, month_abbr


# The "r" notes that file path should be read in. The rootdir is the path to where you start searching for files
rootdir = (r"D:\\") 
# Scan the path for all the folders grab their names and pt them in the subfolder list
subfolders = [f.name for f in os.scandir(rootdir) if f.is_dir()] 

monthList = [] # List To hold names for months
folderFiles = [] # List To hold the whole paths of the files 
theDates = [] # List To hold the "Modified by dates (The dates the video was shot)"
# months = {m.lower() for m in month_name[1:] }
# Takes month names and month abbreviations from calendar librarys and zips them together into one list
for mon, abr in zip(month_name[1:], month_abbr[1:]):
    monthList.append(mon)
    monthList.append(abr)

for i in subfolders:
    for j in monthList:
        #If the name of the folders contains a month name or month abbreviation
        if(j in i): 
            # Create a path to the subfolder by joining it's name with the root directory, add that path to the "folderFiles" list
            folderFiles.append(os.path.join(rootdir, i)) 
            break


for subdir, dirs, folderFiles in os.walk(rootdir):# for the all the folders and subfolders in the given directory
    for file in folderFiles: # for every file path in the folder files list

        print("Huncho "+os.path.basename(file)) #
        if file.endswith(".MTS"): # If the file extensiton is ".MTS"
            # Gets the the path of file,then, gets the modified by date of the file in seconds since "epoch", converts the seconds into a string in local time format
            my_string = " %s" % time.ctime(os.path.getmtime(os.path.join(subdir, file))) 
            
            #Turns the string into a datetime object using the specific format code for the string 
            my_date = datetime.strptime( my_string, " %a %b  %d %H:%M:%S %Y") 
            #Adds a year and subtracts a day from the dateime object to account for the camera  being on the wrong date settings
            my_date = my_date + relativedelta(years=+1)
            my_date = my_date + relativedelta(days=-1)

            #Turns the day back into a string in the month/day/year format; option uncommented  if you want to rename files at the end
            #oldFiles = my_date.strftime('%m%d%Y') 
            # // Format so you can put it into a txt file
            #theDates.append(my_date.strftime('%A %B %m/%d/%Y'))
            theDates.append(my_date.strftime('%A %B %m/%d/%Y')+"  "+file)#  Turns the date into a string in format "Friday May 05 28 2018"  
            #os.rename(os.path.join(subdir, file),os.path.join(subdir,(oldFiles+ file))) #Optional renaming of files to the date forma 05 28 2018


MyFile = open('dateList.txt', 'w')  # writes a the list of dates to a txt files
for element in theDates:
 MyFile.write(element)
 MyFile.write('\n')
MyFile.close()
