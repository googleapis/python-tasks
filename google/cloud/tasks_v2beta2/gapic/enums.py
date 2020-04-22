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
    The HTTP method used to execute the task.

    Attributes:
      HTTP_METHOD_UNSPECIFIED (int): HTTP method unspecified
      POST (int): HTTP POST
      GET (int): HTTP GET
      HEAD (int): HTTP HEAD
      PUT (int): HTTP PUT
      DELETE (int): HTTP DELETE
    """

    HTTP_METHOD_UNSPECIFIED = 0
    POST = 1
    GET = 2
    HEAD = 3
    PUT = 4
    DELETE = 5


class Queue(object):
    class State(enum.IntEnum):
        """
        State of the queue.

        Attributes:
          STATE_UNSPECIFIED (int): Unspecified state.
          RUNNING (int): Required. The queue name. For example:
          ``projects/PROJECT_ID/location/LOCATION_ID/queues/QUEUE_ID``
          PAUSED (int): javalite_serializable
          DISABLED (int): A generic empty message that you can re-use to avoid defining
          duplicated empty messages in your APIs. A typical example is to use it
          as the request or the response type of an API method. For instance:

          ::

              service Foo {
                rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);
              }

          The JSON representation for ``Empty`` is empty JSON object ``{}``.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        PAUSED = 2
        DISABLED = 3


class Task(object):
    class View(enum.IntEnum):
        """
        ``filter`` can be used to specify a subset of tasks to lease.

        When ``filter`` is set to ``tag=<my-tag>`` then the ``response`` will
        contain only tasks whose ``tag`` is equal to ``<my-tag>``. ``<my-tag>``
        must be less than 500 characters.

        When ``filter`` is set to ``tag_function=oldest_tag()``, only tasks
        which have the same tag as the task with the oldest ``schedule_time``
        will be returned.

        Grammar Syntax:

        -  ``filter = "tag=" tag | "tag_function=" function``

        -  ``tag = string``

        -  ``function = "oldest_tag()"``

        The ``oldest_tag()`` function returns tasks which have the same tag as
        the oldest task (ordered by schedule time).

        SDK compatibility: Although the SDK allows tags to be either string or
        `bytes <https://cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/taskqueue/TaskOptions.html#tag-byte:A->`__,
        only UTF-8 encoded tags can be used in Cloud Tasks. Tag which aren't
        UTF-8 encoded can't be used in the ``filter`` and the task's ``tag``
        will be displayed as empty in Cloud Tasks.

        Attributes:
          VIEW_UNSPECIFIED (int): Unspecified. Defaults to BASIC.
          BASIC (int): Request message for ``DeleteQueue``.
          FULL (int): JSON name of this field. The value is set by protocol compiler. If
          the user has set a "json_name" option on this field, that option's value
          will be used. Otherwise, it's deduced from the field's name by
          converting it to camelCase.
        """

        VIEW_UNSPECIFIED = 0
        BASIC = 1
        FULL = 2
