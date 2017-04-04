import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as features

class WatsonNLU(object):
    def __init__(self, creds_file):
        self.creds = NLUCreds(creds_file)
        self.nlu = NaturalLanguageUnderstandingV1(
            version = '2017-02-27',
            username = self.creds.user,
            password = self.creds.passwd
        )
    
    def annotate(self, text, tags):
        f_list = self.featureList(tags)
        return self.nlu.analyze(text=text, features=f_list)
    
    def featureList(self, tags):
        f_list = []
        for tag in tags:
            if tag == "sentiment":
                f_list.append(features.Sentiment())
            elif tag == "categories":
                f_list.append(features.Categories())
            elif tag == "concepts":
                f_list.append(features.Concepts())
            elif tag == "emotion":
                f_list.append(features.Emotion())
            elif tag == "entities":
                f_list.append(features.Entities())
        return f_list
    
class NLUCreds(object):
    def __init__(self, file_path):
        with open(file_path) as creds:
            nlu_creds = json.load(creds)
            self.user = nlu_creds["username"]
            self.passwd = nlu_creds["password"]