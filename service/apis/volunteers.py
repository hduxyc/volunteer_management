from flask_restplus import Resource
from service.apis import api
from flask import request
from service.models.volunteers import VolunteerModel


class VolunteerParsers(object):
    @staticmethod
    def getvolunteerlist():
        parser = api.parser()
        parser.add_argument('index', type=int, help='第几页', required=True)
        parser.add_argument('count', type=int, help='每页包含多少数据', required=True)
        return parser

    @staticmethod
    def getpaperCardIdSearch():
        # 解析器
        parser = api.parser()
        parser.add_argument('index', type=int, help='第几页', required=True)
        parser.add_argument('count', type=int, help='每页包含多少数据', required=True)
        parser.add_argument('card_id', type=str, help='志愿者身份证', required=True)
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
    @api.expect(VolunteerParsers.getpaperCardIdSearch())
    def get(self):
        index = int(request.values.get('index', 0))
        count = int(request.values.get('count', 0))
        card_id = request.values.get('card_id','')
        papers, has_next = VolunteerModel.get_cardid_records(index, count, card_id)
        return {
            'status': 10000,
            'msg': 'success',
            'data': papers,
            'index': index,
            'count': count,
            'has_next': has_next
        }


ns = api.namespace('volunteers', description='志愿者信息管理接口')
ns.add_resource(VolunteerList, '', '/')
ns.add_resource(VolunteerCardidSearch, '/card_id', '/card_id/')