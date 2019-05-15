# Copyright 2019 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import create_http_task_with_token

TEST_PROJECT_ID = os.getenv('GCLOUD_PROJECT')
TEST_LOCATION = os.getenv('TEST_QUEUE_LOCATION', 'us-central1')
TEST_QUEUE_NAME = os.getenv('TEST_QUEUE_NAME', 'my-queue')
TEST_SERVICE_ACCOUNT = (
    'test-run-invoker@python-docs-samples-tests.iam.gserviceaccount.com')


def test_create_http_task_with_token():
    url = 'https://example.com/task_handler'
    result = create_http_task_with_token.create_http_task(TEST_PROJECT_ID,
                                                          TEST_QUEUE_NAME,
                                                          TEST_LOCATION,
                                                          url,
                                                          TEST_SERVICE_ACCOUNT)
    assert TEST_QUEUE_NAME in result.name
