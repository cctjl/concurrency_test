#!python
#-*- coding: utf-8

import argparse
import os
import subprocess
import time
import shutil
from runConfig import RunConfig
from requests import requests
import random
import threading


def get_connections(request_config):
    if 'connections' in request_config:
        return int(request_config['connections'])
    else:
        return RunConfig.connections


def gen_cmd(request_config):
    '''

    :param request_config:
    :return:
    '''
    # 初始化参数
    cmd = 'wrk --latency -t 1 '
    args = []

    url = request_config['url']
    method = request_config.get('method', 'GET')
    headers = request_config.get('headers', [])
    body = request_config.get('body', None)

    for header in headers:
        for header_key in header:
            args.append(' -H "%s: %s"' % (header_key, header[header_key]))
    if 'duration' in request_config:
        args.append(' -d %s' % request_config['duration'])
    else:
        args.append(' -d %s' % RunConfig.duration)
    args.append(' -c %s' % get_connections(request_config))
    # 如果有 method 和 body，就必须修改 lua 文件了
    script_path = RunConfig.script
    if method != 'GET' or body:
        script_path = RunConfig.script + str(random.randint(0, 100000))
        shutil.copy(RunConfig.script, script_path)
        RunConfig.tmp_script_paths.append(script_path)
        lua_fp = open(script_path, 'ab')
        if method != 'GET':
            lua_fp.write(bytes('\nwrk.method = "%s"' % method, encoding='utf-8'))
        if body:
            lua_fp.write(bytes('\nwrk.body = "%s"' % str(body), encoding='utf-8'))
    args.append(' -s %s' % script_path)
    cmd = cmd + ' '.join(args) + ' ' + url
    if not RunConfig.debug:
        cmd += ' 1>/dev/null'
    if RunConfig.debug:
        print(cmd)
    return cmd


def run_config(request_config):
    start = time.time()
    output = list()
    output.append('start test: %s %s, connections %s' % (request_config.get('method', 'GET'), request_config['url'],
                                                 get_connections(request_config)))
    cmd = gen_cmd(request_config)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    if stdout:
        output.append(stdout.decode('utf-8'))
    if stderr:
        output.append(stderr.decode('utf-8'))
    end = time.time()
    if RunConfig.debug:
        output.append('  completed, cost %.2fs\n' % (end - start))
    else:
        output.append('')
    for line in output:
        print(line)


def run():
    for request_config in requests:
        if RunConfig.concurrency:
            threading.Thread(target=run_config, args=(request_config,)).start()
        else:
            run_config(request_config)
    while threading.active_count() > 1:
        time.sleep(1)
    if not RunConfig.debug:
        for tmp_script_path in RunConfig.tmp_script_paths:
            os.remove(tmp_script_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='接口并发测试工具V1.0')
    parser.add_argument('--debug', dest='debug', action='store_true', default=False, help='开启debug模式，开启后会多一些输出信息，默认关闭')
    parser.add_argument('--concurrency', dest='concurrency', action='store_true', default=False, help='并行执行所有测试')

    args = parser.parse_args()
    RunConfig.debug = args.debug
    RunConfig.concurrency = args.concurrency
    run()
