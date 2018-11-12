''' To run tests use class InputTests function: getAnswer() '''

from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree
import datetime
import traceback

from reminder import Reminder
from sport import Sport
from currency import Currency

class InputTests():    
    def __init__(self):
        self.testFileInputs = 'testInputs.xml'
        self.testFileAnswers = 'testAnswers.xml'
        self.tests = []
        self.initTestList()        
    
    def initTestList(self):
        try:
            xmldoc = minidom.parse(self.testFileInputs)
            itemList = xmldoc.getElementsByTagName('test')
            # tests are a list of tuples(module, input)
            for item in itemList:
                module = item.attributes['module'].value
                userInput = item.attributes['input'].value
                if module == None or userInput == None:
                    continue
                else:
                    self.tests.append((module, userInput))
        except:
            print("Error: parsing test inputs")
    
    def fixXmlString(self, rootElement):
        rough_string = ElementTree.tostring(rootElement, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="   ")
    
    def logToFile(self):
        ''' Tutorial: https://pymotw.com/2/xml/etree/ElementTree/create.html '''
        root = Element('root')
        comment = Comment('Test time: {}'.format(str(datetime.datetime.now())))
        root.append(comment)
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
    
    def getAnswer(self, userInput=None):        
        for i in range(len(self.tests)): # t is a tuple(module, input)
            try:
                # eval('from ' + self.tests[i][0].lower() + ' import ' + self.tests[i][0])
                moduleObj = eval(self.tests[i][0] + '()')
                answer = moduleObj.getAnswer(self.tests[i][1])
                # making new tuple: (module, user_input, answer)
                self.tests[i] = (self.tests[i][0], self.tests[i][1], answer)
            except:
                print('Test failed for:', str(self.tests[i]))
                traceback.print_exc()
                self.tests[i] = None
        # popping failed tests using decrementing for loop
        for i in range(len(self.tests) - 1, -1, -1):
            try:
                if self.tests[i] == None:
                    self.tests.pop(i)
            except:
                print("Error: cannot pop %d" % i)
                
        self.logToFile()
        return 'Test successfully saved at: ```' + self.testFileAnswers + '```'
    
if __name__ == '__main__':
    obj = InputTests()
    obj.getAnswer()
