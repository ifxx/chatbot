#!/usr/bin/env 
#coding=utf-8
import jenkins
from time import sleep
import itchatmp

jenkins_server_url='http://ssncg.koreacentral.cloudapp.azure.com:8080'
#在用户设定中找到uid 和 token
user_id='scott'
api_token='xxxxxxxxxxxxx12c7124b6dfb5'
server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
jobOn = 'testOn'
jobOff = 'testOff'

def run_jenkins_job(jobname):
    next_build_number = server.get_job_info(jobname)['nextBuildNumber']
    server.build_job(jobname)
    sleep(2)
# 返回执行结果
    return server.get_build_info(jobname, next_build_number)[u'result']

itchatmp.update_config(itchatmp.WechatConfig(
    token='scott',
    appId = 'wx297e7d13e096de5a',
    appSecret = 'b3d11f31887ab4780c0355fb4f098e4b'))

@itchatmp.msg_register(itchatmp.content.TEXT)
def text_reply(msg):
    if msg['Content'] == 'D:ON':
        result=run_jenkins_job(jobOn)
        return result
    elif msg['Content'] == 'D:OFF':
        result=run_jenkins_job(jobOff)
        return result

itchatmp.run(port=80)
