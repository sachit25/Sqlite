from datetime import date
import sqlite3

def insert_data():
    conn=sqlite3.connect('test.db')

    cursor = conn.execute(" SELECT * FROM FOReCAST ORDER BY Id DESC LIMIT 1")
    new_id=0
    for row in cursor:
        print(row,"-------row----")
        new_id=row[0]
        print(new_id,"------new id-----")



    conn.execute('''INSERT INTO FORECAST(Id,
                Material_Number,
                Region,
                Delivering_Plant  ,
                Sold_To_Customerr_Name  ,
                Standard_price_USD  ,
                SafetyFactor,
                Quantity_Delivered,
                ss,
                Lead_Time,
                Predicted,
                safety_stock,
                ROP ,
                Max_Stock ,
                Churn_in_Dollar ,
                Service_Level ,
                Forecast_Buckets ,
                Forecast_Periods,
                Delivery_Time
                ) \
            VALUES ({},526, 'Asia', 'india', 'bbbb', 2000,20.5,44,0,55,66,0,0,2,6.5,8,6,2,'{}');'''.format(new_id+1,date.today()))

    conn.commit()
    print ("Records created successfully")
    conn.close()        




def create_forecast_table():
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    conn.execute('''CREATE TABLE if not exists Forecast
            (Id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
            Material_Number CHAR(10) ,
            Region CHAR(50),
            Delivering_Plant CHAR(100),
            Sold_To_Customerr_Name CHAR(50),
            Standard_price_USD int,
            SafetyFactor real,
            Quantity_Delivered,
            SS int,
            Lead_Time int,
            Predicted int,
            safety_stock int,
            ROP int,
            Max_Stock int,
            Churn_in_Dollar real,
            Service_Level int,
            Forecast_Buckets int,
            Forecast_Periods int,
            Delivery_Time DATE NOT NULL
            );''')
    conn.commit()
    print("Forecast Table created ")    
    conn.close()            

def delete_table():
    conn = sqlite3.connect('test.db')

    conn.execute("drop table FORECAST")
    conn.commit()
    print("Table Deleted")
    
def get_data():
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    cursor = conn.execute("select * from FORECAST ")
    print(cursor)
    # cursor = conn.execute("select * from FORECAST inner join Override on Id=Override.Override_id")
    # print(cursor.fetchall())
    for row in cursor:
        print(row) 
# delete_table()
# create_forecast_table()
get_data()        


def check_table_column():
    conn = sqlite3.connect('test.db')
    cursor=conn.execute("PRAGMA table_info(FORECAST)") 
    records = cursor.fetchall() 
    print(records)
    for row in records:
        print("Columns: ", row[1])

# check_table_column()        
# insert_data()