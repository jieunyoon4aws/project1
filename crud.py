from pymysql import *

# db처리는 따로 모듈 만듦. 이외에 컨트롤러 부분, 화면 뷰 구성 정도로 모듈 성격별로 나눌 수 있음

def sign_up(id, pw, name, country, city, birthday, gender):
    con = connect(host='localhost', user='root', password ='1234', db = 'facebook')
    cur = con.cursor()

    sql = "insert into members values('%s','%s','%s','%s','%s','%s','%s','default.png', '', '%s')" % (id, pw, name, country, city, birthday, gender, pw)

    cur.execute(sql)
    con.commit()
    con.close()

def sign_in(id):
    con = connect(host = 'localhost', user = 'root', password = '1234', db = 'facebook')
    cur = con.cursor()

    sql = "select pw from members where id = '%s'" % id

    cur.execute(sql)
    result = cur.fetchone()
    con.close()

    return result

def my_info_update(id, pw, name, country, city, birthday, gender, hobby, profile, pw2):
    con = connect(host='localhost', user='root', password ='1234', db = 'facebook')
    cur = con.cursor()

    sql = """update members set pw = '%s', name = '%s', country = '%s', city = '%s', birthday = '%s', gender = '%s', 
        hobby = '%s', profile = '%s', pw2 = '%s' where id = '%s'""" % (pw, name, country, city, birthday, gender, hobby, profile, pw2, id)

    cur.execute(sql)
    con.commit()
    con.close()


def delete_account(id):
    con = connect(host='localhost', user='root', password ='1234', db = 'facebook')
    cur = con.cursor()
    sql = "delete from members where id = '%s' " % id
    cur.execute(sql)
    con.commit()
    con.close()

def select_my_info(id): # 게시판 관련 함수
    con = connect(host='localhost', user='root', password ='1234', db = 'facebook')
    cur = con.cursor()

    sql = "select * from members where id = '%s'" % id

    cur.execute(sql)

    record = list(cur.fetchone())     

    con.commit()
    con.close()

    return record

def select_my_id(my_id):
    con = connect(host='localhost', user='root', password ='1234', db = 'facebook')
    cur = con.cursor()

    sql = "select id from members where id = '%s'" % my_id

    cur.execute(sql)

    record = cur.fetchone()

    con.commit()
    con.close()

    return record

def select_all_id():
    con = connect(host = 'localhost', user='root', password = '1234', db = 'facebook')
    cur = con.cursor()

    sql = "select id from members"

    cur.execute(sql)

    record = cur.fetchall()

    con.close()

    return record
