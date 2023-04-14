import os
import MySQLdb
from MySQLdb.cursors import DictCursor
from dbutils.pooled_db import PooledDB

from settings import DATABASES, BASE_DIR

mysql_account = DATABASES['default']['USER']
mysql_passwd = DATABASES['default']['PASSWORD']
mysql_ip = DATABASES['default']['HOST']
mysql_port = DATABASES['default']['PORT']
db_name = DATABASES['default']['NAME']


class Config(object):
    pass


class DbManager(object):

    _pool = None

    def __init__(self):
        self.conn = self.get_conn()
        self.cur = self.conn.cursor()

    @staticmethod
    def get_conn():
        if DbManager._pool is None:
            _pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=20,
                             host=mysql_ip, port=mysql_port, user=mysql_account, passwd=mysql_passwd, db=db_name,
                             use_unicode=False, charset="utf8", cursorclass=DictCursor)
        return _pool.connection()

    def __del__(self):
        """
        :return:
        """
        self.dispose()

    def execute(self, sql, args=None):
        print(f"the sql is {sql}")
        self.cur.execute(sql, args)

    def executemany(self, sql, args=None):
        self.cur.executemany(sql, args)

    def copy_from(self, f, table, origin_column_list):
        self.cur.copy_from(f, table, columns=origin_column_list, sep='\t', null='\\N', size=60000)  # 默认sep和null 都是none

    def execute_fetchall(self, sql, args=None):
        self.execute(sql, args)
        result = self.cur.fetchall()
        print(f"shun ========================================{result}", type(result))
        if isinstance(result, tuple):
            result = list(result)
        return result

    def execute_fetchone(self, sql, args=None):
        self.execute(sql, args)
        result = self.cur.fetchone()
        print(f"shun ========================================{result}", type(result))
        if isinstance(result, tuple):
            result = list(result)
        return result

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def begin(self):
        """
        @summary: 开启事务
        """
        self.conn.autocommit(0)

    def end(self, option='commit'):
        """
        @summary: 结束事务
        """
        if option == 'commit':
            self.conn.commit()
        else:
            self.conn.rollback()

    def dispose(self, isEnd=1):
        """
        @summary: 释放连接池资源
        """
        if isEnd == 1:
            self.end('commit')
        else:
            self.end('rollback');
        self.cur.close()
        self.conn.close()

    def close(self):
        self.cur.close()
        self.conn.close()


class MysqlManager(DbManager):
    def __init__(self):
        super(MysqlManager, self).__init__()

    def call_procedure(self, table, threshold_value):
        """
        调用存储过程
        :param table: 表名称
        :param threshold_value:查询阈值
        :return:
        """
        self.cur.callproc("alarm_ip", args=(table, threshold_value, '@query_string'))
        return self.cur.fetchall()

    @staticmethod
    def event():
        """
        定义事件
        :return:
        """
        pass

    def create(self):
        """
        将过程和事件写入mysql
        :return:
        """
        # self.start_all()
        # print('=================存储过程已经启用')
        # print(os.system(f"mysql -u{mysql_account} -p{mysql_passwd} {db_name} < {self.file}"))
        pass

    def restart_event(self):
        """
        重启事件
        :return:
        """
        self.execute('set global event_scheduler=OFF;', None)
        self.execute('set global event_scheduler=ON;', None)
        self.create()

    def stop_all(self):
        """
        停止所有事件
        :return:
        """
        self.execute('set global event_scheduler=OFF;', None)

    def start_all(self):
        self.execute('set global event_scheduler=ON;', None)

    def start_tasks(self):
        self.start_all()
        self.create()

    def start(self, name):
        """
        开启单个事件
        :return:
        """
        self.execute('alter event {event_name} on completion preserve enable  disable]'.format(event_name=name), None)

    def stop(self, name):
        """
        关闭单个事件
        :return:
        """
        self.execute('alter event {event_name} on completion preserve disable'.format(event_name=name), None)


if __name__ == '__main__':
    env = MysqlManager()
    env.create()
