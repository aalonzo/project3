class Course:
        def __init__(self,n,t,gp):
            self.name=n
            self.timecode=t
            self.gradepoints=gp

        def getName(self):
            return self.name
        def getTimecode(self):
            return self.timecode
        def getGP(self):
            return self.gradepoints
        
        def getFullTime(self):
            time=""
            timeraw=str(self.timecode)
            if timeraw[0]=='1'or timeraw[1]=='1'or timeraw[2]=='1'or timeraw[3]=='1'or timeraw[4]=='1':
                time+="Monday "
            if timeraw[0]=='2'or timeraw[1]=='2'or timeraw[2]=='2'or timeraw[3]=='2'or timeraw[4]=='2':
                time+="Tuesday "
            if timeraw[0]=='3'or timeraw[1]=='3'or timeraw[2]=='3'or timeraw[3]=='3'or timeraw[4]=='3':
                time+="Wednesday "
            if timeraw[0]=='4'or timeraw[1]=='4'or timeraw[2]=='1'or timeraw[3]=='4'or timeraw[4]=='4':
                time+="Thursday "
            if timeraw[0]=='5'or timeraw[1]=='5'or timeraw[2]=='5'or timeraw[3]=='5'or timeraw[4]=='5':
                time+="Friday "

            timetemp1=timeraw[5:9]
            if int(timetemp1)<1200:
                morntemp1=(timeraw[5:7]).remove('0')
                time=time+morntemp1+":"+timeraw[7:9]+ " AM "
            elif int(timetemp1)<1300:
                time=time+timeraw[5:7]+":"+timeraw[7:9]+" PM "
            else:
                timeconv=str(int(timeraw[5:7])-12)
                time=time+timeconv+":"+timeraw[7:9]+" PM "

            time+= "to "
            
            timetemp2=timeraw[9:13]
            if int(timetemp2)<1200:
                morntemp2=(timeraw[9:11]).remove('0')
                time=time+morntemp2+":"+timeraw[11:13]+" AM"
            elif int(timetemp2)<1300: 
                time=time+timeraw[9:11]+":"+timeraw[11:13]+" PM"
            else:
                timeconv=str(int(timeraw[9:11])-12)
                time=time+timeconv+":"+timeraw[11:13]+" PM"

            return time
        
        def sameDays(self,other):
            timeraw1=str(other.getTimecode())
            timeraw2=str(self.timecode)
            daylist1=list(timeraw1[0:5])
            daylist2=list(timeraw2[0:5])
            for i in range(daylist1.count('0')):
                daylist1.remove('0')
            for j in range(daylist2.count('0')):
                daylist2.remove('0')
            for i in daylist1:
                for j in daylist2:
                    if i==j:
                        return True
            return False
                
        def getStartTime(self):
            timeraw=str(self.timecode)
            return int(timeraw[5:9])
        
        def getEndTime(self):
            timeraw=str(self.timecode)
            return int(timeraw[9:13])
        
        def checkConflicts(self,other):
            if self.sameDays(other):
                if other.getStartTime()==self.getStartTime():
                    return True
                elif other.getStartTime()<=self.getStartTime() and other.getEndTime()>self.getStartTime():
                    return True
                elif other.getStartTime()>=self.getStartTime() and other.getStartTime()<self.getEndTime():
                    return True
                elif other.getStartTime()==self.getEndTime():
                    return False
            return False
        
def createTimecode(days,start,end): #Enter days separated by comma, start and end in format "3:30pm" or similar
    timecode=""
    days=days.replace(" ","") #supposed to remove commas, spaces, and lowercase everything
    days=days.lower()
    daylist=days.split(',')
    if "monday" in daylist:
        timecode+="1"
    if "tuesday" in daylist:
        timecode+="2"
    if "wednesday" in daylist:
        timecode+="3"
    if "thursday" in daylist:
        timecode+="4"
    if "friday" in daylist:
        timecode+="5"
    if len(timecode)<5: #makes sure 5 characters in timecode represent days
        for i in range(5-len(timecode)):
            timecode+="0"
    
    start=start.replace(" ","") #supposed to remove spaces and lowercase everything
    start=start.lower() 
    if len(start)<6: #makes sure four characters in timecode represent start
        start="0"+start
    start.remove(':')
    time1=start[0:2]
    if start[-2:]=="pm":
        afttime1=int(start[0:2])
        if afttime1!=12:            
            afttime1+=12
        time1=str(afttime1)
    timecode+=time1+start[2:4]

    end=end.replace(" ","") #supposed to remove spaces and lowercase everything
    end=end.lower()
    if len(end)<6: #makes sure four characters in timecode represent end
        end="0"+end
    end.remove(':')
    time2=end[0:2]
    if end[-2:]=="pm":
        afttime2=int(end[0:2])
        if afttime2!=12:            
            afttime2+=12
        time2=str(afttime2)
    timecode+=time2+end[2:4]

    return int(timecode) #timecode should be in format dddddsssseeee as an int
