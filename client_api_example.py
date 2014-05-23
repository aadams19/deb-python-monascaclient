# Copyright (c) 2014 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" An example using monclient via the Python API """

from monclient import client
import monclient.exc as exc
import time

# In order to use the python api directly, you must first obtain an
# auth token and identify which endpoint you wish to speak to.
endpoint = 'http://192.168.10.4:8080/v2.0'

# The api version of mon-api
api_version = '2_0'

# There are other kwarg options (ca files) used for http request.
# Refer to monclient.shell.py for other kwargs supported.
kwargs = {}
kwargs['token'] = '12345678'

# construct the mon client
mon_client = client.Client(api_version, endpoint, **kwargs)

# you can reference the monclient.v2_0.shell.py
# do_commands for command fields

# post a metric
dimensions = {'instance_id': '12345', 'service': 'hello'}
fields = {}
fields['name'] = 'metric1'
fields['dimensions'] = dimensions
fields['timestamp'] = time.time()
fields['value'] = 222.333
try:
    resp = mon_client.metrics.create(**fields)
except exc.HTTPException as he:
    print('HTTPException code=%s message=%s' % (he.code, he.message))
else:
    print(resp)
    print('Successfully created metric')


# metric-list
name = 'metric1'
dimensions = None
fields = {}
if name:
    fields['name'] = name
if dimensions:
    fields['dimensions'] = dimensions
try:
    body = mon_client.metrics.list(**fields)
except exc.HTTPException as he:
    print('HTTPException code=%s message=%s' % (he.code, he.message))
else:
    print(body)