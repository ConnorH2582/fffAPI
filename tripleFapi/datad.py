import time
import requests
import datadog
from checks import CheckAgent
from hashlib import md5

class RandomCheck(AgentCheck):
    def check(self, instance):
        random_val = random.random()
        self.gauge('test.support.random', random_val)

a= RandomCheck()
a.check()
