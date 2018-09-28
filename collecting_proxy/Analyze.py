from HTTPRequest import HTTPRequest
from pprint import pprint
import urlparse

class Analyze:
    def __init__(self,data):
        self.data = data
        self.input_features = [0] * 108

    def counting_feature(self, str, kelas):
        import re
        pattern = re.compile("^[a-zA-Z0-9]+$")

        index = 0
        if (kelas == "url"):
            index = 0
        elif (kelas == "get_params"):
            index = 35
        elif (kelas == "body_params"):
            index = 70
        else:
            print "NOT RECOGNIZED"
            sys.exit(-1)

        #~ ! @ # $ % ^ & * ( ) _ + { } | : " < > ? ` - = [ ] \ ; ', . / <<<SPACE>>>
        for c in str:
            if pattern.match(c):
                self.input_features[index+0] += 1
            elif (c == "~"):
                self.input_features[index+1] += 1
            elif (c == "!"):
                self.input_features[index+2] += 1
            elif (c == "@"):
                self.input_features[index+3] += 1
            elif (c == "#"):
                self.input_features[index+4] += 1
            elif (c == "$"):
                self.input_features[index+5] += 1
            elif (c == "%"):
                self.input_features[index+6] += 1
            elif (c == "^"):
                self.input_features[index+7] += 1
            elif (c == "&"):
                self.input_features[index+8] += 1
            elif (c == "*"):
                self.input_features[index+9] += 1
            elif (c == "("):
                self.input_features[index+10] += 1
            elif (c == ")"):
                self.input_features[index+11] += 1
            elif (c == "_"):
                self.input_features[index+12] += 1
            elif (c == "+"):
                self.input_features[index+13] += 1
            elif (c == "{"):
                self.input_features[index+14] += 1
            elif (c == "}"):
                self.input_features[index+15] += 1
            elif (c == "|"):
                self.input_features[index+16] += 1
            elif (c == ":"):
                self.input_features[index+17] += 1
            elif (c == "\""):
                self.input_features[index+18] += 1
            elif (c == "<"):
                self.input_features[index+19] += 1
            elif (c == ">"):
                self.input_features[index+20] += 1
            elif (c == "?"):
                self.input_features[index+21] += 1
            elif (c == "`"):
                self.input_features[index+22] += 1
            elif (c == "-"):
                self.input_features[index+23] += 1
            elif (c == "="):
                self.input_features[index+24] += 1
            elif (c == "["):
                self.input_features[index+25] += 1
            elif (c == "]"):
                self.input_features[index+26] += 1
            elif (c == "\\"):
                self.input_features[index+27] += 1
            elif (c == ";"):
                self.input_features[index+28] += 1
            elif (c == "'"):
                self.input_features[index+29] += 1
            elif (c == ","):
                self.input_features[index+30] += 1
            elif (c == "."):
                self.input_features[index+31] += 1
            elif (c == "/"):
                self.input_features[index+32] += 1
            elif (c == " "):
                self.input_features[index+33] += 1
            else:
                self.input_features[index+34] += 1        
        self.input_features[index+35] += 1


    def split_query_data(self, content_type, content):
        #to gain all value from variable
        data = ""
        if (content_type == "application/json"):
            print "Parsing as json..."
            try:
                import json
                data = json.loads(content)
            except:
                print "Something went error"

        elif (content_type == "application/x-www-form-urlencoded"):
            print "Parsing as url..."
            try:
                from urlparse import parse_qs
                data = parse_qs(content)
            except:
                print "Something went error"

        elif (content_type == "application/xml"):
            print "Parsing as XML..."
            try:
                import xmltodict
                data = xmltodict.parse(content)
            except:
                print "Something went error"

        else:
            print "This type either not supported or let it go"

        for key in data:
            self.counting_feature(data[key][0],"body_params")

        print "==========================================================="
        pprint(self.input_features)

    def analyze(self):
        request = HTTPRequest(self.data)
        content = self.data.split("\r\n\r\n")[1]
        if (request.command == "POST"):
            #pprint(vars(request))
            #print "================="
            #pprint(vars(request.headers))
            #print "================="
            if ('content-type' in request.headers):
                self.split_query_data(request.headers['content-type'].lower(), content)