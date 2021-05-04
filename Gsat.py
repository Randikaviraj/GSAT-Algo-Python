from GsatFunc import Expression,gsatAlgorithm
import sys
import time




if __name__ =="__main__":
    try:
        
        expression=Expression()
        expression.setMaxFlips(int(sys.argv[2]))
        expression.setMaxTries(int(sys.argv[3]))
        
        with open(sys.argv[1],"r") as file:
            print(f"{sys.argv[1]} Reading..")
            line=file.readline()
            noOfVariables=line.split(" ")[2]
            expression.setNoOfVariables(int(noOfVariables))
            line=file.readline()
            
            while line:
                list=line.split(" ")
                expression.stringToExpressionInputConveter(list)
                line=file.readline()
                
                
            print('Algorithm Started::')
            seconds = time.time()
            l=gsatAlgorithm(expression)
            seconds = seconds-time.time()
            if len(l)==0:
                print('No Satified Answers found to SAT problem ')
            else:
                print('Answer to SAT problem :'+str(l))
            print('Finished::')
            print('Running Time in second'+str(seconds))
            
    except Exception as e:
        print(e)
        print('Invalid no of Arguments :: python Dpll.py <filename> <Max no of flips> <Max no of tries>')