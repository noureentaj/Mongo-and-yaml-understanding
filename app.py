from pymongo import MongoClient
import yaml
import configparser
import codeThis

cfg = configparser.RawConfigParser()
cfg.read('config.conf')
code_fname = cfg.get('COUNTRY_CODE_FILE', 'filepath')
connection = MongoClient(cfg.get('MONGODB', 'uri'))
db = connection['MyDB']

print("running")
with open("properties.yml") as doc:
    document = yaml.safe_load(doc)
    # codeThis.codingthis(code_fname, document)
    document = codeThis.coding_this(code_fname, document)

for each_specimen in document:
    collection = db[each_specimen]
    collection.insert_one(document[each_specimen])
