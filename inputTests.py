''' ----- USAGE explanation -----
    1. Write test inputs in testInputs.xml file
    2. Create class object
    3. Call function getAnswer()
    4. Answers will be logged in testAnswers.xml file
    
    Example:
    import InputTests from inputTests
    obj = InputTests()
    obj.getAnswer()
    
    Test case writing in xml file:
    In <root> tag write <test>'s with 2 attributes: {module} and {input}
    I.E. <test module="Reminder" input="Remind me at 6oclock to make homework"/>
'''

# xml DOCUMENTATION: 
# https://docs.python.org/2/library/xml.dom.minidom.html
# https://docs.python.org/2/library/xml.etree.elementtree.html
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree

import datetime
import traceback # for debugging

# import all modules available for testing
from reminder import Reminder

class InputTests():    
    def __init__(self):
        self.testFileInputs = 'testInputs.xml'
        self.testFileAnswers = 'testAnswers.xml'
        self.tests = []
        self.initTestList() # loads/prepare testInputs.xml       
    
    ''' <summary>preparing tests for analyses</summary>
        <return>None</return>'''
    def initTestList(self):
        try:
            xmldoc = minidom.parse(self.testFileInputs) # loads file content(str)
            itemList = xmldoc.getElementsByTagName('test') # filters tag <test>
            # tests are a list of tuples(module, input)
            for item in itemList:
                module = item.attributes['module'].value
                userInput = item.attributes['input'].value
                if module == None or userInput == None: # if syntax failure - skip
                    continue
                else: # parsed successfully, adding the test
                    self.tests.append((module, userInput))
        except:
            print("Error: parsing test inputs")
    
    ''' <summary>fixes indentation</summary>
        <return>str</return>'''
    def fixXmlString(self, rootElement): 
        # Used examples from documentation 
        rough_string = ElementTree.tostring(rootElement, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="   ")
    
    ''' <summary>parsing python list of tuples to xml</summary>
        <return>None</return>'''
    def logToFile(self):
        ''' Code fragments grabbed from tutorial: 
            https://pymotw.com/2/xml/etree/ElementTree/create.html '''
        # Creates root tag
        root = Element('root')
        # Adds comment
        comment = Comment('Test time: {}'.format(str(datetime.datetime.now())))
        root.append(comment)
        # Appends all test results
        for t in self.tests:
            # t is test of type tuple(module, input, answer)
            if t != None:
                testTag = SubElement(root, 'test')
                inputTag = SubElement(testTag, 'input')
                inputTag.text = t[1]
                answerTag = SubElement(testTag, 'answer')
                answerTag.text = t[2]
            
        file = open(self.testFileAnswers, 'w')
        file.write(self.fixXmlString(root))
        file.close()
    
    ''' <summary>Test starting function</summary>
        <return>str(message for user)</return>'''
    def getAnswer(self, userInput=None):        
        for i in range(len(self.tests)): # t is a tuple(module, input)
            try:
                # Creating selected module object
                moduleObj = eval(self.tests[i][0] + '()')
                # Getting module answer, given arg is input
                answer = moduleObj.getAnswer(self.tests[i][1])
                # Making new tuple: (module, user_input, answer)
                self.tests[i] = (self.tests[i][0], self.tests[i][1], answer)
            except:
                print('Test failed for:', str(self.tests[i]))
                traceback.print_exc()
                self.tests[i] = None
        # popping failed tests using decreasing for loop
        for i in range(len(self.tests) - 1, -1, -1):
            try:
                if self.tests[i] == None:
                    self.tests.pop(i)
            except:
                print("Error: cannot pop %d" % i)
                
        self.logToFile() # Writes to answer file
        return 'Test successfully saved at: ```' + self.testFileAnswers + '```'

# Console test version (on discord write !test)
if __name__ == '__main__':
    obj = InputTests()
    obj.getAnswer()
