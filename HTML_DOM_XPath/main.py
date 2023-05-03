
import HH_parsing
import JC_parsing
import DB_update


HH_parsing.parseHH()

JC_parsing.parseJC()

DB_update.updateDB("hh.json")
DB_update.updateDB("jc.json") 


