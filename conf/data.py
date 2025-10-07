import sqlite3

connection = sqlite3.connect('F:\\BDZX\\data\\bdzx.db3')
cursor = connection.cursor()


def get_attr(s_name,table,key,val):
    sql = "select {} from {} where {} = '{}'".format(s_name,table,key,val)
    cursor.execute(sql)
    results = cursor.fetchall()
    # cursor.close()
    return results[0][0]

def update_attr(table,col,val1,key,val2):
    sql = "update {} set {} = '{}' where {} = '{}'".format(table,col,val1,key,val2)
    cursor.execute(sql)
    connection.commit()
    # cursor.close()

login_data = {
            'account': get_attr('account','users','name','test'),
            'password':get_attr('password','users','name','test')
        }

headers = {
  'Blade-Auth':get_attr('token','users','name','test'),
  'Authorization': get_attr('Authorization','users','name','test'),
  'Content-Type': 'application/json'
}

