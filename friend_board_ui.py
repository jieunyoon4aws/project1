from pymysql import *


def friend_info(id):    # 정보 출력
    con = connect(host = 'localhost', user = 'root', password = '1234', db = 'facebook')
    cur = con.cursor()
    sql = "select * from members where id = '%s'" % id   #친구id
    cur.execute(sql)
    record = list(cur.fetchone())
    con.commit()
    con.close()
    return record


def content_insert(content_num, friend_num, id1, id2, content):   # 게시물 등록
    con = connect(host = 'localhost', user = 'root', password = '1234', db = 'facebook')
    cur = con.cursor()
    sql = """insert into board values('%d', '%d', '%s', '%s', '%s')""" % (content_num, friend_num, id1, id2, content) 
    cur.execute(sql)
    con.commit()
    con.close()



def content_number():
    con = connect(host = 'localhost', user = 'root', password = '1234', db = 'facebook')
    cur = con.cursor()
    sql = "select content_num from board order by content_num DESC"
    cur.execute(sql)
    result = cur.fetchone()
    con.close()
    return result


def content_list(num):   # 게시물 목록 출력
    con = connect(host = 'localhost', user = 'root', password = '1234', db = 'facebook')
    cur = con.cursor()
    sql = "select writer_id, content from board where content_num = '%d'" % num
    cur.execute(sql)

    record = list(cur.fetchone())

    con.commit()
    con.close()
    return record


def content_owner(id):
    con = connect(host = 'localhost', user = 'root', password = '1234', db = 'facebook')
    cur = con.cursor()
    sql = "select content_num from board where owner_id = '%s'" % id
    cur.execute(sql)

    result = []
    while True:
        record = cur.fetchone()
        if record == None:
            break
        else:
            result.append(list(record))

    con.commit()
    con.close()
    return result


def content_num(id):    # 개별 게시판 게시글 정보 출력
    con = connect(host = 'localhost', user = 'root', password = '1234', db = 'facebook')
    cur = con.cursor()
    sql = "select content_num from board where owner_id = '%s' order by content_num DESC" % id   #친구id
    cur.execute(sql)
    record = list(cur.fetchall())
    con.close()
    return record


def content_select(num): # 작성자 id, 게시물 내용 출력
    con = connect(host = 'localhost', user = 'root', password = '1234', db = "facebook")
    cur = con.cursor()
    sql = "select writer_id, content from board where content_num = '%d'" % num
    cur.execute(sql)

    record = cur.fetchone()

    con.commit()
    con.close()

    return record

def writer_info_select(id):
    con = connect(host = 'localhost', user = 'root', password = '1234', db = "facebook")
    cur = con.cursor()
    sql = "select profile, name from members where id = '%s'" % (id)
    cur.execute(sql)

    record = cur.fetchone()

    con.commit()
    con.close()

    return record


def friend_content_update(num, new_content):   # 게시물 수정
    con = connect(host = 'localhost', user = 'root', password = '1234', db = 'facebook')
    cur = con.cursor()
    sql = "update board set content = '%s' where content_num = '%d'" % (new_content, num)
    cur.execute(sql)
    con.commit()
    con.close()



def friend_content_delete(num):   # 게시물 삭제
    con = connect(host = 'localhost', user = 'root', password = '1234', db = 'facebook')
    cur = con.cursor()
    sql = "delete from board where (content_num) = '%d'" % num
    cur.execute(sql)
    con.commit()
    con.close()


# 친구 조회

def friend_select(id1, id2):
    con = connect(host = 'localhost', user = 'root', password = '1234', db = "facebook")
    cur = con.cursor()
    sql = "select id from friends where user1 = '%s' and user2 = '%s'" % (id1, id2)

    cur.execute(sql)

    record = cur.fetchone()

    if record == None:
        record = ""
    else:
        record = record[0]

    con.commit()
    con.close()

    return record

def friend_id_select(id):
    con = connect(host = 'localhost', user = 'root', password = '1234', db = "facebook")
    cur = con.cursor()
    sql = "select id from members where id = '%s'" % (id)
    cur.execute(sql)

    record = cur.fetchone()

    con.commit()
    con.close()

    return record


def friend_insert(id1, id2): # 친구 추가
    con = connect(host = 'localhost', user = 'root', password = '1234', db = "facebook")
    cur = con.cursor()
    # 친구추가 시 friends 테이블의 user1, user2 필드 모두에 두 아이디가 들어가게 처리
    if id1 != id2:
        sql1 = "insert into friends set user1 = '%s', user2 = '%s'" % (id1, id2)
        sql2 = "insert into friends set user1 = '%s', user2 = '%s'" % (id2, id1)
        cur.execute(sql1)
        cur.execute(sql2)
    # 회원가입 시 friends 테이블에 user1, user2 필드 모두에 아이디가 들어가게 처리
    elif id1 == id2:
        sql = "insert into friends set user1 = '%s', user2 = '%s'" % (id1, id2)        
        cur.execute(sql)
        
    con.commit()
    con.close()
