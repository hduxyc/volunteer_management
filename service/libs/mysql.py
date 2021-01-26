import pymysql
import logging


class MySQLDB(object):
    def __init__(self, host='localhost', port=3306, user='root', passwd='x123456.', database='volunteer'):
        # cursorclass=pymysql.cursors.DictCursor 数据库查询返回dict字典 -- 默认：tuple元组
        self.conn = pymysql.connect(host=host,
                                    port=port,
                                    user=user,
                                    password=passwd,
                                    db=database,
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.log = logging.getLogger(__name__)

    def execute(self, sql, kwags=None):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, kwags)
            self.conn.commit()
            return cursor
        except Exception as e:
            self.log.error(f'mysqldb execute error: {e}', exc_info=True)
            raise e

    def query(self, sql, kwargs=None):
        try:
            cursor = self.execute(sql, kwargs)
            if cursor:
                return cursor.fetchall()  # 查询的所有内容， dict
            else:
                raise Exception(f'sql error: {sql}')
        except Exception as e:
            self.log.error(e)
            raise e
        finally:
            if cursor:
                cursor.close()

    def insert(self, sql, kwargs=None):
        try:
            cursor = self.execute(sql, kwargs)
            if cursor:
                row_id = cursor.lastrowid
                return row_id
            else:
                raise Exception(f'sql error: {sql}')
        except Exception as e:
            self.log.error(e)
            raise e
        finally:
            if cursor:
                cursor.close()

    def escape_string(self, _):
        return pymysql.converters.escape_string(_)


db = MySQLDB(user='root', passwd='x123456')
