from os import makedirs
import random

class Expression:
    
    def __init__(self):
        self.noOfVariables=0
        self.expression=[]
        self.maxFlips=0
        self.maxTries=0
        
        
    def setMaxFlips(self,value):
        self.maxFlips=value
    
    def setMaxTries(self,value):
        self.maxTries=value
        
    def getMaxFlips(self):
        return self.maxFlips
    
    def getMaxTries(self):
        return self.maxTries
        
        
    def getExpression(self):
        return self.expression
        
    def setNoOfVariables(self,value):
        self.noOfVariables=value
        
    def getNoOfVariables(self)-> int:
        return self.noOfVariables
    
    def stringToExpressionInputConveter(self,expression: list):
        closure=[]
        for item in expression:
            item=item.strip('\n')
            if item:
                val=int(item)
                if val==0:
                  break
                closure.append(val)
        self.expression.append(closure)


def generateRandomTruthAssignment(noOfVariables: int):
    l = random.choices([True, False], k=noOfVariables)
    return l

def checkSatisfiability(expression:Expression,values: list)-> bool:

    for closure in expression.getExpression():
        passed=False
        for literal in closure:
            if (literal>0 and values[abs(literal)-1]) or (literal<0 and not(values[abs(literal)-1])):
                passed=True
                break
        if not passed:
            return False
    return True  

def noOfMakesAndBreakeByFlip(variable:int,expression:Expression,valueSet: list):
    makes=0
    breaks=0
    
    for closure in expression.getExpression():
        dependOnFlipingVariable = True
        valueOfliteral=0
        for literal in closure:
            if (literal>0 and valueSet[abs(literal)-1] and abs(literal)!=variable) or (literal<0 and not(valueSet[abs(literal)-1]) and abs(literal)!=variable):
                dependOnFlipingVariable=False
                break
            elif abs(literal)==variable:
                valueOfliteral=literal
                
        if dependOnFlipingVariable:
            if (valueOfliteral>0 and valueSet[abs(valueOfliteral)-1]) or (literal<0 and not(valueSet[abs(valueOfliteral)-1])):
                breaks=breaks+1
            else:
                makes=makes+1
                
    return (makes,breaks)   


def maxDiff(diff: list)-> int:
    max=len(diff)-1
    for i in range(len(diff)-1):
        if diff[i]>diff[max]:
            max=i
    return max
        
        
def gsatAlgorithm(expression:Expression):
    for tryNo in range(expression.getMaxTries()):
        randomlyGeneratedValues=generateRandomTruthAssignment(expression.getNoOfVariables())
        for flip in range(expression.getMaxFlips()):
            
            if checkSatisfiability(expression,randomlyGeneratedValues):
                return randomlyGeneratedValues
            
            diffs=[None] * expression.getNoOfVariables()
            
            for variable in range(expression.getNoOfVariables()):
                makes,breaks=noOfMakesAndBreakeByFlip(variable+1,expression,randomlyGeneratedValues)
                diffs[variable]=makes-breaks
                
            max=maxDiff(diffs)
            randomlyGeneratedValues[max]=not(randomlyGeneratedValues[max])
        
    return []