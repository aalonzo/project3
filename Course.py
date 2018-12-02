class Course:
        def __init__(self,n,t,gp):
            self.name=n
            self.timecode=t
            self.gradepoints=gp
        def getTime():
            time=""
            timeraw=str(timecode)
            if timeraw[0]==1:
                time+="Monday "
            elif timeraw[0]==2:
                time+="Tuesday "
            elif timeraw[0]==3:
                time+="Wednesday "
            elif timeraw[0]==4:
                time+="Thursday "
            elif timeraw[0]==5:
                time+="Friday "
                
            timetemp1=timeraw[1:5]
            if timetemp1<1200:
                time=time+timetemp1[1:3]+":"+timetemp1[3:5]+" AM "
            elif timetemp1<1300:
                time=time+timetemp1[1:3]+":"+timetemp1[3:5]+" PM "
            else:
                timeconv=str(int(timetemp1[1:3])-12)
                time=time+timeconv+":"+timetemp1[3:5]+" PM "
                
            time+="to " 
        
            timetemp2=timeraw[5:9]
            if timetemp2<1200:
                time=time+timetemp2[5:7]+":"+timetemp2[7:9]+" AM"
            elif timetemp2<1300:
                time=time+timetemp2[5:7]+":"+timetemp2[7:9]+" PM"
            else:
                timeconv=str(int(timetemp2[5:7])-12)
                time=time+timeconv+":"+timetemp2[7:9]+" PM"
            
            return time
            
            
                
                
