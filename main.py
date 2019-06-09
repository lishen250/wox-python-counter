# -*- coding: utf-8 -*-
from wox import Wox,WoxAPI
import sqlite3 as sql

class Counter(Wox):

    whole = 1


    # 暂定支持以下几种 方法
    # ct creat <title> <defaultPos> <defaultAdd> <addOrSub> <defaultValue>
    # ct list
    # ct
    #
    def query(self, query):
        results = []

        results.append({
            "Title": "Hello World {} times".format(self.whole),
            "SubTitle": "Query: {}".format(query),
            "IcoPath":"Images/add.png",
            "ContextData": "ctxData",
            "JsonRPCAction": {},
            "dontHideAfterAction": True
        })
        retVar = query.split();
        if retVar[0].lower() == "add":
            self.debug("yes!" + self.whole)
            ret = self.format_field(title='调用几次',subtitle=self.whole)
            results.append(ret)

            self.whole += 1;
        #
        #
        # results.append(self.format_field(title="总共",subtitle=self.whole))

        return results

    @staticmethod
    def format_field(self,title='',subtitle='',icoPath='smile',contextData='ctxData', JsonRPCAction={}, dontHideAfterAction = True):
        return {
            "Title": title,
            "SubTitle": subtitle,
            "IcoPath":"Images/" + icoPath + ".png",
            "ContextData": contextData,
            "JsonRPCAction": JsonRPCAction,
            "dontHideAfterAction": dontHideAfterAction
        }


    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(data),
            "IcoPath":"Images/app.ico"
        })
        return results

if __name__ == "__main__":
    Counter()
