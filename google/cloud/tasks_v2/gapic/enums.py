# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wrappers for protocol buffer enum types."""

import enum


class HttpMethod(enum.IntEnum):
    """
    The HTTP method used to deliver the task.

    Attributes:
      HTTP_METHOD_UNSPECIFIED (int): HTTP method unspecified
      POST (int): HTTP POST
      GET (int): HTTP GET
      HEAD (int): HTTP HEAD
      PUT (int): HTTP PUT
      DELETE (int): HTTP DELETE
      PATCH (int): HTTP PATCH
      OPTIONS (int): HTTP OPTIONS
    """

    HTTP_METHOD_UNSPECIFIED = 0
    POST = 1
    GET = 2
    HEAD = 3
    PUT = 4
    DELETE = 5
    PATCH = 6
    OPTIONS = 7


class Queue(object):
    class State(enum.IntEnum):
        """
        State of the queue.

        Attributes:
          STATE_UNSPECIFIED (int): Unspecified state.
          RUNNING (int): Request message for ``UpdateQueue``.
          PAUSED (int): Tasks are paused by the user. If the queue is paused then Cloud
          Tasks will stop delivering tasks from it, but more tasks can
          still be added to it by the user.
          DISABLED (int): Protocol Buffers - Google's data interchange format Copyright 2008
          Google Inc. All rights reserved.
          https://developers.google.com/protocol-buffers/

          Redistribution and use in source and binary forms, with or without
          modification, are permitted provided that the following conditions are
          met:

          ::

              * Redistributions of source code must retain the above copyright

          notice, this list of conditions and the following disclaimer. \*
          Redistributions in binary form must reproduce the above copyright
          notice, this list of conditions and the following disclaimer in the
          documentation and/or other materials provided with the distribution. \*
          Neither the name of Google Inc. nor the names of its contributors may be
          used to endorse or promote products derived from this software without
          specific prior written permission.

          THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
          IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
          TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
          PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
          OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
          EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
          PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
          PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
          LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
          NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
          SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        PAUSED = 2
        DISABLED = 3


class Task(object):
    class View(enum.IntEnum):
        """
        The plural name used in the resource name, such as 'projects' for
        the name of 'projects/{project}'. It is the same concept of the
        ``plural`` field in k8s CRD spec
        https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/

        Attributes:
          VIEW_UNSPECIFIED (int): Unspecified. Defaults to BASIC.
          BASIC (int): Output only. The last time this queue was purged.

          All tasks that were ``created`` before this time were purged.

          A queue can be purged using ``PurgeQueue``, the `App Engine Task Queue
          SDK, or the Cloud
          Console <https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/deleting-tasks-and-queues#purging_all_tasks_from_a_queue>`__.

          Purge time will be truncated to the nearest microsecond. Purge time will
          be unset if the queue has never been purged.
          FULL (int): Set true to use the old proto1 MessageSet wire format for
          extensions. This is provided for backwards-compatibility with the
          MessageSet wire format. You should not use this for any other reason:
          It's less efficient, has fewer features, and is more complicated.

          The message must be defined exactly as follows: message Foo { option
          message_set_wire_format = true; extensions 4 to max; } Note that the
          message cannot have any defined fields; MessageSets only have
          extensions.

          All extensions of your type must be singular messages; e.g. they cannot
          be int32s, enums, or repeated messages.

          Because this is an option, the above two restrictions are not enforced
          by the protocol compiler.
        """

        VIEW_UNSPECIFIED = 0
        BASIC = 1
        FULL = 2
