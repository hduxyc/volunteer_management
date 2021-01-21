from service.libs.mysql import db


class VolunteerModel(object):

    @staticmethod
    def get_volunteers(index, count):
        """
        获得所有志愿者服务信息
        :param index: 分页的第几页
        :param count: 分页含条目数
        :return: result:查询结果，has_next:是否有下一页
        """
        sql = f'''
            SELECT
                id,
                name,
                class_no,
                sex,
                card_id,
                task,
                date,
                duration
            FROM
                volunteer_records
            WHERE 
                is_deleted=0
            LIMIT {(index-1)*count}, {count+1}
        '''

        result = db.query(sql)
        if not result:
            return [], 0
        if len(result) == count+1:
            result.pop()
            has_next = 1
        else:
            has_next = 0
        return result, has_next

    @staticmethod
    def get_cardid_records(index, count, card_id):
        """
        根据身份证号，获得指定志愿者的服务信息
        :param index:
        :param count:
        :param card_id:
        :return:
        """
        sql = f'''
            SELECT
                id,
                name,
                class_no,
                sex,
                card_id,
                task,
                date,
                duration
            FROM
                volunteer_records
            WHERE
                card_id = {card_id}
                AND is_deleted=0
            LIMIT {(index - 1) * count}, {count + 1}
        '''

        result = db.query(sql)
        if not result:
            return [], 0
        if len(result) == count + 1:
            result.pop()
            has_next = 1
        else:
            has_next = 0
        return result, has_next