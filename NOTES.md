Research notes:
1. Doesn't support upload file yet
2. Get the input feature from
    2.1 URLs
    2.2 GET Params (after ?)
    2.3 Body params (for post parameters)
3. CONTENT-TYPE IS IMPORTANT FOR BODY PARAMS
    1. Calculate normal alphanumeric (COUNT ALL OF THOSE IN 1 Variable)
        a-zA-Z0-9
    2. Calculate these non-alphanumeric (COUNT PER CHARACTER)
        ~ ! @ # $ % ^ & * ( ) _ + { } | : " < > ? ` - = [ ] \ ; ', . / <<<SPACE>>>
    3. Calculate character outside recognize char
4. Feature mapping
        alphanumeric = 1
        non-alpha = 33
        outside = 1
        length of its input = 1
        feature per value = 36