#!/usr/bin/python

import httplib
import httplib2
import os
import random
import sys
import time
import ntpath
import upload_video

from apiclient.errors import HttpError
from upload_video import initialize_upload
from upload_video import get_authenticated_service
from oauth2client.tools import argparser, run_flow

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage





path = 'F:/TEMP_C/'

print("Starting YouTube upload from TEMP_C..")

count = 0
while (count < 1):
	for file in os.listdir(path):
			if file.endswith(".mp4"):
				fullName=path + file
				#print fullName
				print file
				print("Searching in TEMP_C...")
				print "File exists and is readable"
				
				title =file
				description = ("SUBSCRIBE: http://bit.ly/Oqg3iE\n\nThe Atlantic Coast Conference (ACC) is a collegiate athletic conference in the United States in which its fifteen member universities compete in the National Collegiate Athletic Association (NCAA's) Division I, with its football teams competing in the Football Bowl Subdivision (FBS), the highest levels for athletic competition in US-based collegiate sports. The ACC sponsors competition in twenty-five sports with many of its member institutions' athletic programs held in high regard nationally. ACC teams and athletes have claimed dozens of national championships in multiple sports throughout the conference's history. Generally, the ACC's top athletes and teams in any particular sport in a given year are considered to be among the top collegiate competitors in the nation. The ACC is considered to be one of the six collegiate power conferences, all of which enjoy extensive media coverage and automatic qualifying for their football champion into the Bowl Championship Series (BCS). With the advent of the College Football Playoff in 2014, the ACC will be one of five conferences with a contractual tie-in to an \"access bowl\", the successors to the BCS. \n\nFounded in 1953 in Greensboro, North Carolina, by seven universities located in the South Atlantic States, the conference added additional members in late 1953, 1979, 1991, 2004, and 2013. The 2004 and 2013 additions extended the conference's footprint into the Northeast and Midwest. The most recent expansion in 2013 saw the additions of the University of Notre Dame, the University of Pittsburgh, and Syracuse University. In 2012, the University of Maryland's Board of Regents voted to withdraw from the ACC to join the Big Ten Conference. On November 28, 2012, the ACC's Council of Presidents voted unanimously to invite the University of Louisville as a full member, replacing Maryland.\n\nConnect with the ACCDigitalNetwork Online:\nVisit the ACC WEBSITE: http://theacc.com\nFollow the ACCDN on Twitter: https://twitter.com/theACCDN\nFollow the ACCDN on Instagram: http://instagram.com/theACCDN\n\nhttp://www.youtube.com/user/ACCDigitalNetwork")
				keywords = ["ACCDigitalNetwork, ACC Digital Network, ACCDN, ACC, College Sports, Division I, NCAA, Atlantic Coast Conference, athletics, competition, Ruby Tuesday"]
				category="17"
				privacyStatus="private"
				options=fullName, title, description, keywords, category, privacyStatus
				args = argparser.parse_args()
				youtube = get_authenticated_service(args)
				try:
					initialize_upload(youtube, options)
				except HttpError, e:
					print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
				os.remove(fullName)
				#fullName = ""
				print "Complete"
			else:
				print "Either file is missing or is not readable"
	
	
print "Stopped"