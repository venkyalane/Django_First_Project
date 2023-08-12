import mysql.connector

def Student(fn,ln,jd,po):
    conn = mysql.connector.connect(host='localhost',
                            user='root',
                            port=3307,
                            database='django_third_project'
                            )
    CurObj = conn.cursor()
    sql_qry = 'insert into members_member (firstname,lastname,joined_date,phone) values (%(fn)s, %(ln)s, %(jd)s, %(po)s)'
    params = {'fn':fn, 'ln':ln, 'jd':jd, 'po':po}
    try:
        CurObj.execute(sql_qry,params)
        conn.commit()
        print(CurObj.rowcount, 'inserted')

    except:
        conn.rollback()
        print("Unable to insert")

    CurObj.close()
    conn.close()

while True:
    fn= input("Enter firstname:")
    ln= input("Enter lastname:")
    jd= input("Enter JOin date:")
    po= int(input("Enter phone:"))
    Student(fn,ln,jd,po)
    exit = input("Do you want to exit?(y/n):")
    if exit == 'y':
        break