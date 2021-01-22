from flask_restplus import Resource
from service.apis import api
from flask import request
from service.models.volunteers import VolunteerModel


class VolunteerParsers(object):
    @staticmethod
    def getvolunteerlist():
        # 解析器 志愿者服务信息列表
        parser = api.parser()
        parser.add_argument('index', type=int, help='第几页', required=True)
        parser.add_argument('count', type=int, help='每页包含多少数据', required=True)
        return parser

    @staticmethod
    def getvolunteerCardIdSearch():
        # 解析器 根据志愿者身份证号获得服务信息列表
        parser = api.parser()
        parser.add_argument('index', type=int, help='第几页', required=True)
        parser.add_argument('count', type=int, help='每页包含多少数据', required=True)
        parser.add_argument('card_id', type=str, help='志愿者身份证', required=True)
        return parser

    @staticmethod
    def insertvolunteerRecord():
        # 解析器 添加志愿者服务信息
        parser = api.parser()
        parser.add_argument('name', type=str, help='姓名', required=True)
        parser.add_argument('class_no', type=str, help='班级', required=True)
        parser.add_argument('sex', type=str, help='性别', required=True)
        parser.add_argument('card_id', type=str, help='志愿者身份证', required=True)
        parser.add_argument('task', type=str, help='任务', required=True)
        parser.add_argument('date', type=str, help='日期', required=True)
        parser.add_argument('duration', type=int, help='服务时长', required=True)
        return parser


class VolunteerList(Resource):
    @api.expect(VolunteerParsers.getvolunteerlist())
    def get(self):
        index = int(request.values.get('index', 0))
        count = int(request.values.get('count', 0))
        papers, has_next = VolunteerModel.get_volunteers(index, count)
        return {
            'status': 10000,
            'msg': 'success',
            'data': papers,
            'index': index,
            'count': count,
            'has_next': has_next
        }


class VolunteerCardidSearch(Resource):
    @api.expect(VolunteerParsers.getvolunteerCardIdSearch())
    def get(self):
        index = int(request.values.get('index', 0))
        count = int(request.values.get('count', 0))
        card_id = request.values.get('card_id', '')
        papers, has_next = VolunteerModel.get_cardid_records(index, count, card_id)
        return {
            'status': 10000,
            'msg': 'success',
            'data': papers,
            'index': index,
            'count': count,
            'has_next': has_next
        }


class VolunteerRecordInsert(Resource):
    @api.expect(VolunteerParsers.insertvolunteerRecord())
    def get(self):
        name = request.values.get('name', '')
        class_no = request.values.get('class_no', '')
        sex = request.values.get('sex', '')
        card_id = request.values.get('card_id', '')
        task = request.values.get('task', '')
        date = request.values.get('date', '')
        duration = int(request.values.get('duration', 0))
        record, index = VolunteerModel.insert_cardid_records(name, class_no, sex, card_id, task, date, duration)
        return {
            'status': 10001,
            'msg': 'success',
            'data': record,
            'index': index,
        }


ns = api.namespace('volunteers', description='志愿者信息管理接口')
ns.add_resource(VolunteerList, '', '/')
ns.add_resource(VolunteerCardidSearch, '/card_id', '/card_id/')
ns.add_resource(VolunteerRecordInsert, '/inset', '/inset/')