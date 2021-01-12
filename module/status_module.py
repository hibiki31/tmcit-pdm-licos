import sqlite3
import os
import logging
import pprint
import shutil
import datetime
import json

def attribute_dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return AttributeDict(d)


class AttributeDict(object):
    def __init__(self, obj):
        if type(obj) != dict:
            raise
        self.obj = obj

    ### Pickle
    def __getstate__(self):
        return self.obj.items()

    ### Pickle
    def __setstate__(self, items):
        if not hasattr(self, 'obj'):
            self.obj = {}
        for key, val in items:
            self.obj[key] = val

    ### Class["key"] = "val"
    def __setitem__(self, key, val):
        self.obj[key] = val

    ### Class["key"]
    def __getitem__(self, name):
        if name in self.obj:
            return self.obj.get(name)
        else:
            return None

    ### Class.name
    def __getattr__(self, name):
        if name in self.obj:
            return self.obj.get(name)
        else:
            return None

    ### dict互換
    def keys(self):
        return self.obj.keys()

    ### dict互換
    def values(self):
        return self.obj.values()

class Connection():
    def __init__(self,path):
        self.path = path

    def sqlCommits(self,SQL,DATAS):
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        cur.executemany(SQL,DATAS)
        con.commit()

    def sqlCommit(self,SQL,DATA):
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        cur.execute(SQL,DATA)
        result = cur.lastrowid
        con.commit()
        return result

    def sqlFetchall(self,SQL,DATA):
        con = sqlite3.connect(self.path)
        con.row_factory = attribute_dict_factory
        cur = con.cursor()
        return cur.execute(SQL,DATA).fetchall()

    def sql_seed(self):
        data = (
            [],
            [],
        )
        sql = "insert into table(a,b) values(?,?)"
        self.sqlCommits(sql,data)

    def sql_init(self):
        try:
            os.remove(self.path)
        except:
            pass
        con = sqlite3.connect(self.path)
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = 1")
        cur.execute("""
        CREATE TABLE status
        (
            rool TEXT NOT NULL,
            key TEXT NOT NULL,
            value TEXT NOT NULL,
            PRIMARY KEY (rool,key)
        );
        """)
        con.commit()
        cur.close()
        con.close()

def save(rool, key, value):
    json_str = json.dumps(value)
    db = Connection("data.sqlite3")
    db.sqlCommit("insert or replace into status (rool,key,value) values (?,?,?)",[rool,key,json_str])

def load(rool, key):
    db = Connection("data.sqlite3")
    result = db.sqlFetchall("select * from status where rool=? and key=?",[rool,key])
    if len(result) == 0:
        return False
    else:
        return json.loads(result[0]["value"])

def init():
    db = Connection("data.sqlite3")
    db.sql_init()