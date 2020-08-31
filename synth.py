# Copyright 2018 Google LLC
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

"""This script is used to synthesize generated parts of this library."""

import synthtool as s
import synthtool.gcp as gcp
from synthtool.languages import python
import logging

logging.basicConfig(level=logging.DEBUG)

gapic = gcp.GAPICBazel()
common = gcp.CommonTemplates()
excludes = ["README.rst", "setup.py", "nox*.py", "docs/index.rst"]

# ----------------------------------------------------------------------------
# Generate tasks GAPIC layer
# ----------------------------------------------------------------------------
for version in ["v2beta2", "v2beta3", "v2"]:
    library = gapic.py_library(
        service="tasks",
        version=version,
        bazel_target=f"//google/cloud/tasks/{version}:tasks-{version}-py",
        include_protos=True,
    )

    s.copy(library, excludes=excludes)

    s.replace(
        f"google/cloud/tasks_{version}/gapic/cloud_tasks_client.py",
        "(Google IAM .*?_) ",
        "\g<1>_ ",
    )

    # Issues with Anonymous ('__') links. Change to named.
    s.replace(f"google/cloud/tasks_{version}/proto/*.py", ">`__", ">`_")

# Wrapped link fails due to space in link (v2beta2)
s.replace(
    "google/cloud/tasks_v2beta2/proto/queue_pb2.py",
    "(in queue.yaml/xml) <\n\s+",
    "\g<1>\n          <",
)

# Wrapped link fails due to newline (v2)
s.replace(
    "google/cloud/tasks_v2/proto/queue_pb2.py",
    """#retry_parameters>
          `__\.""",
    "#retry_parameters>`__.",
)

# Restore updated example from PR #7025.
s.replace(
    "google/cloud/tasks_v2beta3/gapic/cloud_tasks_client.py",
    ">>> # TODO: Initialize `queue`:",
    ">>> # Initialize `queue`:",
)
s.replace(
    "google/cloud/tasks_v2beta3/gapic/cloud_tasks_client.py",
    "^(\s+)>>> queue = {}\n",
    "\g<1>>>> queue = {\n"
    "\g<1>...     # The fully qualified path to the queue\n"
    "\g<1>...     'name': client.queue_path('[PROJECT]', '[LOCATION]', '[NAME]'),\n"
    "\g<1>...     'app_engine_http_queue': {\n"
    "\g<1>...         'app_engine_routing_override': {\n"
    "\g<1>...             # The App Engine service that will receive the tasks.\n"
    "\g<1>...             'service': 'default',\n"
    "\g<1>...         },\n"
    "\g<1>...     },\n"
    "\g<1>... }\n",
)

# Fix enum docstring references
s.replace(
    "google/cloud/**/cloud_tasks_client.py",
    "types\.View",
    "enums.Task.View")

# Change wording of optional params to disambiguate
# client library request methods from Cloud Task requests
s.replace("google/cloud/**/*.py",
"""            retry \(Optional\[google\.api_core\.retry\.Retry\]\):  A retry object used
                to retry requests\. If ``None`` is specified, requests will
                be retried using a default configuration\.
            timeout \(Optional\[float\]\): The amount of time, in seconds, to wait
                for the request to complete\. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt\.
            metadata \(Optional\[Sequence\[Tuple\[str, str\]\]\]\): Additional metadata
                that is provided to the method\.

""",
"""            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

""")

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library(cov_level=86, samples=True)
s.move(templated_files)

# ----------------------------------------------------------------------------
# Samples templates
# ----------------------------------------------------------------------------
python.py_samples(skip_readmes=True)

# TODO(busunkim): Use latest sphinx after microgenerator transition
s.replace("noxfile.py", """['"]sphinx['"]""", '"sphinx<3.0.0"')

# Escape '_' in docstrings
s.replace(
   "google/cloud/**/*_pb2.py",
   """\_$""",
   """\_""",
)

s.shell.run(["nox", "-s", "blacken"], hide_output=False)
