"""
Write a python function to extract data between HTML tags using Regex. Your function
should accept an input string and a list of HTML tags to look for. Your function should
return a list of the extracted data.
"""
import re

def extract_data(input_string="<p> This is amazing</p>", tags=["p"]):
    """ Given a string look for html tags and read the data in been the tags"""
    content_pattern = re.compile(r'<{0}[^>]*>(.*?)</{1}>'.format(tags[0], tags[0]), flags = re.M)
    data = content_pattern.findall(input_string)
    return data


if __name__ == '__main__':
    result = extract_data()
    print(result)