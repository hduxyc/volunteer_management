-- 数据表
CREATE TABLE `volunteer_records` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `name` varchar (20) NOT NULL DEFAULT '' COMMENT '姓名',
    `class_no` varchar (10) NOT NULL DEFAULT 0 COMMENT '班级',
    `sex` varchar (10) NOT NULL DEFAULT '' COMMENT '性别',
    `card_id` varchar(100) NOT NULL DEFAULT 0 COMMENT '身份证号',
    `task` varchar (100) NOT NULL DEFAULT '' COMMENT '任务内容',
    `date` varchar(20) NOT NULL DEFAULT 0 COMMENT '日期',
    `duration` int(11) NOT NULL DEFAULT 0 COMMENT '服务时间',
    `is_deleted` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否已删除',
    PRIMARY KEY (`id`),
    KEY `name_IDX` (`name`) USING BTREE,
    KEY `card_id_IDX` (`card_id`) USING BTREE
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT=''