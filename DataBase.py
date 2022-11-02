from sys import int_info
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from time import sleep

import Database_ui as ui

from PyQt5.QtWidgets import QMainWindow, QApplication
import numpy as np

import pymysql #資料庫套件

# 資料庫參數設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3308,
    "user": "root",
    "password": "u6ru/4",
    "db": "database",
}

# 確認資料庫是否連線成功
try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)
    print("database 連線成功")
except Exception as ex:
    print("!!!database 連線失敗!!!")
    print(ex)

class Main(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.Button_ButtonQuery.clicked.connect(self.ButtonQuery)
        self.Button_Query.clicked.connect(self.Query)
        choices = ['SELECT-FROM-WHERE', 'DELETE', 'INSERT', 'UPDATE', 'IN', 'NOT IN', 'EXISTS', 'NOT EXISTS', 'COUNT', 'SUM', 'MAX', 'MIN', 'AVG', 'HAVING ']
        self.comboBox_Button.addItems(choices)


    def ButtonQuery(self):
        print("-------------ButtonQuery-------------")

        # 尋找下拉選單的選項
        choice = self.comboBox_Button.currentText()
        print('choice = ',choice)
        print()

        if  choice == 'SELECT-FROM-WHERE':
            print('-------------SELECT-FROM-WHERE-------------')

            # 設定文字欄位顯示現在要執行的SQL語法
            self.lineEdit_ButtonQuery.setText("查詢 department 的資料表")

            with conn.cursor() as cursor:
                # 修改資料SQL語法
                command = "SELECT * FROM department"
                # 執行指令
                cursor.execute(command)

                # 得到所有查詢到的資料
                myresult = cursor.fetchall()

                # 取得欄位名稱
                field_name = [des[0] for des in cursor.description]
                # 取得欄位長度
                self.tableWidget.setColumnCount(len(field_name))
                # 設定欄位名稱
                self.tableWidget.setHorizontalHeaderLabels(field_name)
                # 取得資料長度
                self.tableWidget.setRowCount(len(myresult))
                self.tableWidget.verticalHeader().setVisible(False)

                # 顯示所查詢到的資料
                for i in range(0,len(myresult)):
                    for j in range(len(field_name)):
                        newItem = QTableWidgetItem(str(myresult[i][j]))
                        self.tableWidget.setItem(i,j,newItem)

                #儲存變更
                conn.commit()

            print("-------------SELECT-FROM-WHERE 執行完成-------------")

        elif choice == 'DELETE':
            print('-------------DELETE-------------')

            # 設定文字欄位顯示現在要執行的SQL語法
            self.lineEdit_ButtonQuery.setText("刪除 employee 表中 SSN =023 的員工資料")

            with conn.cursor() as cursor:
                # 修改資料SQL語法
                command = "DELETE FROM employee WHERE SSN ='023'"
                # 執行指令
                cursor.execute(command)

                # 取得欄位長度
                self.tableWidget.setColumnCount(1)
                # 設定欄位名稱
                self.tableWidget.setHorizontalHeaderLabels(['刪除成功'])
                # 取得資料長度
                self.tableWidget.setRowCount(0)

                #儲存變更
                conn.commit()

            print('-------------DELETE 執行完成-------------')

        elif choice == 'INSERT':
            print('-------------INSERT-------------')

            # 設定文字欄位顯示現在要執行的SQL語法
            self.lineEdit_ButtonQuery.setText("新增一筆 ('025', '雪倫', '女', '0918168400', '1992-09-08', '10') 的資料")

            with conn.cursor() as cursor:
                # 修改資料SQL語法
                command = "INSERT INTO employee VALUES ('025', '雪倫', '女', '0918168400', '1992-09-08', '10')"
                # 執行指令
                cursor.execute(command)

                # 取得欄位長度
                self.tableWidget.setColumnCount(1)
                # 設定欄位名稱
                self.tableWidget.setHorizontalHeaderLabels(['新增成功'])
                # 取得資料長度
                self.tableWidget.setRowCount(0)

                #儲存變更
                conn.commit()

            print('-------------INSERT 執行完成-------------')

        elif choice == 'UPDATE':
            print('-------------UPDATE-------------')

            # 設定文字欄位顯示現在要執行的SQL語法
            self.lineEdit_ButtonQuery.setText("更新 employee 表中 SSN=025 的手機號碼更改為 9999999")

            with conn.cursor() as cursor:
                # 修改資料SQL語法
                command = "UPDATE employee SET Ephone='9999999' WHERE SSN='025'"
                # 執行指令
                cursor.execute(command)

                # 取得欄位長度
                self.tableWidget.setColumnCount(1)
                # 設定欄位名稱
                self.tableWidget.setHorizontalHeaderLabels(['更新成功'])
                # 取得資料長度
                self.tableWidget.setRowCount(0)

                #儲存變更
                conn.commit()

            print('-------------UPDATE 執行完成-------------')

        elif choice == 'IN':
            print('-------------IN-------------')

            # 設定文字欄位顯示現在要執行的SQL語法
            self.lineEdit_ButtonQuery.setText("查詢 employee 表中部門是 1、3、5、9 的員工資料")

            with conn.cursor() as cursor:
                # 修改資料SQL語法
                command = "SELECT * FROM employee WHERE D_id IN(1,3,5,9)"
                # 執行指令
                cursor.execute(command)

                # 得到所有查詢到的資料
                myresult = cursor.fetchall()

                # 取得欄位名稱
                field_name = [des[0] for des in cursor.description]
                # 取得欄位長度
                self.tableWidget.setColumnCount(len(field_name))
                # 設定欄位名稱
                self.tableWidget.setHorizontalHeaderLabels(field_name)
                # 取得資料長度
                self.tableWidget.setRowCount(len(myresult))
                self.tableWidget.verticalHeader().setVisible(False)

                # 顯示所查詢到的資料
                for i in range(0,len(myresult)):
                    for j in range(len(field_name)):
                        newItem = QTableWidgetItem(str(myresult[i][j]))
                        self.tableWidget.setItem(i,j,newItem)

                #儲存變更
                conn.commit()


            print('-------------IN 執行完成-------------')

        elif choice == 'NOT IN':
            print('-------------NOT IN-------------')

            # 設定文字欄位顯示現在要執行的SQL語法
            self.lineEdit_ButtonQuery.setText("查詢 employee 表中部門不是 2、3、5、6 的員工資料")

            with conn.cursor() as cursor:
                # 修改資料SQL語法
                command = "SELECT * FROM employee WHERE D_id NOT IN(2,3,5,6)"
                # 執行指令
                cursor.execute(command)

                # 得到所有查詢到的資料
                myresult = cursor.fetchall()

                # 取得欄位名稱
                field_name = [des[0] for des in cursor.description]
                # 取得欄位長度
                self.tableWidget.setColumnCount(len(field_name))
                # 設定欄位名稱
                self.tableWidget.setHorizontalHeaderLabels(field_name)
                # 取得資料長度
                self.tableWidget.setRowCount(len(myresult))
                self.tableWidget.verticalHeader().setVisible(False)

                # 顯示所查詢到的資料
                for i in range(0,len(myresult)):
                    for j in range(len(field_name)):
                        newItem = QTableWidgetItem(str(myresult[i][j]))
                        self.tableWidget.setItem(i,j,newItem)

                #儲存變更
                conn.commit()


            print('-------------NOT IN 執行完成-------------')

        elif choice == 'EXISTS':
            print('-------------EXISTS-------------')

            # 設定文字欄位顯示現在要執行的SQL語法
            self.lineEdit_ButtonQuery.setText("查詢 order_list 表中有點飲料(紅茶、豆漿、奶茶)的顧客資料")

            with conn.cursor() as cursor:
                # 修改資料SQL語法
                command = "SELECT * FROM customer WHERE EXISTS(SELECT * FROM order_list WHERE customer.C_id=order_list.C_id AND M_id IN (13, 14, 15))"
                # 執行指令
                cursor.execute(command)

                # 得到所有查詢到的資料
                myresult = cursor.fetchall()

                # 取得欄位名稱
                field_name = [des[0] for des in cursor.description]
                # 取得欄位長度
                self.tableWidget.setColumnCount(len(field_name))
                # 設定欄位名稱
                self.tableWidget.setHorizontalHeaderLabels(field_name)
                # 取得資料長度
                self.tableWidget.setRowCount(len(myresult))
                self.tableWidget.verticalHeader().setVisible(False)

                # 顯示所查詢到的資料
                for i in range(0,len(myresult)):
                    for j in range(len(field_name)):
                        newItem = QTableWidgetItem(str(myresult[i][j]))
                        self.tableWidget.setItem(i,j,newItem)

                #儲存變更
                conn.commit()

            print('-------------EXISTS 執行完成-------------')

        elif choice == 'NOT EXISTS':
            print('-------------NOT EXISTS-------------')

            # 設定文字欄位顯示現在要執行的SQL語法
            self.lineEdit_ButtonQuery.setText("查詢 order_list 表中沒有點餐過的顧客資料")

            with conn.cursor() as cursor:
                # 修改資料SQL語法
                command = "SELECT * FROM customer WHERE NOT EXISTS(SELECT * FROM order_list WHERE customer.C_id=order_list.C_id)"
                # 執行指令
                cursor.execute(command)

                # 得到所有查詢到的資料
                myresult = cursor.fetchall()

                # 取得欄位名稱
                field_name = [des[0] for des in cursor.description]
                # 取得欄位長度
                self.tableWidget.setColumnCount(len(field_name))
                # 設定欄位名稱
                self.tableWidget.setHorizontalHeaderLabels(field_name)
                # 取得資料長度
                self.tableWidget.setRowCount(len(myresult))
                self.tableWidget.verticalHeader().setVisible(False)

                # 顯示所查詢到的資料
                for i in range(0,len(myresult)):
                    for j in range(len(field_name)):
                        newItem = QTableWidgetItem(str(myresult[i][j]))
                        self.tableWidget.setItem(i,j,newItem)

                #儲存變更
                conn.commit()


            print('-------------NOT EXISTS 執行完成-------------')

        elif choice == 'COUNT':
            print('-------------COUNT-------------')

            # 設定文字欄位顯示現在要執行的SQL語法
            self.lineEdit_ButtonQuery.setText("查詢 2021-12-01 總共有幾筆訂單")

            with conn.cursor() as cursor:
                # 修改資料SQL語法
                command = "SELECT COUNT(*) FROM order_list WHERE dealtime like '2021-12-01%'"
                # 執行指令
                cursor.execute(command)

                # 得到所有查詢到的資料
                myresult = cursor.fetchall()

                # 取得欄位名稱
                field_name = [des[0] for des in cursor.description]
                # 取得欄位長度
                self.tableWidget.setColumnCount(len(field_name))
                # 設定欄位名稱
                self.tableWidget.setHorizontalHeaderLabels(field_name)
                # 取得資料長度
                self.tableWidget.setRowCount(len(myresult))
                self.tableWidget.verticalHeader().setVisible(False)

                # 顯示所查詢到的資料
                for i in range(0,len(myresult)):
                    for j in range(len(field_name)):
                        newItem = QTableWidgetItem(str(myresult[i][j]))
                        self.tableWidget.setItem(i,j,newItem)

                #儲存變更
                conn.commit()


            print('-------------COUNT 執行完成-------------')

        elif choice == 'SUM':
            print('-------------SUM-------------')

            # 設定文字欄位顯示現在要執行的SQL語法
            self.lineEdit_ButtonQuery.setText("查詢 2021-12-07 單日總金額")

            with conn.cursor() as cursor:
                # 修改資料SQL語法
                command = "SELECT SUM(Oprice) FROM order_list WHERE dealtime like '2021-12-07%'"
                # 執行指令
                cursor.execute(command)

                # 得到所有查詢到的資料
                myresult = cursor.fetchall()

                # 取得欄位名稱
                field_name = [des[0] for des in cursor.description]
                # 取得欄位長度
                self.tableWidget.setColumnCount(len(field_name))
                # 設定欄位名稱
                self.tableWidget.setHorizontalHeaderLabels(field_name)
                # 取得資料長度
                self.tableWidget.setRowCount(len(myresult))
                self.tableWidget.verticalHeader().setVisible(False)

                # 顯示所查詢到的資料
                for i in range(0,len(myresult)):
                    for j in range(len(field_name)):
                        newItem = QTableWidgetItem(str(myresult[i][j]))
                        self.tableWidget.setItem(i,j,newItem)

                #儲存變更
                conn.commit()            

            print('-------------SUM 執行完成-------------')
        
        elif choice == 'MAX':
            print('-------------MAX-------------')

            # 設定文字欄位顯示現在要執行的SQL語法
            self.lineEdit_ButtonQuery.setText("查詢 2021-12-07 單日單筆最大金額")

            with conn.cursor() as cursor:
                # 修改資料SQL語法
                command = "SELECT MAX(Oprice) FROM order_list WHERE dealtime like '2021-12-07%'"
                # 執行指令
                cursor.execute(command)

                # 得到所有查詢到的資料
                myresult = cursor.fetchall()

                # 取得欄位名稱
                field_name = [des[0] for des in cursor.description]
                # 取得欄位長度
                self.tableWidget.setColumnCount(len(field_name))
                # 設定欄位名稱
                self.tableWidget.setHorizontalHeaderLabels(field_name)
                # 取得資料長度
                self.tableWidget.setRowCount(len(myresult))
                self.tableWidget.verticalHeader().setVisible(False)

                # 顯示所查詢到的資料
                for i in range(0,len(myresult)):
                    for j in range(len(field_name)):
                        newItem = QTableWidgetItem(str(myresult[i][j]))
                        self.tableWidget.setItem(i,j,newItem)

                #儲存變更
                conn.commit()    


            print('-------------MAX 執行完成-------------')
        
        elif choice == 'MIN':
            print('-------------MIN-------------')

            # 設定文字欄位顯示現在要執行的SQL語法
            self.lineEdit_ButtonQuery.setText("查詢 2021-12-07 單日單筆最小金額")

            with conn.cursor() as cursor:
                # 修改資料SQL語法
                command = "SELECT MIN(Oprice) FROM order_list WHERE dealtime like '2021-12-07%'"
                # 執行指令
                cursor.execute(command)

                # 得到所有查詢到的資料
                myresult = cursor.fetchall()

                # 取得欄位名稱
                field_name = [des[0] for des in cursor.description]
                # 取得欄位長度
                self.tableWidget.setColumnCount(len(field_name))
                # 設定欄位名稱
                self.tableWidget.setHorizontalHeaderLabels(field_name)
                # 取得資料長度
                self.tableWidget.setRowCount(len(myresult))
                self.tableWidget.verticalHeader().setVisible(False)

                # 顯示所查詢到的資料
                for i in range(0,len(myresult)):
                    for j in range(len(field_name)):
                        newItem = QTableWidgetItem(str(myresult[i][j]))
                        self.tableWidget.setItem(i,j,newItem)

                #儲存變更
                conn.commit()   

            
            print('-------------MIN 執行完成-------------')
        
        elif choice == 'AVG':
            print('-------------AVG-------------')

            # 設定文字欄位顯示現在要執行的SQL語法
            self.lineEdit_ButtonQuery.setText("查詢 2021-12-07 單日平均金額")

            with conn.cursor() as cursor:
                # 修改資料SQL語法
                command = "SELECT AVG(Oprice) FROM order_list WHERE dealtime like '2021-12-07%'"
                # 執行指令
                cursor.execute(command)

                # 得到所有查詢到的資料
                myresult = cursor.fetchall()

                # 取得欄位名稱
                field_name = [des[0] for des in cursor.description]
                # 取得欄位長度
                self.tableWidget.setColumnCount(len(field_name))
                # 設定欄位名稱
                self.tableWidget.setHorizontalHeaderLabels(field_name)
                # 取得資料長度
                self.tableWidget.setRowCount(len(myresult))
                self.tableWidget.verticalHeader().setVisible(False)

                # 顯示所查詢到的資料
                for i in range(0,len(myresult)):
                    for j in range(len(field_name)):
                        newItem = QTableWidgetItem(str(myresult[i][j]))
                        self.tableWidget.setItem(i,j,newItem)

                #儲存變更
                conn.commit()   


            print('-------------AVG 執行完成-------------')
        
        # elif choice == 'HAVING':
        else:
            print('-------------HAVING-------------')

            # 設定文字欄位顯示現在要執行的SQL語法
            self.lineEdit_ButtonQuery.setText("查詢 order_list 表中 所有當日總金額大於$100的日期")

            with conn.cursor() as cursor:
                # 修改資料SQL語法
                command = "SELECT DATE(dealtime),count(*),sum(Oprice) FROM order_list group by DATE(dealtime) HAVING sum(Oprice)>100"
                # 執行指令
                cursor.execute(command)

                # 得到所有查詢到的資料
                myresult = cursor.fetchall()

                # 取得欄位名稱
                field_name = [des[0] for des in cursor.description]
                # 取得欄位長度
                self.tableWidget.setColumnCount(len(field_name))
                # 設定欄位名稱
                self.tableWidget.setHorizontalHeaderLabels(field_name)
                # 取得資料長度
                self.tableWidget.setRowCount(len(myresult))
                self.tableWidget.verticalHeader().setVisible(False)

                # 顯示所查詢到的資料
                for i in range(0,len(myresult)):
                    for j in range(len(field_name)):
                        newItem = QTableWidgetItem(str(myresult[i][j]))
                        self.tableWidget.setItem(i,j,newItem)

                #儲存變更
                conn.commit() 


            print('-------------HAVING 執行完成-------------')

        print("-------------ButtonQuery Finsh-------------\n")
    
    def Query(self):
        print("-------------Query-------------")

        # 取得字串
        # input_word = self.lineEdit_Query.text()

        # 建立Cursor物件
        with conn.cursor() as cursor:
            # 修改資料SQL語法
            command = self.lineEdit_Query.text()
            cursor.execute(command)

        # 得到所有查詢到的資料
        myresult = cursor.fetchall()

        # 新增、修改、刪除用
        if myresult == ():
            # 取得欄位長度
            self.tableWidget.setColumnCount(1)
            # 設定欄位名稱
            self.tableWidget.setHorizontalHeaderLabels(['操作成功'])
            # 取得資料長度
            self.tableWidget.setRowCount(0)

        # 有查詢結果用
        else:
            # 取得欄位名稱
            field_name = [des[0] for des in cursor.description]
            # 取得欄位長度
            self.tableWidget.setColumnCount(len(field_name))
            # 設定欄位名稱
            self.tableWidget.setHorizontalHeaderLabels(field_name)
            # 取得資料長度
            self.tableWidget.setRowCount(len(myresult))
            self.tableWidget.verticalHeader().setVisible(False)

            # 顯示所查詢到的資料
            for i in range(0,len(myresult)):
                for j in range(len(field_name)):
                    newItem = QTableWidgetItem(str(myresult[i][j]))
                    self.tableWidget.setItem(i,j,newItem)

        conn.commit()

        print("-------------Query Finsh-------------\n")
    

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())