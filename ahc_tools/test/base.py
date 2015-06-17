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

import unittest

from oslo_config import cfg

# Import configuration options
from ahc_tools import conf  # noqa

CONF = cfg.CONF


class BaseTest(unittest.TestCase):
    def setUp(self):
        super(BaseTest, self).setUp()
        CONF.reset()
        for group in ('ironic', 'swift'):
            CONF.register_group(cfg.OptGroup(group))
