import face_recognition.api as face_recognition
import cv2, pickle, os, csv, stat
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib as mpl
from imutils import face_utils
import pymysql

import dlib
# from skimage.feature import hog
# from skimage import data, feature, exposure
# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

def dbConnection():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="root", database="042-attendence")
        return connection
    except:
        print("Something went wrong in database Connection")


def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")
def mark_your_attendance(username,filename_secure):
    username=username
    filename_secure=filename_secure
   
    imagefile="static/uploadimage/"+username+"/"+filename_secure
    print(imagefile)
    
    
    mpl.rcParams['toolbar'] = 'None'
    STORAGE_PATH = "storage"

    try:
        with open( os.path.join(STORAGE_PATH, "known_face_ids.pickle"),"rb") as fp:
            known_face_ids = pickle.load(fp)
        with open( os.path.join(STORAGE_PATH, "known_face_encodings.pickle"),"rb") as fp:
            known_face_encodings = pickle.load(fp)
        # known_face_ids = np.load("known_face_ids.npy")
        # known_face_encodings = np.load("known_face_encodings.npy")
    except:
        known_face_encodings = []
        known_face_ids = []


    # CSV_PATH = "/home/harsh/Backup/face-recognition/data/attendance.csv"
    # CSV_PATH = "static/data/attendance.csv"


    

    name = "Unknown"
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    sanity_count = 0
    unknown_count = 0
    marked = True
    
    try:
        # video_capture = cv2.VideoCapture(0+ cv2.CAP_DSHOW)
        # ret, frame = video_capture.read()
        frame = cv2.imread(imagefile)
    
        # plot = plt.subplot(1,1,1)
        # plt.title("Detecting Face")
        # plt.axis('off')
        # im1 = plot.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        studentname=''
        while sanity_count < 12:
            # Grab a single frame of video
            # ret, frame = video_capture.read()
            # print("FRAME READ WORKS")
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    
            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]
    
            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                
                # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
                # detect faces in the grayscale image
                # rects = detector(gray, 0)
                
                # hog_image_rescaled=frame
                # for (i, rect) in enumerate(rects):
            
                #     # imageHOG = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                #     # fd, hog_image = hog(imageHOG, orientations = 8, pixels_per_cell = (16,16), 
                #     #             cells_per_block = (1,1), visualize = True, channel_axis = True)
                #     # hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range = (0,10))
                    
                #     # determine the facial landmarks for the face region, then
                #     # convert the facial landmark (x, y)-coordinates to a NumPy
                #     # array
                #     shape = predictor(gray, rect)
                #     shape = face_utils.shape_to_np(shape)
                
                #     # loop over the (x, y)-coordinates for the facial landmarks
                #     # and draw them on the image
                #     for (x, y) in shape:
                #         cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
                
                # show the output image with the face detections + facial landmarks
              
                
                face_locations = face_recognition.face_locations(frame)
                face_encodings = face_recognition.face_encodings(frame, face_locations)

                print()
                print("printing after face recognition")
                print()
    
                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance = 0.35)
                    name = "Unknown"
    
                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_ids[first_match_index]
    
                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    # print(face_distances)
                    try:
                        best_match_index = np.argmin(face_distances)
                        marked = True
                        print("Students have been marked")
                    except:
                        print("No students have been marked")
                        # video_capture.release()
                        # cv2.destroyAllWindows()
                        marked = False
                        return marked
                    if matches[best_match_index]:
                        name = known_face_ids[best_match_index]
    
                    face_names.append(name)
            
            
            if(name == "Unknown"):
                unknown_count += 1
            else:
                unknown_count = 0
    
            if(unknown_count == 30):
                # video_capture.release()
                # cv2.destroyAllWindows()
                print("You haven't been registered")
                marked = False
                unknown_count = 0
                break
    
            process_this_frame = not process_this_frame
    
    
            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
    
                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    
                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.7, (255, 255, 255), 1)
    
    
            # print("BEFORE SHOWING")
            # Display the resulting image
            cv2.imshow('Video', frame)
            #cv2.imshow("Output", image)
            # cv2.imshow("hog_image", hog_image_rescaled)
            if cv2.waitKey(20) == 27:
                break
    
            # plt.ion()
            # im1.set_data(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            # plt.pause(0.001)
            # # as opencv loads in BGR format by default, we want to show it in RGB.
            # plt.show()
    
            # print("AFTER SHOWING")
            # Hit 'q' on the keyboard to quit!
            if(sanity_count == 0):
                prev_name = name
                sanity_count += 1
    
            elif(sanity_count < 10):
                if(prev_name == name and name != "Unknown"):
                    sanity_count += 1
                    prev_name = name
                else:
                    sanity_count = 0
    
            elif(sanity_count == 10):
                # print("Face registered")
                # video_capture.release()
                # cv2.destroyAllWindows()
                sanity_count = 0
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                date = dt_string.split(" ")[0]
                time = dt_string.split(" ")[1]
                studentname=str(name)#+" at "+str(date)
                #writer.writerow([name, date, time])
                # print(name + date + time)
                break
    
        # Release handle to the webcam
    
    
        # video_capture.release()
        cv2.destroyAllWindows()
        studentname = face_names[0]
        dt = date+" "+time
        print("printing face_names")
        print(studentname)
        print(marked)
        return marked,studentname,dt
    except:
        return False,"",""


def mark_your_attendance_singlepic(date,filename_secure):

    mpl.rcParams['toolbar'] = 'None'
    STORAGE_PATH = "storage"

    try:
        with open( os.path.join(STORAGE_PATH, "known_face_ids.pickle"),"rb") as fp:
            known_face_ids = pickle.load(fp)
        with open( os.path.join(STORAGE_PATH, "known_face_encodings.pickle"),"rb") as fp:
            known_face_encodings = pickle.load(fp)
        # known_face_ids = np.load("known_face_ids.npy")
        # known_face_encodings = np.load("known_face_encodings.npy")
    except:
        known_face_encodings = []
        known_face_ids = []


    # CSV_PATH = "/home/harsh/Backup/face-recognition/data/attendance.csv"
    CSV_PATH = "static/data/attendance.csv"


    if(os.path.exists(CSV_PATH)):
        csv_file = open(CSV_PATH, "a+")
        writer = csv.writer(csv_file)

    else:
        os.mknod(CSV_PATH)
        csv_file = open(CSV_PATH, "w+")
        writer = csv.writer(csv_file)
        writer.writerow(["Student ID", "Date", "Time of Entry"])

    name = "Unknown"
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    sanity_count = 0
    unknown_count = 0
    marked = True
    
    filepath="static/uploadimage/"+date+"/"+filename_secure
    print(filepath)
    
    try:
       
    
        # plot = plt.subplot(1,1,1)
        # plt.title("Detecting Face")
        # plt.axis('off')
        
        studentname=''
        while True:
           
            # Grab a single frame of video
            frame = cv2.imread(filepath)
            # print("FRAME READ WORKS")
            # Resize frame of video to 1/4 size for faster face recognition processing
            # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25, interpolation = cv2.INTER_CUBIC)
            small_frame = np.ascontiguousarray(frame[:, :, ::-1])
    
            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            # rgb_small_frame = small_frame[:, :, ::-1]
            rgb_small_frame = small_frame[:, :, ::-1]
            
            # Only process every other frame of video to save time
            if process_this_frame:
               
                # Find all the faces and face encodings in the current frame of video
                
                # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
                # # detect faces in the grayscale image
                # rects = detector(gray, 0)
                
                # hog_image_rescaled=frame
                # for (i, rect) in enumerate(rects):
            
                   
                #     # determine the facial landmarks for the face region, then
                #     # convert the facial landmark (x, y)-coordinates to a NumPy
                #     # array
                #     shape = predictor(gray, rect)
                #     shape = face_utils.shape_to_np(shape)
                
                #     # loop over the (x, y)-coordinates for the facial landmarks
                #     # and draw them on the image
                #     for (x, y) in shape:
                #         cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
                
                # show the output image with the face detections + facial landmarks
              
                
                
                face_locations = face_recognition.face_locations(frame)
                face_encodings = face_recognition.face_encodings(frame, face_locations)
    
                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance = 0.35)
                    name = "Unknown"
    
                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_ids[first_match_index]
    
                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    # print(face_distances)
                    try:
                        best_match_index = np.argmin(face_distances)
                    except:
                        # print("No students have been marked")
                       
                        marked = False
                        return marked
                    if matches[best_match_index]:
                        name = known_face_ids[best_match_index]
    
                    face_names.append(name)
    
            if(name == "Unknown"):
                unknown_count += 1
            else:
                unknown_count = 0
    
            if(unknown_count == 600):
                # video_capture.release()
                # cv2.destroyAllWindows()
                # print("You haven't been registered")
                marked = False
                unknown_count = 0
                break
    
            process_this_frame = not process_this_frame
    
    
            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
    
                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    
                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.7, (255, 255, 255), 1)
    
    
            # print("BEFORE sHOWING")
            # Display the resulting image
            imS = cv2.resize(frame, (960, 540))
            cv2.imshow('Video', imS)
            #cv2.imshow("Output", image)
            
            if cv2.waitKey(20) == 27:
                break
    
            # plt.ion()
          
            
          
            # plt.pause(0.001)
            # as opencv loads in BGR format by default, we want to show it in RGB.
            # plt.show()
    
            # print("AFTER SHOWING")
            # Hit 'q' on the keyboard to quit!
            if(sanity_count == 0):
                prev_name = name
                sanity_count += 1
    
            elif(sanity_count < 60):
                if(prev_name == name and name != "Unknown"):
                    sanity_count += 1
                    prev_name = name
                else:
                    sanity_count = 0
    
            elif(sanity_count == 60):
                # print("Face registered")
                # video_capture.release()
                # cv2.destroyAllWindows()
                sanity_count = 0
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                date = dt_string.split(" ")[0]
                time = dt_string.split(" ")[1]
                studentname=str(name)+" at "+str(date)
                print(studentname)
                writer.writerow([name, date, time])
                # print(name + date + time)
                break
    
        # Release handle to the webcam
    
        # plt.close()
        
        cv2.destroyAllWindows()
        print()
        print("face_names")
        print(face_names)
        print()
    
        return marked,face_names
    except Exception as e:
        print(e)
        return False,""
    


# username = "101"
# filename_secure = "static/uploadimage/admin/101_7.jpg"

# print(mark_your_attendance(username,filename_secure))
