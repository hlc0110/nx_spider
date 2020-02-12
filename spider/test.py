from DB.Db import Db as mysql

db = mysql("check_baihe_type")
print(db.getPrikey())