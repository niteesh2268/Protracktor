import json

def read_config():
    '''
    This method reads the config file to get the course no.
    :returns: course no stored in the config file 
    '''
    with open("config.json") as json_data_file:
        data = json.load(json_data_file)
    return data['course_name']



def write_config(str):
    '''
    This method updates the config file with new course no.

    :param str: String argument
    '''
    with open("config.json", "w") as outfile:
        json.dump({"course_name":str}, outfile)
