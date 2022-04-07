import fitz
import os

os.chdir(r"C:\Users\kulra\OneDrive\Desktop\SplittedPDF\Updated_set_of_test_prints_____RE-_TESTS_FOR_NEW_PROGRAM_-_Tracker_Pro")
print(os.getcwd())

pdf_document = "0 Due Diligence AVI Foreign TEST TEST (4).pdf"
doc = fitz.open(pdf_document)
print ("number of pages: %i" % doc.pageCount)
#print(doc.metadata)

page1 = doc.load_page(0)
page1text = page1.get_text("text")
print(page1text)

#pageText = {}
#pageText = page1text.list()
print(type(page1text))
pageText = page1text.split("\n")
print(type(pageText))

print(pageText)

#agentCode = ""

def find_agent_code(pageText):
    for item in pageText:
        if item.startswith("Agent Code:" or"Contract:"):
            agentCode = item
            return agentCode
            break
    #return agentCode

agentCode = find_agent_code(pageText)
print(agentCode)
agentCode = agentCode.replace("Agent Code: ","")
print(agentCode)
print(agentCode.length())