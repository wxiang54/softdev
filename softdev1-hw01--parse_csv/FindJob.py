import decimal
import random

jobfile = open('occupations.csv', 'r')

jobsDict = {}
for line in jobfile.readlines()[1:-1]: #skip first and last line
            splitIndex = line.rfind(",") #find last occurance of comma
            jobsDict[line[:splitIndex].strip('"')] = float(line[splitIndex+1:]) #split line accordingly


def randJob( jobsDict ):
            randnum = decimal.Decimal(random.randrange(1000))/10
            curr = 0
            for occupation, chance in jobsDict.items():
                        curr += chance
                        if randnum < curr:
                                    return occupation
            return "Unemployed"


if __name__ == '__main__': #creds to PChan for explaining how this works
            jobCounts = {job:0 for job in jobsDict} 
            for i in range(100):
                        jobCounts[randJob(jobsDict)] += 1

            #FORMAT: JOB | THEORETICAL CHANCE | EXPERIMENTAL CHANCE
            for job in jobsDict:
                        print("%s:\t%f\t%d" % (job, jobsDict[job], jobCounts[job]))
                        
