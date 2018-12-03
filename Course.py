class Course:
        def __init__(self,n,t,gp):
            self.name=n
            self.timecode=t
            self.gradepoints=gp

        def getFullTime(self):
            time=""
            timeraw=str(self.timecode)
            if timeraw[0]=='1':
                time+="Monday "
            elif timeraw[0]=='2':
                time+="Tuesday "
            elif timeraw[0]=='3':
                time+="Wednesday "
            elif timeraw[0]=='4':
                time+="Thursday "
            elif timeraw[0]=='5':
                time+="Friday "

            timetemp1=timeraw[1:5]
            if int(timetemp1)<1200:
                time=time+timeraw[1:3]+":"+timeraw[3:5]+ " AM "
            elif int(timetemp1)<1300:
                time=time+timeraw[1:3]+":"+timeraw[3:5]+" PM "
            else:
                timeconv=str(int(timeraw[1:3])-12)
                time=time+timeconv+":"+timeraw[3:5]+" PM "

            time+= "to "
            
            timetemp2=timeraw[5:9]
            if int(timetemp2)<1200:
                time=time+timeraw[5:7]+":"+timeraw[7:9]+" AM"
            elif int(timetemp2)<1300:
                time=time+timeraw[5:7]+":"+timeraw[7:9]+" PM"
            else:
                timeconv=str(int(timeraw[5:7])-12)
                time=time+timeconv+":"+timeraw[7:9]+" PM"

            return time

        def changeGP(gp):
            self.gradepoints=gp
        
        def getStartTime():
            timeraw=str(self.timecode)
            return int(timeraw[1:5])
        
        def getEndTime()
            timeraw=str(self.timecode)
            return int(timeraw[5:9])
        
        def compareTimes(other):
            if other.getStartTime()==self.getStartTime():
                return False
            elif other.getStartTime()<=self.getStartTime() and other.getEndTime()>self.getStartTime():
                return False
            elif other.getStartTime()>=self.getStartTime() and other.getStartTime()<self.getEndTime():
                return False
            else:
                return True
