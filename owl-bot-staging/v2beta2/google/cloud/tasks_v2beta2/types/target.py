# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
#
from typing import MutableMapping, MutableSequence

import proto  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.tasks.v2beta2',
    manifest={
        'HttpMethod',
        'PullTarget',
        'PullMessage',
        'AppEngineHttpTarget',
        'AppEngineHttpRequest',
        'AppEngineRouting',
    },
)


class HttpMethod(proto.Enum):
    r"""The HTTP method used to execute the task."""
    HTTP_METHOD_UNSPECIFIED = 0
    POST = 1
    GET = 2
    HEAD = 3
    PUT = 4
    DELETE = 5


class PullTarget(proto.Message):
    r"""Pull target.
    """


class PullMessage(proto.Message):
    r"""The pull message contains data that can be used by the caller of
    [LeaseTasks][google.cloud.tasks.v2beta2.CloudTasks.LeaseTasks] to
    process the task.

    This proto can only be used for tasks in a queue which has
    [pull_target][google.cloud.tasks.v2beta2.Queue.pull_target] set.

    Attributes:
        payload (bytes):
            A data payload consumed by the worker to
            execute the task.
        tag (str):
            The task's tag.

            Tags allow similar tasks to be processed in a batch. If you
            label tasks with a tag, your worker can [lease
            tasks][google.cloud.tasks.v2beta2.CloudTasks.LeaseTasks]
            with the same tag using
            [filter][google.cloud.tasks.v2beta2.LeaseTasksRequest.filter].
            For example, if you want to aggregate the events associated
            with a specific user once a day, you could tag tasks with
            the user ID.

            The task's tag can only be set when the [task is
            created][google.cloud.tasks.v2beta2.CloudTasks.CreateTask].

            The tag must be less than 500 characters.

            SDK compatibility: Although the SDK allows tags to be either
            string or
            `bytes <https://cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/taskqueue/TaskOptions.html#tag-byte:A->`__,
            only UTF-8 encoded tags can be used in Cloud Tasks. If a tag
            isn't UTF-8 encoded, the tag will be empty when the task is
            returned by Cloud Tasks.
    """

    payload: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    tag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AppEngineHttpTarget(proto.Message):
    r"""App Engine HTTP target.

    The task will be delivered to the App Engine application hostname
    specified by its
    [AppEngineHttpTarget][google.cloud.tasks.v2beta2.AppEngineHttpTarget]
    and
    [AppEngineHttpRequest][google.cloud.tasks.v2beta2.AppEngineHttpRequest].
    The documentation for
    [AppEngineHttpRequest][google.cloud.tasks.v2beta2.AppEngineHttpRequest]
    explains how the task's host URL is constructed.

    Using
    [AppEngineHttpTarget][google.cloud.tasks.v2beta2.AppEngineHttpTarget]
    requires
    ```appengine.applications.get`` <https://cloud.google.com/appengine/docs/admin-api/access-control>`__
    Google IAM permission for the project and the following scope:

    ``https://www.googleapis.com/auth/cloud-platform``

    Attributes:
        app_engine_routing_override (google.cloud.tasks_v2beta2.types.AppEngineRouting):
            Overrides for the [task-level
            app_engine_routing][google.cloud.tasks.v2beta2.AppEngineHttpRequest.app_engine_routing].

            If set, ``app_engine_routing_override`` is used for all
            tasks in the queue, no matter what the setting is for the
            [task-level
            app_engine_routing][google.cloud.tasks.v2beta2.AppEngineHttpRequest.app_engine_routing].
    """

    app_engine_routing_override: 'AppEngineRouting' = proto.Field(
        proto.MESSAGE,
        number=1,
        message='AppEngineRouting',
    )


class AppEngineHttpRequest(proto.Message):
    r"""App Engine HTTP request.

    The message defines the HTTP request that is sent to an App Engine
    app when the task is dispatched.

    This proto can only be used for tasks in a queue which has
    [app_engine_http_target][google.cloud.tasks.v2beta2.Queue.app_engine_http_target]
    set.

    Using
    [AppEngineHttpRequest][google.cloud.tasks.v2beta2.AppEngineHttpRequest]
    requires
    ```appengine.applications.get`` <https://cloud.google.com/appengine/docs/admin-api/access-control>`__
    Google IAM permission for the project and the following scope:

    ``https://www.googleapis.com/auth/cloud-platform``

    The task will be delivered to the App Engine app which belongs to
    the same project as the queue. For more information, see `How
    Requests are
    Routed <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`__
    and how routing is affected by `dispatch
    files <https://cloud.google.com/appengine/docs/python/config/dispatchref>`__.
    Traffic is encrypted during transport and never leaves Google
    datacenters. Because this traffic is carried over a communication
    mechanism internal to Google, you cannot explicitly set the protocol
    (for example, HTTP or HTTPS). The request to the handler, however,
    will appear to have used the HTTP protocol.

    The [AppEngineRouting][google.cloud.tasks.v2beta2.AppEngineRouting]
    used to construct the URL that the task is delivered to can be set
    at the queue-level or task-level:

    -  If set,
       [app_engine_routing_override][google.cloud.tasks.v2beta2.AppEngineHttpTarget.app_engine_routing_override]
       is used for all tasks in the queue, no matter what the setting is
       for the [task-level
       app_engine_routing][google.cloud.tasks.v2beta2.AppEngineHttpRequest.app_engine_routing].

    The ``url`` that the task will be sent to is:

    -  ``url =``
       [host][google.cloud.tasks.v2beta2.AppEngineRouting.host] ``+``
       [relative_url][google.cloud.tasks.v2beta2.AppEngineHttpRequest.relative_url]

    Tasks can be dispatched to secure app handlers, unsecure app
    handlers, and URIs restricted with
    ```login: admin`` <https://cloud.google.com/appengine/docs/standard/python/config/appref>`__.
    Because tasks are not run as any user, they cannot be dispatched to
    URIs restricted with
    ```login: required`` <https://cloud.google.com/appengine/docs/standard/python/config/appref>`__
    Task dispatches also do not follow redirects.

    The task attempt has succeeded if the app's request handler returns
    an HTTP response code in the range [``200`` - ``299``]. The task
    attempt has failed if the app's handler returns a non-2xx response
    code or Cloud Tasks does not receive response before the
    [deadline][Task.dispatch_deadline]. Failed tasks will be retried
    according to the [retry
    configuration][google.cloud.tasks.v2beta2.Queue.retry_config].
    ``503`` (Service Unavailable) is considered an App Engine system
    error instead of an application error and will cause Cloud Tasks'
    traffic congestion control to temporarily throttle the queue's
    dispatches. Unlike other types of task targets, a ``429`` (Too Many
    Requests) response from an app handler does not cause traffic
    congestion control to throttle the queue.

    Attributes:
        http_method (google.cloud.tasks_v2beta2.types.HttpMethod):
            The HTTP method to use for the request. The default is POST.

            The app's request handler for the task's target URL must be
            able to handle HTTP requests with this http_method,
            otherwise the task attempt fails with error code 405 (Method
            Not Allowed). See `Writing a push task request
            handler <https://cloud.google.com/appengine/docs/java/taskqueue/push/creating-handlers#writing_a_push_task_request_handler>`__
            and the App Engine documentation for your runtime on `How
            Requests are
            Handled <https://cloud.google.com/appengine/docs/standard/python3/how-requests-are-handled>`__.
        app_engine_routing (google.cloud.tasks_v2beta2.types.AppEngineRouting):
            Task-level setting for App Engine routing.

            If set,
            [app_engine_routing_override][google.cloud.tasks.v2beta2.AppEngineHttpTarget.app_engine_routing_override]
            is used for all tasks in the queue, no matter what the
            setting is for the [task-level
            app_engine_routing][google.cloud.tasks.v2beta2.AppEngineHttpRequest.app_engine_routing].
        relative_url (str):
            The relative URL.
            The relative URL must begin with "/" and must be
            a valid HTTP relative URL. It can contain a path
            and query string arguments. If the relative URL
            is empty, then the root path "/" will be used.
            No spaces are allowed, and the maximum length
            allowed is 2083 characters.
        headers (MutableMapping[str, str]):
            HTTP request headers.

            This map contains the header field names and values. Headers
            can be set when the [task is
            created][google.cloud.tasks.v2beta2.CloudTasks.CreateTask].
            Repeated headers are not supported but a header value can
            contain commas.

            Cloud Tasks sets some headers to default values:

            -  ``User-Agent``: By default, this header is
               ``"AppEngine-Google; (+http://code.google.com/appengine)"``.
               This header can be modified, but Cloud Tasks will append
               ``"AppEngine-Google; (+http://code.google.com/appengine)"``
               to the modified ``User-Agent``.

            If the task has a
            [payload][google.cloud.tasks.v2beta2.AppEngineHttpRequest.payload],
            Cloud Tasks sets the following headers:

            -  ``Content-Type``: By default, the ``Content-Type`` header
               is set to ``"application/octet-stream"``. The default can
               be overridden by explicitly setting ``Content-Type`` to a
               particular media type when the [task is
               created][google.cloud.tasks.v2beta2.CloudTasks.CreateTask].
               For example, ``Content-Type`` can be set to
               ``"application/json"``.
            -  ``Content-Length``: This is computed by Cloud Tasks. This
               value is output only. It cannot be changed.

            The headers below cannot be set or overridden:

            -  ``Host``
            -  ``X-Google-*``
            -  ``X-AppEngine-*``

            In addition, Cloud Tasks sets some headers when the task is
            dispatched, such as headers containing information about the
            task; see `request
            headers <https://cloud.google.com/appengine/docs/python/taskqueue/push/creating-handlers#reading_request_headers>`__.
            These headers are set only when the task is dispatched, so
            they are not visible when the task is returned in a Cloud
            Tasks response.

            Although there is no specific limit for the maximum number
            of headers or the size, there is a limit on the maximum size
            of the [Task][google.cloud.tasks.v2beta2.Task]. For more
            information, see the
            [CreateTask][google.cloud.tasks.v2beta2.CloudTasks.CreateTask]
            documentation.
        payload (bytes):
            Payload.

            The payload will be sent as the HTTP message body. A message
            body, and thus a payload, is allowed only if the HTTP method
            is POST or PUT. It is an error to set a data payload on a
            task with an incompatible
            [HttpMethod][google.cloud.tasks.v2beta2.HttpMethod].
    """

    http_method: 'HttpMethod' = proto.Field(
        proto.ENUM,
        number=1,
        enum='HttpMethod',
    )
    app_engine_routing: 'AppEngineRouting' = proto.Field(
        proto.MESSAGE,
        number=2,
        message='AppEngineRouting',
    )
    relative_url: str = proto.Field(
        proto.STRING,
        number=3,
    )
    headers: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    payload: bytes = proto.Field(
        proto.BYTES,
        number=5,
    )


class AppEngineRouting(proto.Message):
    r"""App Engine Routing.

    Defines routing characteristics specific to App Engine - service,
    version, and instance.

    For more information about services, versions, and instances see `An
    Overview of App
    Engine <https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine>`__,
    `Microservices Architecture on Google App
    Engine <https://cloud.google.com/appengine/docs/python/microservices-on-app-engine>`__,
    `App Engine Standard request
    routing <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`__,
    and `App Engine Flex request
    routing <https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed>`__.

    Attributes:
        service (str):
            App service.

            By default, the task is sent to the service which is the
            default service when the task is attempted.

            For some queues or tasks which were created using the App
            Engine Task Queue API,
            [host][google.cloud.tasks.v2beta2.AppEngineRouting.host] is
            not parsable into
            [service][google.cloud.tasks.v2beta2.AppEngineRouting.service],
            [version][google.cloud.tasks.v2beta2.AppEngineRouting.version],
            and
            [instance][google.cloud.tasks.v2beta2.AppEngineRouting.instance].
            For example, some tasks which were created using the App
            Engine SDK use a custom domain name; custom domains are not
            parsed by Cloud Tasks. If
            [host][google.cloud.tasks.v2beta2.AppEngineRouting.host] is
            not parsable, then
            [service][google.cloud.tasks.v2beta2.AppEngineRouting.service],
            [version][google.cloud.tasks.v2beta2.AppEngineRouting.version],
            and
            [instance][google.cloud.tasks.v2beta2.AppEngineRouting.instance]
            are the empty string.
        version (str):
            App version.

            By default, the task is sent to the version which is the
            default version when the task is attempted.

            For some queues or tasks which were created using the App
            Engine Task Queue API,
            [host][google.cloud.tasks.v2beta2.AppEngineRouting.host] is
            not parsable into
            [service][google.cloud.tasks.v2beta2.AppEngineRouting.service],
            [version][google.cloud.tasks.v2beta2.AppEngineRouting.version],
            and
            [instance][google.cloud.tasks.v2beta2.AppEngineRouting.instance].
            For example, some tasks which were created using the App
            Engine SDK use a custom domain name; custom domains are not
            parsed by Cloud Tasks. If
            [host][google.cloud.tasks.v2beta2.AppEngineRouting.host] is
            not parsable, then
            [service][google.cloud.tasks.v2beta2.AppEngineRouting.service],
            [version][google.cloud.tasks.v2beta2.AppEngineRouting.version],
            and
            [instance][google.cloud.tasks.v2beta2.AppEngineRouting.instance]
            are the empty string.
        instance (str):
            App instance.

            By default, the task is sent to an instance which is
            available when the task is attempted.

            Requests can only be sent to a specific instance if `manual
            scaling is used in App Engine
            Standard <https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine?hl=en_US#scaling_types_and_instance_classes>`__.
            App Engine Flex does not support instances. For more
            information, see `App Engine Standard request
            routing <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`__
            and `App Engine Flex request
            routing <https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed>`__.
        host (str):
            Output only. The host that the task is sent to.

            For more information, see `How Requests are
            Routed <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`__.

            The host is constructed as:

            -  ``host = [application_domain_name]``\
               ``| [service] + '.' + [application_domain_name]``\
               ``| [version] + '.' + [application_domain_name]``\
               ``| [version_dot_service]+ '.' + [application_domain_name]``\
               ``| [instance] + '.' + [application_domain_name]``\
               ``| [instance_dot_service] + '.' + [application_domain_name]``\
               ``| [instance_dot_version] + '.' + [application_domain_name]``\
               ``| [instance_dot_version_dot_service] + '.' + [application_domain_name]``

            -  ``application_domain_name`` = The domain name of the app,
               for example .appspot.com, which is associated with the
               queue's project ID. Some tasks which were created using
               the App Engine SDK use a custom domain name.

            -  ``service =``
               [service][google.cloud.tasks.v2beta2.AppEngineRouting.service]

            -  ``version =``
               [version][google.cloud.tasks.v2beta2.AppEngineRouting.version]

            -  ``version_dot_service =``
               [version][google.cloud.tasks.v2beta2.AppEngineRouting.version]
               ``+ '.' +``
               [service][google.cloud.tasks.v2beta2.AppEngineRouting.service]

            -  ``instance =``
               [instance][google.cloud.tasks.v2beta2.AppEngineRouting.instance]

            -  ``instance_dot_service =``
               [instance][google.cloud.tasks.v2beta2.AppEngineRouting.instance]
               ``+ '.' +``
               [service][google.cloud.tasks.v2beta2.AppEngineRouting.service]

            -  ``instance_dot_version =``
               [instance][google.cloud.tasks.v2beta2.AppEngineRouting.instance]
               ``+ '.' +``
               [version][google.cloud.tasks.v2beta2.AppEngineRouting.version]

            -  ``instance_dot_version_dot_service =``
               [instance][google.cloud.tasks.v2beta2.AppEngineRouting.instance]
               ``+ '.' +``
               [version][google.cloud.tasks.v2beta2.AppEngineRouting.version]
               ``+ '.' +``
               [service][google.cloud.tasks.v2beta2.AppEngineRouting.service]

            If
            [service][google.cloud.tasks.v2beta2.AppEngineRouting.service]
            is empty, then the task will be sent to the service which is
            the default service when the task is attempted.

            If
            [version][google.cloud.tasks.v2beta2.AppEngineRouting.version]
            is empty, then the task will be sent to the version which is
            the default version when the task is attempted.

            If
            [instance][google.cloud.tasks.v2beta2.AppEngineRouting.instance]
            is empty, then the task will be sent to an instance which is
            available when the task is attempted.

            If
            [service][google.cloud.tasks.v2beta2.AppEngineRouting.service],
            [version][google.cloud.tasks.v2beta2.AppEngineRouting.version],
            or
            [instance][google.cloud.tasks.v2beta2.AppEngineRouting.instance]
            is invalid, then the task will be sent to the default
            version of the default service when the task is attempted.
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=3,
    )
    host: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
