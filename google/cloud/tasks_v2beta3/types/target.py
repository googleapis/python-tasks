# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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

import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.tasks.v2beta3",
    manifest={
        "HttpMethod",
        "HttpRequest",
        "AppEngineHttpQueue",
        "AppEngineHttpRequest",
        "AppEngineRouting",
        "OAuthToken",
        "OidcToken",
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
    PATCH = 6
    OPTIONS = 7


class HttpRequest(proto.Message):
    r"""HTTP request.

    The task will be pushed to the worker as an HTTP request. If the
    worker or the redirected worker acknowledges the task by returning a
    successful HTTP response code ([``200`` - ``299``]), the task will
    be removed from the queue. If any other HTTP response code is
    returned or no response is received, the task will be retried
    according to the following:

    -  User-specified throttling: [retry
       configuration][google.cloud.tasks.v2beta3.Queue.retry_config],
       [rate limits][google.cloud.tasks.v2beta3.Queue.rate_limits], and
       the [queue's state][google.cloud.tasks.v2beta3.Queue.state].

    -  System throttling: To prevent the worker from overloading, Cloud
       Tasks may temporarily reduce the queue's effective rate.
       User-specified settings will not be changed.

    System throttling happens because:

    -  Cloud Tasks backs off on all errors. Normally the backoff
       specified in [rate
       limits][google.cloud.tasks.v2beta3.Queue.rate_limits] will be
       used. But if the worker returns ``429`` (Too Many Requests),
       ``503`` (Service Unavailable), or the rate of errors is high,
       Cloud Tasks will use a higher backoff rate. The retry specified
       in the ``Retry-After`` HTTP response header is considered.

    -  To prevent traffic spikes and to smooth sudden increases in
       traffic, dispatches ramp up slowly when the queue is newly
       created or idle and if large numbers of tasks suddenly become
       available to dispatch (due to spikes in create task rates, the
       queue being unpaused, or many tasks that are scheduled at the
       same time).

    Attributes:
        url (str):
            Required. The full url path that the request will be sent
            to.

            This string must begin with either "http://" or "https://".
            Some examples are: ``http://acme.com`` and
            ``https://acme.com/sales:8080``. Cloud Tasks will encode
            some characters for safety and compatibility. The maximum
            allowed URL length is 2083 characters after encoding.

            The ``Location`` header response from a redirect response
            [``300`` - ``399``] may be followed. The redirect is not
            counted as a separate attempt.
        http_method (~.target.HttpMethod):
            The HTTP method to use for the request. The
            default is POST.
        headers (Sequence[~.target.HttpRequest.HeadersEntry]):
            HTTP request headers.

            This map contains the header field names and values. Headers
            can be set when the [task is
            created][google.cloud.tasks.v2beta3.CloudTasks.CreateTask].

            These headers represent a subset of the headers that will
            accompany the task's HTTP request. Some HTTP request headers
            will be ignored or replaced.

            A partial list of headers that will be ignored or replaced
            is:

            -  Host: This will be computed by Cloud Tasks and derived
               from
               [HttpRequest.url][google.cloud.tasks.v2beta3.HttpRequest.url].
            -  Content-Length: This will be computed by Cloud Tasks.
            -  User-Agent: This will be set to ``"Google-Cloud-Tasks"``.
            -  X-Google-\*: Google use only.
            -  X-AppEngine-\*: Google use only.

            ``Content-Type`` won't be set by Cloud Tasks. You can
            explicitly set ``Content-Type`` to a media type when the
            [task is
            created][google.cloud.tasks.v2beta3.CloudTasks.CreateTask].
            For example, ``Content-Type`` can be set to
            ``"application/octet-stream"`` or ``"application/json"``.

            Headers which can have multiple values (according to
            RFC2616) can be specified using comma-separated values.

            The size of the headers must be less than 80KB.
        body (bytes):
            HTTP request body.

            A request body is allowed only if the [HTTP
            method][google.cloud.tasks.v2beta3.HttpRequest.http_method]
            is POST, PUT, or PATCH. It is an error to set body on a task
            with an incompatible
            [HttpMethod][google.cloud.tasks.v2beta3.HttpMethod].
        oauth_token (~.target.OAuthToken):
            If specified, an `OAuth
            token <https://developers.google.com/identity/protocols/OAuth2>`__
            will be generated and attached as an ``Authorization``
            header in the HTTP request.

            This type of authorization should generally only be used
            when calling Google APIs hosted on \*.googleapis.com.
        oidc_token (~.target.OidcToken):
            If specified, an
            `OIDC <https://developers.google.com/identity/protocols/OpenIDConnect>`__
            token will be generated and attached as an ``Authorization``
            header in the HTTP request.

            This type of authorization can be used for many scenarios,
            including calling Cloud Run, or endpoints where you intend
            to validate the token yourself.
    """

    url = proto.Field(proto.STRING, number=1)

    http_method = proto.Field(proto.ENUM, number=2, enum="HttpMethod",)

    headers = proto.MapField(proto.STRING, proto.STRING, number=3)

    body = proto.Field(proto.BYTES, number=4)

    oauth_token = proto.Field(
        proto.MESSAGE, number=5, oneof="authorization_header", message="OAuthToken",
    )

    oidc_token = proto.Field(
        proto.MESSAGE, number=6, oneof="authorization_header", message="OidcToken",
    )


class AppEngineHttpQueue(proto.Message):
    r"""App Engine HTTP queue.

    The task will be delivered to the App Engine application hostname
    specified by its
    [AppEngineHttpQueue][google.cloud.tasks.v2beta3.AppEngineHttpQueue]
    and
    [AppEngineHttpRequest][google.cloud.tasks.v2beta3.AppEngineHttpRequest].
    The documentation for
    [AppEngineHttpRequest][google.cloud.tasks.v2beta3.AppEngineHttpRequest]
    explains how the task's host URL is constructed.

    Using
    [AppEngineHttpQueue][google.cloud.tasks.v2beta3.AppEngineHttpQueue]
    requires
    ```appengine.applications.get`` <https://cloud.google.com/appengine/docs/admin-api/access-control>`__
    Google IAM permission for the project and the following scope:

    ``https://www.googleapis.com/auth/cloud-platform``

    Attributes:
        app_engine_routing_override (~.target.AppEngineRouting):
            Overrides for the [task-level
            app_engine_routing][google.cloud.tasks.v2beta3.AppEngineHttpRequest.app_engine_routing].

            If set, ``app_engine_routing_override`` is used for all
            tasks in the queue, no matter what the setting is for the
            [task-level
            app_engine_routing][google.cloud.tasks.v2beta3.AppEngineHttpRequest.app_engine_routing].
    """

    app_engine_routing_override = proto.Field(
        proto.MESSAGE, number=1, message="AppEngineRouting",
    )


class AppEngineHttpRequest(proto.Message):
    r"""App Engine HTTP request.

    The message defines the HTTP request that is sent to an App Engine
    app when the task is dispatched.

    Using
    [AppEngineHttpRequest][google.cloud.tasks.v2beta3.AppEngineHttpRequest]
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

    The [AppEngineRouting][google.cloud.tasks.v2beta3.AppEngineRouting]
    used to construct the URL that the task is delivered to can be set
    at the queue-level or task-level:

    -  If set,
       [app_engine_routing_override][google.cloud.tasks.v2beta3.AppEngineHttpQueue.app_engine_routing_override]
       is used for all tasks in the queue, no matter what the setting is
       for the [task-level
       app_engine_routing][google.cloud.tasks.v2beta3.AppEngineHttpRequest.app_engine_routing].

    The ``url`` that the task will be sent to is:

    -  ``url =``
       [host][google.cloud.tasks.v2beta3.AppEngineRouting.host] ``+``
       [relative_uri][google.cloud.tasks.v2beta3.AppEngineHttpRequest.relative_uri]

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
    [deadline][google.cloud.tasks.v2beta3.Task.dispatch_deadline].
    Failed tasks will be retried according to the [retry
    configuration][google.cloud.tasks.v2beta3.Queue.retry_config].
    ``503`` (Service Unavailable) is considered an App Engine system
    error instead of an application error and will cause Cloud Tasks'
    traffic congestion control to temporarily throttle the queue's
    dispatches. Unlike other types of task targets, a ``429`` (Too Many
    Requests) response from an app handler does not cause traffic
    congestion control to throttle the queue.

    Attributes:
        http_method (~.target.HttpMethod):
            The HTTP method to use for the request. The default is POST.

            The app's request handler for the task's target URL must be
            able to handle HTTP requests with this http_method,
            otherwise the task attempt fails with error code 405 (Method
            Not Allowed). See `Writing a push task request
            handler <https://cloud.google.com/appengine/docs/java/taskqueue/push/creating-handlers#writing_a_push_task_request_handler>`__
            and the App Engine documentation for your runtime on `How
            Requests are
            Handled <https://cloud.google.com/appengine/docs/standard/python3/how-requests-are-handled>`__.
        app_engine_routing (~.target.AppEngineRouting):
            Task-level setting for App Engine routing.

            If set,
            [app_engine_routing_override][google.cloud.tasks.v2beta3.AppEngineHttpQueue.app_engine_routing_override]
            is used for all tasks in the queue, no matter what the
            setting is for the [task-level
            app_engine_routing][google.cloud.tasks.v2beta3.AppEngineHttpRequest.app_engine_routing].
        relative_uri (str):
            The relative URI.
            The relative URI must begin with "/" and must be
            a valid HTTP relative URI. It can contain a path
            and query string arguments. If the relative URI
            is empty, then the root path "/" will be used.
            No spaces are allowed, and the maximum length
            allowed is 2083 characters.
        headers (Sequence[~.target.AppEngineHttpRequest.HeadersEntry]):
            HTTP request headers.

            This map contains the header field names and values. Headers
            can be set when the [task is
            created][google.cloud.tasks.v2beta3.CloudTasks.CreateTask].
            Repeated headers are not supported but a header value can
            contain commas.

            Cloud Tasks sets some headers to default values:

            -  ``User-Agent``: By default, this header is
               ``"AppEngine-Google; (+http://code.google.com/appengine)"``.
               This header can be modified, but Cloud Tasks will append
               ``"AppEngine-Google; (+http://code.google.com/appengine)"``
               to the modified ``User-Agent``.

            If the task has a
            [body][google.cloud.tasks.v2beta3.AppEngineHttpRequest.body],
            Cloud Tasks sets the following headers:

            -  ``Content-Type``: By default, the ``Content-Type`` header
               is set to ``"application/octet-stream"``. The default can
               be overridden by explicitly setting ``Content-Type`` to a
               particular media type when the [task is
               created][google.cloud.tasks.v2beta3.CloudTasks.CreateTask].
               For example, ``Content-Type`` can be set to
               ``"application/json"``.
            -  ``Content-Length``: This is computed by Cloud Tasks. This
               value is output only. It cannot be changed.

            The headers below cannot be set or overridden:

            -  ``Host``
            -  ``X-Google-\*``
            -  ``X-AppEngine-\*``

            In addition, Cloud Tasks sets some headers when the task is
            dispatched, such as headers containing information about the
            task; see `request
            headers <https://cloud.google.com/tasks/docs/creating-appengine-handlers#reading_request_headers>`__.
            These headers are set only when the task is dispatched, so
            they are not visible when the task is returned in a Cloud
            Tasks response.

            Although there is no specific limit for the maximum number
            of headers or the size, there is a limit on the maximum size
            of the [Task][google.cloud.tasks.v2beta3.Task]. For more
            information, see the
            [CreateTask][google.cloud.tasks.v2beta3.CloudTasks.CreateTask]
            documentation.
        body (bytes):
            HTTP request body.

            A request body is allowed only if the HTTP method is POST or
            PUT. It is an error to set a body on a task with an
            incompatible
            [HttpMethod][google.cloud.tasks.v2beta3.HttpMethod].
    """

    http_method = proto.Field(proto.ENUM, number=1, enum="HttpMethod",)

    app_engine_routing = proto.Field(
        proto.MESSAGE, number=2, message="AppEngineRouting",
    )

    relative_uri = proto.Field(proto.STRING, number=3)

    headers = proto.MapField(proto.STRING, proto.STRING, number=4)

    body = proto.Field(proto.BYTES, number=5)


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
            [host][google.cloud.tasks.v2beta3.AppEngineRouting.host] is
            not parsable into
            [service][google.cloud.tasks.v2beta3.AppEngineRouting.service],
            [version][google.cloud.tasks.v2beta3.AppEngineRouting.version],
            and
            [instance][google.cloud.tasks.v2beta3.AppEngineRouting.instance].
            For example, some tasks which were created using the App
            Engine SDK use a custom domain name; custom domains are not
            parsed by Cloud Tasks. If
            [host][google.cloud.tasks.v2beta3.AppEngineRouting.host] is
            not parsable, then
            [service][google.cloud.tasks.v2beta3.AppEngineRouting.service],
            [version][google.cloud.tasks.v2beta3.AppEngineRouting.version],
            and
            [instance][google.cloud.tasks.v2beta3.AppEngineRouting.instance]
            are the empty string.
        version (str):
            App version.

            By default, the task is sent to the version which is the
            default version when the task is attempted.

            For some queues or tasks which were created using the App
            Engine Task Queue API,
            [host][google.cloud.tasks.v2beta3.AppEngineRouting.host] is
            not parsable into
            [service][google.cloud.tasks.v2beta3.AppEngineRouting.service],
            [version][google.cloud.tasks.v2beta3.AppEngineRouting.version],
            and
            [instance][google.cloud.tasks.v2beta3.AppEngineRouting.instance].
            For example, some tasks which were created using the App
            Engine SDK use a custom domain name; custom domains are not
            parsed by Cloud Tasks. If
            [host][google.cloud.tasks.v2beta3.AppEngineRouting.host] is
            not parsable, then
            [service][google.cloud.tasks.v2beta3.AppEngineRouting.service],
            [version][google.cloud.tasks.v2beta3.AppEngineRouting.version],
            and
            [instance][google.cloud.tasks.v2beta3.AppEngineRouting.instance]
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

            The host is constructed from the domain name of the app
            associated with the queue's project ID (for example
            .appspot.com), and the
            [service][google.cloud.tasks.v2beta3.AppEngineRouting.service],
            [version][google.cloud.tasks.v2beta3.AppEngineRouting.version],
            and
            [instance][google.cloud.tasks.v2beta3.AppEngineRouting.instance].
            Tasks which were created using the App Engine SDK might have
            a custom domain name.

            For more information, see `How Requests are
            Routed <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`__.
    """

    service = proto.Field(proto.STRING, number=1)

    version = proto.Field(proto.STRING, number=2)

    instance = proto.Field(proto.STRING, number=3)

    host = proto.Field(proto.STRING, number=4)


class OAuthToken(proto.Message):
    r"""Contains information needed for generating an `OAuth
    token <https://developers.google.com/identity/protocols/OAuth2>`__.
    This type of authorization should generally only be used when
    calling Google APIs hosted on \*.googleapis.com.

    Attributes:
        service_account_email (str):
            `Service account
            email <https://cloud.google.com/iam/docs/service-accounts>`__
            to be used for generating OAuth token. The service account
            must be within the same project as the queue. The caller
            must have iam.serviceAccounts.actAs permission for the
            service account.
        scope (str):
            OAuth scope to be used for generating OAuth
            access token. If not specified,
            "https://www.googleapis.com/auth/cloud-platform"
            will be used.
    """

    service_account_email = proto.Field(proto.STRING, number=1)

    scope = proto.Field(proto.STRING, number=2)


class OidcToken(proto.Message):
    r"""Contains information needed for generating an `OpenID Connect
    token <https://developers.google.com/identity/protocols/OpenIDConnect>`__.
    This type of authorization can be used for many scenarios, including
    calling Cloud Run, or endpoints where you intend to validate the
    token yourself.

    Attributes:
        service_account_email (str):
            `Service account
            email <https://cloud.google.com/iam/docs/service-accounts>`__
            to be used for generating OIDC token. The service account
            must be within the same project as the queue. The caller
            must have iam.serviceAccounts.actAs permission for the
            service account.
        audience (str):
            Audience to be used when generating OIDC
            token. If not specified, the URI specified in
            target will be used.
    """

    service_account_email = proto.Field(proto.STRING, number=1)

    audience = proto.Field(proto.STRING, number=2)


__all__ = tuple(sorted(__protobuf__.manifest))
