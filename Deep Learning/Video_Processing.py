#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:41:19 2019

@author: kazzastic
"""

import cv2

def show_video():
    cap = cv2.VideoCapture(0)
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    while True:
        ret,frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('This is me', gray)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def video_save():
    cap = cv2.VideoCapture(0)
    
    #width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    #height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('Kazim.avi',fourcc, 20.0, (640,480))
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # write the flipped frame
            out.write(frame)
    
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    
    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    
video_save()