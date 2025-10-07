import os
from locust import HttpUser, task, TaskSet
from conf import  data

class BeidouTestUser(TaskSet):

    def on_start(self):
        url = '/plat-auth/token'
        headers = {'Authorization': data.get_attr('Authorization','users','name','test')}
        res = self.client.post(url=url, headers=headers, data=data.login_data)
        token =  'bearer '+ res.json()['data']['accessToken']
        data.update_attr('users','token',token,'name','test')


    @task
    def vehicle_info(self):
        url = data.get_attr('url','req_data','name','vehicle_info')
        payload = data.get_attr('payload','req_data','name','vehicle_info')
        res = self.client.post(url=url, headers=data.headers, data=payload)
        response = res.json()['data']['content'][0]['moduleCode']
        if response == data.get_attr('response1','req_data','name','vehicle_info'):
            print('vehicle_info check success')
        else:
            print('vehicle_info check failed')

    @task
    def model_info(self):
        url = data.get_attr('url','req_data','name','module_info')
        payload = data.get_attr('payload','req_data','name','module_info')
        res = self.client.post(url=url, headers=data.headers, data=payload)
        response = res.json()['data']['content'][0]['name']
        if response == data.get_attr('response1','req_data','name','module_info'):
            print('model_info check success')
        else:
            print('model_info check failed')

    @task
    def battery(self):
        url = data.get_attr('url','req_data','name','battery')
        payload = data.get_attr('payload','req_data','name','battery')
        res = self.client.post(url=url, headers=data.headers, data=payload)
        response = res.json()['data']['content'][0]['devId']
        if response == data.get_attr('response1','req_data','name','battery'):
            print('battery check success')
        else:
            print('battery check failed')

    @task
    def charge_record(self):
        url = data.get_attr('url','req_data','name','charge_record')
        payload = data.get_attr('payload','req_data','name','charge_record')
        res = self.client.post(url=url, headers=data.headers, data=payload)
        response = res.json()['data']['content'][0]['devId']
        if response == data.get_attr('response1','req_data','name','charge_record'):
            print('battery check success')
        else:
            print('battery check failed')

    @task
    def vehicle_track(self):
        url = data.get_attr('url', 'req_data', 'name', 'vehicle_track')
        payload = data.get_attr('payload', 'req_data', 'name', 'vehicle_track')
        res = self.client.post(url=url, headers=data.headers, data=payload)
        response = res.json()['data']['content'][0]['devId']
        if response == data.get_attr('response1', 'req_data', 'name', 'vehicle_track'):
            print('vehicle_track check success')
        else:
            print('vehicle_track check failed')

    @task
    def sim_card(self):
        url = data.get_attr('url', 'req_data', 'name', 'sim_card')
        payload = data.get_attr('payload', 'req_data', 'name', 'sim_card')
        res = self.client.post(url=url, headers=data.headers, data=payload)
        response = res.json()['data']['content'][0]['devId']
        if response == data.get_attr('response1', 'req_data', 'name', 'sim_card'):
            print('sim_card check success')
        else:
            print('sim_card check failed')

    @task
    def sim_usage(self):
        url = data.get_attr('url', 'req_data', 'name', 'sim_usage')
        payload = data.get_attr('payload', 'req_data', 'name', 'sim_usage')
        res = self.client.post(url=url, headers=data.headers, data=payload)
        response = res.json()['data']['content'][0]['devId']
        if response == data.get_attr('response1', 'req_data', 'name', 'sim_usage'):
            print('sim_usage check success')
        else:
            print('sim_usage check failed')

    @task
    def network(self):
        url = data.get_attr('url', 'req_data', 'name', 'network')
        payload = data.get_attr('payload', 'req_data', 'name', 'network')
        res = self.client.post(url=url, headers=data.headers, data=payload)
        response = res.json()['data']['content'][0]['contactPerson']
        if response == data.get_attr('response1', 'req_data', 'name', 'network'):
            print('network check success')
        else:
            print('network check failed')


class WebSiteUser(HttpUser):
        host = data.get_attr('url','req_data','name','host')
        tasks = [BeidouTestUser]
        min_wait = 1000
        max_wait = 3000

if __name__ == '__main__':
    os.system('locust -f locust_bd.py')