'''
write a python program which generates a html file/string to display a json in the below format
- dict will be represented as table with key and value in 2 columns
- list will be represented as an unordered list of items
- string, number and other types as it is
'''


class HTMLGenerator:
    __final_html = ''
    __trial_html = '</table></body></html>'
    __output_file = r'C:\Temp\result.html'
    
    def __init__(self):
        self.__final_html = '''
        <html>
        <head>
        <style>
            table, th, td {
              border: 1px solid black;
            }
        </style>
        </head>
        <body><table>'''
    
    def addTrialTags(self):
        self.__final_html = self.__final_html + self.__trial_html
    
    def getHTML(self):
        return self.__final_html
    
    def createCompleteRow(self, value):
        self.__final_html = self.__final_html + '<tr><td>{0}</td><td>{1}</td></tr>'.format(value[0], str(value[1]))
    
    def basicFileWrite(self):
        try:
            f = open(self.__output_file, 'w')
            f.write(self.__final_html)
            f.close()
        except Exception as e:
            print('Writing failed! ',e)
        
    def addSingleListItem(self, text):
        self.__final_html = self.__final_html + '<li>' + str(text) + '</li>'
    
    def addSingleElementColumn(self, text):
        self.__final_html = self.__final_html + '<td>{0}</td>'.format(text)
    
    def closeTableRow(self):
        self.__final_html = self.__final_html + '</tr>'
    
    def openTableRow(self):
        self.__final_html = self.__final_html + '<tr>'
    
    def openOrderedList(self):
        self.__final_html = self.__final_html + '<ul>'
    
    def closeOrderedList(self):
        self.__final_html = self.__final_html + '</ul>'
    
    def openListItem(self):
        self.__final_html = self.__final_html + '<li>'
    
    def closeListItem(self):
        self.__final_html = self.__final_html + '</li>'
    
    def openTable(self):
        self.__final_html = self.__final_html + '<table>'
    
    def closeTable(self):
        self.__final_html = self.__final_html + '</table>'
    
    def openTableData(self):
        self.__final_html = self.__final_html + '<td>'
    
    def closeTableData(self):
        self.__final_html = self.__final_html + '</td>'

def htmlHelper(obj, htmlGenerator):
    print('...'+str(obj)+'...')
    if isinstance(obj,dict):
        htmlGenerator.openTable()
        for item in obj.items():
            if isinstance(item, tuple):
                if isinstance(item[1], str) or isinstance(item[1], int):
                    htmlGenerator.createCompleteRow(item)
                elif isinstance(item[1], list) or isinstance(item[1], dict):
                    htmlGenerator.openTableRow()
                    htmlGenerator.addSingleElementColumn(item[0])
                    htmlGenerator.openTableData()
                    htmlHelper(item[1], htmlGenerator)
                    htmlGenerator.closeTableData()
                    htmlGenerator.closeTableRow()
        htmlGenerator.closeTable()
    if isinstance(obj, list):
        if len(obj) > 0:
            if  isinstance(obj[0], str) or isinstance(obj[0], int):
                
                htmlGenerator.openOrderedList()
                for item in obj:
                    htmlGenerator.addSingleListItem(item)
                htmlGenerator.closeOrderedList()
                return
            else:
                htmlGenerator.openOrderedList()
                for o in obj:
                    htmlGenerator.openListItem()
                    htmlHelper(o, htmlGenerator)
                    htmlGenerator.closeListItem()
                htmlGenerator.closeOrderedList()
    

if __name__ == '__main__':
    _json =    {
    "medications":[{
            "aceInhibitors":[{
                "name":"lisinopril",
                "strength":"10 mg Tab",
                "dose":"1 tab",
                "route":"PO",
                "sig":"daily",
                "pillCount":"#90",
                "refills":"Refill 3"
            }],
            "antianginal":[{
                "name":"nitroglycerin",
                "strength":"0.4 mg Sublingual Tab",
                "dose":"1 tab",
                "route":"SL",
                "sig":"q15min PRN",
                "pillCount":"#30",
                "refills":"Refill 1"
            }],
            "anticoagulants":[{
                "name":"warfarin sodium",
                "strength":"3 mg Tab",
                "dose":"1 tab",
                "route":"PO",
                "sig":"daily",
                "pillCount":"#90",
                "refills":"Refill 3"
            }],
            "betaBlocker":[{
                "name":"metoprolol tartrate",
                "strength":"25 mg Tab",
                "dose":"1 tab",
                "route":"PO",
                "sig":"daily",
                "pillCount":"#90",
                "refills":"Refill 3"
            }],
            "diuretic":[{
                "name":"furosemide",
                "strength":"40 mg Tab",
                "dose":"1 tab",
                "route":"PO",
                "sig":"daily",
                "pillCount":"#90",
                "refills":"Refill 3"
            }],
            "mineral":[{
                "name":"potassium chloride ER",
                "strength":"10 mEq Tab",
                "dose":"1 tab",
                "route":"PO",
                "sig":"daily",
                "pillCount":"#90",
                "refills":"Refill 3"
            }]
        }
    ],
    "labs":[{
        "name":"Arterial Blood Gas",
        "time":"Today",
        "location":"Main Hospital Lab"      
        },
        {
        "name":"BMP",
        "time":"Today",
        "location":"Primary Care Clinic"    
        },
        {
        "name":"BNP",
        "time":"3 Weeks",
        "location":"Primary Care Clinic"    
        },
        {
        "name":"BUN",
        "time":"1 Year",
        "location":"Primary Care Clinic"    
        },
        {
        "name":"Cardiac Enzymes",
        "time":"Today",
        "location":"Primary Care Clinic"    
        },
        {
        "name":"CBC",
        "time":"1 Year",
        "location":"Primary Care Clinic"    
        },
        {
        "name":"Creatinine",
        "time":"1 Year",
        "location":"Main Hospital Lab"  
        },
        {
        "name":"Electrolyte Panel",
        "time":"1 Year",
        "location":"Primary Care Clinic"    
        },
        {
        "name":"Glucose",
        "time":"1 Year",
        "location":"Main Hospital Lab"  
        },
        {
        "name":"PT/INR",
        "time":"3 Weeks",
        "location":"Primary Care Clinic"    
        },
        {
        "name":"PTT",
        "time":"3 Weeks",
        "location":"Coumadin Clinic"    
        },
        {
        "name":"TSH",
        "time":"1 Year",
        "location":"Primary Care Clinic"    
        }
    ],
    "imaging":[{
        "name":"Chest X-Ray",
        "time":"Today",
        "location":"Main Hospital Radiology"    
        },
        {
        "name":"Chest X-Ray",
        "time":"Today",
        "location":"Main Hospital Radiology"    
        },
        {
        "name":"Chest X-Ray",
        "time":"Today",
        "location":"Main Hospital Radiology"    
        }
    ]
}
    
    htmlGenerator = HTMLGenerator()
    htmlHelper(_json, htmlGenerator)
    htmlGenerator.addTrialTags()
    
    print('Result \r\n{0}\r\n'.format(htmlGenerator.getHTML()))
    
    htmlGenerator.basicFileWrite()
