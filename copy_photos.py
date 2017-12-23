from PIL import Image, ExifTags
from shutil import copyfile
import os, os.path
import datetime
import sys

#TODO Run script on scheduled times?
#TODO Check for the board in the pictures?
#TODO set rules for which minutes it should copy for

copy_from_directory = os.fsdecode('C:/Users/fredr/Dropbox/Camera Uploads') #Directory of pictures
copy_to_directory = os.fsdecode('C:/Users/fredr/PycharmProjects/lecture_photo/copied_files')
copies = 0

for file in os.listdir(copy_from_directory): #For all files in picture directory
    filename = os.fsdecode(file) #Get file name
    print('Checking file: ' + filename)

    try:
        if filename.endswith(".jpg"): #If .jpg
            current_file = os.path.join(copy_from_directory, filename)
            copy_to_folder_path = copy_from_directory + "/copied_files/"
            img = Image.open(current_file)
            exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
            try:
                date, time = exif['DateTimeOriginal'].split(' ', 1)  # Get date and time from exif data and split it
            except:
                print('No DateTimeOriginal.')

                try:
                    date, time = exif['DateTime'].split(' ', 1)
                except:
                    print('Cant find DateTime')
            pass

            year, month, day = date.split(':', 2)
            hour, minute, second = time.split(':', 2)
            h = hour

            if year == '2017':

                if month == '12' or month == '11' or month == '10':
                    s = datetime.datetime.strptime(year+month+day,"%Y%m%d")
                    weekday = s.strftime("%A")

                    if weekday != 'Saturday' and weekday != 'Sunday':

                        if (h=='08'  or h=='09' or h=='10'
                            or h=='11' or h=='13' or h=='14'
                            or h=='15' or h=='16'):

                            date_and_time = date.replace(':', '_') + '-' + time.replace(':', '_') + '.jpg'
                            print('copying file: ' + current_file)
                            new_file_name_and_path = os.path.join(copy_to_directory, date_and_time)
                            copyfile(current_file, new_file_name_and_path) # Copy the picture
                            copies += 1
                            print('Files copied: ' + str(copies))
                        else:
                            print('Wrong hour: ' + hour)
                            continue
                    else:
                        print('Wrong weekday: ' + weekday)
                        continue
                else:
                    print('Wrong month: ' + month)
                    continue
            else:
                print('Wrong year: ' + year)
                continue
        else:
            print('Wrong filetype.')
            continue

    except AttributeError:
        print('Strange picture..')
        pass

    except SystemExit:
        print('Exiting')
        sys.exit(0)
        pass

