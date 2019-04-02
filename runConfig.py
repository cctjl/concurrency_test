#!python
#-*- coding: utf-8


class RunConfig:
    debug = False
    # 默认100个并发连接
    connections = 20
    # 默认单线程
    threads = 1
    # 默认测试时长 60s
    duration = '10s'
    # 默认lua脚本
    script = 'report.lua'
    # 并行执行所有测试
    concurrency = False
    # 生成的临时脚本路径
    tmp_script_paths = []
