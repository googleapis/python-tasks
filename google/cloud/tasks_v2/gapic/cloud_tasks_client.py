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

"""Accesses the google.cloud.tasks.v2 CloudTasks API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from google.cloud.tasks_v2.gapic import cloud_tasks_client_config
from google.cloud.tasks_v2.gapic import enums
from google.cloud.tasks_v2.gapic.transports import cloud_tasks_grpc_transport
from google.cloud.tasks_v2.proto import cloudtasks_pb2
from google.cloud.tasks_v2.proto import cloudtasks_pb2_grpc
from google.cloud.tasks_v2.proto import queue_pb2
from google.cloud.tasks_v2.proto import task_pb2
from google.iam.v1 import iam_policy_pb2
from google.iam.v1 import options_pb2
from google.iam.v1 import policy_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution("google-cloud-tasks").version


class CloudTasksClient(object):
    """
    Cloud Tasks allows developers to manage the execution of background
    work in their applications.
    """

    SERVICE_ADDRESS = "cloudtasks.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.tasks.v2.CloudTasks"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            CloudTasksClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def location_path(cls, project, location):
        """Return a fully-qualified location string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}",
            project=project,
            location=location,
        )

    @classmethod
    def queue_path(cls, project, location, queue):
        """Return a fully-qualified queue string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/queues/{queue}",
            project=project,
            location=location,
            queue=queue,
        )

    @classmethod
    def task_path(cls, project, location, queue, task):
        """Return a fully-qualified task string."""
        return google.api_core.path_template.expand(
            "projects/{project}/locations/{location}/queues/{queue}/tasks/{task}",
            project=project,
            location=location,
            queue=queue,
            task=task,
        )

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.CloudTasksGrpcTransport,
                    Callable[[~.Credentials, type], ~.CloudTasksGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = cloud_tasks_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=cloud_tasks_grpc_transport.CloudTasksGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = cloud_tasks_grpc_transport.CloudTasksGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME]
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def list_queues(
        self,
        parent,
        filter_=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists queues.

        Queues are returned in lexicographical order.

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_queues(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_queues(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Updates a queue.

                This method creates the queue if it does not exist and updates the queue
                if it does exist.

                Queues created with this method allow tasks to live for a maximum of 31
                days. After a task is 31 days old, the task will be deleted regardless
                of whether it was dispatched or not.

                WARNING: Using this method may have unintended side effects if you are
                using an App Engine ``queue.yaml`` or ``queue.xml`` file to manage your
                queues. Read `Overview of Queue Management and
                queue.yaml <https://cloud.google.com/tasks/docs/queue-yaml>`__ before
                using this method.
            filter_ (str): The HTTP method to use for the request. The default is POST.

                The app's request handler for the task's target URL must be able to
                handle HTTP requests with this http_method, otherwise the task attempt
                will fail with error code 405 (Method Not Allowed). See `Writing a push
                task request
                handler <https://cloud.google.com/appengine/docs/java/taskqueue/push/creating-handlers#writing_a_push_task_request_handler>`__
                and the documentation for the request handlers in the language your app
                is written in e.g. `Python Request
                Handler <https://cloud.google.com/appengine/docs/python/tools/webapp/requesthandlerclass>`__.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.tasks_v2.types.Queue` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_queues" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_queues"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_queues,
                default_retry=self._method_configs["ListQueues"].retry,
                default_timeout=self._method_configs["ListQueues"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.ListQueuesRequest(
            parent=parent, filter=filter_, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_queues"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="queues",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def get_queue(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets a queue.

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> name = client.queue_path('[PROJECT]', '[LOCATION]', '[QUEUE]')
            >>>
            >>> response = client.get_queue(name)

        Args:
            name (str): Deletes a queue.

                This command will delete the queue even if it has tasks in it.

                Note: If you delete a queue, a queue with the same name can't be created
                for 7 days.

                WARNING: Using this method may have unintended side effects if you are
                using an App Engine ``queue.yaml`` or ``queue.xml`` file to manage your
                queues. Read `Overview of Queue Management and
                queue.yaml <https://cloud.google.com/tasks/docs/queue-yaml>`__ before
                using this method.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2.types.Queue` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_queue" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_queue"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_queue,
                default_retry=self._method_configs["GetQueue"].retry,
                default_timeout=self._method_configs["GetQueue"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.GetQueueRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_queue"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_queue(
        self,
        parent,
        queue,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        The resource has one pattern, but the API owner expects to add more
        later. (This is the inverse of ORIGINALLY_SINGLE_PATTERN, and prevents
        that from being necessary once there are multiple patterns.)

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # TODO: Initialize `queue`:
            >>> queue = {}
            >>>
            >>> response = client.create_queue(parent, queue)

        Args:
            parent (str): HTTP request headers.

                This map contains the header field names and values. Headers can be set
                when the ``task is created``. Repeated headers are not supported but a
                header value can contain commas.

                Cloud Tasks sets some headers to default values:

                -  ``User-Agent``: By default, this header is
                   ``"AppEngine-Google; (+http://code.google.com/appengine)"``. This
                   header can be modified, but Cloud Tasks will append
                   ``"AppEngine-Google; (+http://code.google.com/appengine)"`` to the
                   modified ``User-Agent``.

                If the task has a ``body``, Cloud Tasks sets the following headers:

                -  ``Content-Type``: By default, the ``Content-Type`` header is set to
                   ``"application/octet-stream"``. The default can be overridden by
                   explicitly setting ``Content-Type`` to a particular media type when
                   the ``task is created``. For example, ``Content-Type`` can be set to
                   ``"application/json"``.
                -  ``Content-Length``: This is computed by Cloud Tasks. This value is
                   output only. It cannot be changed.

                The headers below cannot be set or overridden:

                -  ``Host``
                -  ``X-Google-*``
                -  ``X-AppEngine-*``

                In addition, Cloud Tasks sets some headers when the task is dispatched,
                such as headers containing information about the task; see `request
                headers <https://cloud.google.com/tasks/docs/creating-appengine-handlers#reading_request_headers>`__.
                These headers are set only when the task is dispatched, so they are not
                visible when the task is returned in a Cloud Tasks response.

                Although there is no specific limit for the maximum number of headers or
                the size, there is a limit on the maximum size of the ``Task``. For more
                information, see the ``CreateTask`` documentation.
            queue (Union[dict, ~google.cloud.tasks_v2.types.Queue]): Request message for deleting a task using ``DeleteTask``.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2.types.Queue`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2.types.Queue` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_queue" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_queue"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_queue,
                default_retry=self._method_configs["CreateQueue"].retry,
                default_timeout=self._method_configs["CreateQueue"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.CreateQueueRequest(parent=parent, queue=queue)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_queue"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_queue(
        self,
        queue,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        If this SourceCodeInfo represents a complete declaration, these are
        any comments appearing before and after the declaration which appear to
        be attached to the declaration.

        A series of line comments appearing on consecutive lines, with no other
        tokens appearing on those lines, will be treated as a single comment.

        leading_detached_comments will keep paragraphs of comments that appear
        before (but not connected to) the current element. Each paragraph,
        separated by empty lines, will be one comment element in the repeated
        field.

        Only the comment content is provided; comment markers (e.g. //) are
        stripped out. For block comments, leading whitespace and an asterisk
        will be stripped from the beginning of each line other than the first.
        Newlines are included in the output.

        Examples:

        optional int32 foo = 1; // Comment attached to foo. // Comment attached
        to bar. optional int32 bar = 2;

        optional string baz = 3; // Comment attached to baz. // Another line
        attached to baz.

        // Comment attached to qux. // // Another line attached to qux. optional
        double qux = 4;

        // Detached comment for corge. This is not leading or trailing comments
        // to qux or corge because there are blank lines separating it from //
        both.

        // Detached comment for corge paragraph 2.

        optional string corge = 5; /\* Block comment attached \* to corge.
        Leading asterisks \* will be removed. */ /* Block comment attached to \*
        grault. \*/ optional int32 grault = 6;

        // ignored detached comments.

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> # TODO: Initialize `queue`:
            >>> queue = {}
            >>>
            >>> response = client.update_queue(queue)

        Args:
            queue (Union[dict, ~google.cloud.tasks_v2.types.Queue]): Required. The task name. For example:
                ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID``

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2.types.Queue`
            update_mask (Union[dict, ~google.cloud.tasks_v2.types.FieldMask]): A mask used to specify which fields of the queue are being updated.

                If empty, then all fields will be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2.types.Queue` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_queue" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_queue"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_queue,
                default_retry=self._method_configs["UpdateQueue"].retry,
                default_timeout=self._method_configs["UpdateQueue"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.UpdateQueueRequest(
            queue=queue, update_mask=update_mask
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("queue.name", queue.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_queue"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_queue(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        The mode for generating an ``Authorization`` header for HTTP
        requests.

        If specified, all ``Authorization`` headers in the
        ``HttpRequest.headers`` field will be overridden.

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> name = client.queue_path('[PROJECT]', '[LOCATION]', '[QUEUE]')
            >>>
            >>> client.delete_queue(name)

        Args:
            name (str): Role that is assigned to ``members``. For example, ``roles/viewer``,
                ``roles/editor``, or ``roles/owner``. Required
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_queue" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_queue"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_queue,
                default_retry=self._method_configs["DeleteQueue"].retry,
                default_timeout=self._method_configs["DeleteQueue"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.DeleteQueueRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_queue"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def purge_queue(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Purges a queue by deleting all of its tasks.

        All tasks created before this method is called are permanently deleted.

        Purge operations can take up to one minute to take effect. Tasks
        might be dispatched before the purge takes effect. A purge is irreversible.

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> name = client.queue_path('[PROJECT]', '[LOCATION]', '[QUEUE]')
            >>>
            >>> response = client.purge_queue(name)

        Args:
            name (str): App service.

                By default, the task is sent to the service which is the default service
                when the task is attempted.

                For some queues or tasks which were created using the App Engine Task
                Queue API, ``host`` is not parsable into ``service``, ``version``, and
                ``instance``. For example, some tasks which were created using the App
                Engine SDK use a custom domain name; custom domains are not parsed by
                Cloud Tasks. If ``host`` is not parsable, then ``service``, ``version``,
                and ``instance`` are the empty string.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2.types.Queue` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "purge_queue" not in self._inner_api_calls:
            self._inner_api_calls[
                "purge_queue"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.purge_queue,
                default_retry=self._method_configs["PurgeQueue"].retry,
                default_timeout=self._method_configs["PurgeQueue"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.PurgeQueueRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["purge_queue"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def pause_queue(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Protocol Buffers - Google's data interchange format Copyright 2008
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

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> name = client.queue_path('[PROJECT]', '[LOCATION]', '[QUEUE]')
            >>>
            >>> response = client.pause_queue(name)

        Args:
            name (str): Request message for forcing a task to run now using ``RunTask``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2.types.Queue` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "pause_queue" not in self._inner_api_calls:
            self._inner_api_calls[
                "pause_queue"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.pause_queue,
                default_retry=self._method_configs["PauseQueue"].retry,
                default_timeout=self._method_configs["PauseQueue"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.PauseQueueRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["pause_queue"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def resume_queue(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        If specified, an `OAuth
        token <https://developers.google.com/identity/protocols/OAuth2>`__ will
        be generated and attached as an ``Authorization`` header in the HTTP
        request.

        This type of authorization should generally only be used when calling
        Google APIs hosted on \*.googleapis.com.

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> name = client.queue_path('[PROJECT]', '[LOCATION]', '[QUEUE]')
            >>>
            >>> response = client.resume_queue(name)

        Args:
            name (str): Required. The task name. For example:
                ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID``
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2.types.Queue` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "resume_queue" not in self._inner_api_calls:
            self._inner_api_calls[
                "resume_queue"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.resume_queue,
                default_retry=self._method_configs["ResumeQueue"].retry,
                default_timeout=self._method_configs["ResumeQueue"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.ResumeQueueRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["resume_queue"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_iam_policy(
        self,
        resource,
        options_=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a queue.

        Queues created with this method allow tasks to live for a maximum of 31
        days. After a task is 31 days old, the task will be deleted regardless
        of whether it was dispatched or not.

        WARNING: Using this method may have unintended side effects if you are
        using an App Engine ``queue.yaml`` or ``queue.xml`` file to manage your
        queues. Read `Overview of Queue Management and
        queue.yaml <https://cloud.google.com/tasks/docs/queue-yaml>`__ before
        using this method.

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> # TODO: Initialize `resource`:
            >>> resource = ''
            >>>
            >>> response = client.get_iam_policy(resource)

        Args:
            resource (str): REQUIRED: The resource for which the policy is being requested.
                See the operation documentation for the appropriate value for this field.
            options_ (Union[dict, ~google.cloud.tasks_v2.types.GetPolicyOptions]): Associates ``members`` with a ``role``.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2.types.GetPolicyOptions`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2.types.Policy` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_iam_policy" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_iam_policy"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_iam_policy,
                default_retry=self._method_configs["GetIamPolicy"].retry,
                default_timeout=self._method_configs["GetIamPolicy"].timeout,
                client_info=self._client_info,
            )

        request = iam_policy_pb2.GetIamPolicyRequest(
            resource=resource, options=options_
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("resource", resource)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_iam_policy"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def set_iam_policy(
        self,
        resource,
        policy,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        The response_view specifies which subset of the ``Task`` will be
        returned.

        By default response_view is ``BASIC``; not all information is retrieved
        by default because some data, such as payloads, might be desirable to
        return only when needed because of its large size or because of the
        sensitivity of data that it contains.

        Authorization for ``FULL`` requires ``cloudtasks.tasks.fullView``
        `Google IAM <https://cloud.google.com/iam/>`___ permission on the
        ``Task`` resource.

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> # TODO: Initialize `resource`:
            >>> resource = ''
            >>>
            >>> # TODO: Initialize `policy`:
            >>> policy = {}
            >>>
            >>> response = client.set_iam_policy(resource, policy)

        Args:
            resource (str): REQUIRED: The resource for which the policy is being specified.
                See the operation documentation for the appropriate value for this field.
            policy (Union[dict, ~google.cloud.tasks_v2.types.Policy]): The queue is disabled.

                A queue becomes ``DISABLED`` when
                `queue.yaml <https://cloud.google.com/appengine/docs/python/config/queueref>`__
                or
                `queue.xml <https://cloud.google.com/appengine/docs/standard/java/config/queueref>`__
                is uploaded which does not contain the queue. You cannot directly
                disable a queue.

                When a queue is disabled, tasks can still be added to a queue but the
                tasks are not dispatched.

                To permanently delete this queue and all of its tasks, call
                ``DeleteQueue``.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2.types.Policy`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2.types.Policy` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "set_iam_policy" not in self._inner_api_calls:
            self._inner_api_calls[
                "set_iam_policy"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.set_iam_policy,
                default_retry=self._method_configs["SetIamPolicy"].retry,
                default_timeout=self._method_configs["SetIamPolicy"].timeout,
                client_info=self._client_info,
            )

        request = iam_policy_pb2.SetIamPolicyRequest(resource=resource, policy=policy)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("resource", resource)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["set_iam_policy"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def test_iam_permissions(
        self,
        resource,
        permissions,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        If specified, an
        `OIDC <https://developers.google.com/identity/protocols/OpenIDConnect>`__
        token will be generated and attached as an ``Authorization`` header in
        the HTTP request.

        This type of authorization can be used for many scenarios, including
        calling Cloud Run, or endpoints where you intend to validate the token
        yourself.

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> # TODO: Initialize `resource`:
            >>> resource = ''
            >>>
            >>> # TODO: Initialize `permissions`:
            >>> permissions = []
            >>>
            >>> response = client.test_iam_permissions(resource, permissions)

        Args:
            resource (str): REQUIRED: The resource for which the policy detail is being requested.
                See the operation documentation for the appropriate value for this field.
            permissions (list[str]): A token to retrieve next page of results.

                To return the next page of results, call ``ListTasks`` with this value
                as the ``page_token``.

                If the next_page_token is empty, there are no more results.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2.types.TestIamPermissionsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "test_iam_permissions" not in self._inner_api_calls:
            self._inner_api_calls[
                "test_iam_permissions"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.test_iam_permissions,
                default_retry=self._method_configs["TestIamPermissions"].retry,
                default_timeout=self._method_configs["TestIamPermissions"].timeout,
                client_info=self._client_info,
            )

        request = iam_policy_pb2.TestIamPermissionsRequest(
            resource=resource, permissions=permissions
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("resource", resource)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["test_iam_permissions"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_tasks(
        self,
        parent,
        response_view=None,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Request message for ``CreateTask``.

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> parent = client.queue_path('[PROJECT]', '[LOCATION]', '[QUEUE]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_tasks(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_tasks(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Optional. The relative resource name pattern associated with this
                resource type. The DNS prefix of the full resource name shouldn't be
                specified here.

                The path pattern must follow the syntax, which aligns with HTTP binding
                syntax:

                ::

                    Template = Segment { "/" Segment } ;
                    Segment = LITERAL | Variable ;
                    Variable = "{" LITERAL "}" ;

                Examples:

                ::

                    - "projects/{project}/topics/{topic}"
                    - "projects/{project}/knowledgeBases/{knowledge_base}"

                The components in braces correspond to the IDs for each resource in the
                hierarchy. It is expected that, if multiple patterns are provided, the
                same component name (e.g. "project") refers to IDs of the same type of
                resource.
            response_view (~google.cloud.tasks_v2.enums.Task.View): The ``Status`` type defines a logical error model that is suitable
                for different programming environments, including REST APIs and RPC
                APIs. It is used by `gRPC <https://github.com/grpc>`__. Each ``Status``
                message contains three pieces of data: error code, error message, and
                error details.

                You can find out more about this error model and how to work with it in
                the `API Design Guide <https://cloud.google.com/apis/design/errors>`__.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.tasks_v2.types.Task` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_tasks" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_tasks"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_tasks,
                default_retry=self._method_configs["ListTasks"].retry,
                default_timeout=self._method_configs["ListTasks"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.ListTasksRequest(
            parent=parent, response_view=response_view, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_tasks"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="tasks",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def get_task(
        self,
        name,
        response_view=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Gets a task.

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> name = client.task_path('[PROJECT]', '[LOCATION]', '[QUEUE]', '[TASK]')
            >>>
            >>> response = client.get_task(name)

        Args:
            name (str): A developer-facing error message, which should be in English. Any
                user-facing error message should be localized and sent in the
                ``google.rpc.Status.details`` field, or localized by the client.
            response_view (~google.cloud.tasks_v2.enums.Task.View): Gets the access control policy for a ``Queue``. Returns an empty
                policy if the resource exists and does not have a policy set.

                Authorization requires the following `Google
                IAM <https://cloud.google.com/iam>`__ permission on the specified
                resource parent:

                -  ``cloudtasks.queues.getIamPolicy``
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2.types.Task` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_task" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_task"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_task,
                default_retry=self._method_configs["GetTask"].retry,
                default_timeout=self._method_configs["GetTask"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.GetTaskRequest(name=name, response_view=response_view)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_task"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_task(
        self,
        parent,
        task,
        response_view=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Each of the definitions above may have "options" attached. These are
        just annotations which may cause code to be generated slightly
        differently or may contain hints for code that manipulates protocol
        messages.

        Clients may define custom options as extensions of the \*Options
        messages. These extensions may not yet be known at parsing time, so the
        parser cannot store the values in them. Instead it stores them in a
        field in the \*Options message called uninterpreted_option. This field
        must have the same name across all \*Options messages. We then use this
        field to populate the extensions when we build a descriptor, at which
        point all protos have been parsed and so all extensions are known.

        Extension numbers for custom options may be chosen as follows:

        -  For options which will only be used within a single application or
           organization, or for experimental options, use field numbers 50000
           through 99999. It is up to you to ensure that you do not use the same
           number for multiple options.
        -  For options which will be published and used publicly by multiple
           independent entities, e-mail
           protobuf-global-extension-registry@google.com to reserve extension
           numbers. Simply provide your project name (e.g. Objective-C plugin)
           and your project website (if available) -- there's no need to explain
           how you intend to use them. Usually you only need one extension
           number. You can declare multiple options with only one extension
           number by putting them in a sub-message. See the Custom Options
           section of the docs for examples:
           https://developers.google.com/protocol-buffers/docs/proto#options If
           this turns out to be popular, a web service will be set up to
           automatically assign option numbers.

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> parent = client.queue_path('[PROJECT]', '[LOCATION]', '[QUEUE]')
            >>>
            >>> # TODO: Initialize `task`:
            >>> task = {}
            >>>
            >>> response = client.create_task(parent, task)

        Args:
            parent (str): Sets the access control policy for a ``Queue``. Replaces any
                existing policy.

                Note: The Cloud Console does not check queue-level IAM permissions yet.
                Project-level permissions are required to use the Cloud Console.

                Authorization requires the following `Google
                IAM <https://cloud.google.com/iam>`__ permission on the specified
                resource parent:

                -  ``cloudtasks.queues.setIamPolicy``
            task (Union[dict, ~google.cloud.tasks_v2.types.Task]): Role that is assigned to ``members``. For example, ``roles/viewer``,
                ``roles/editor``, or ``roles/owner``.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2.types.Task`
            response_view (~google.cloud.tasks_v2.enums.Task.View): See ``HttpRule``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2.types.Task` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_task" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_task"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_task,
                default_retry=self._method_configs["CreateTask"].retry,
                default_timeout=self._method_configs["CreateTask"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.CreateTaskRequest(
            parent=parent, task=task, response_view=response_view
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_task"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def delete_task(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes a task.

        A task can be deleted if it is scheduled or dispatched. A task
        cannot be deleted if it has executed successfully or permanently
        failed.

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> name = client.task_path('[PROJECT]', '[LOCATION]', '[QUEUE]', '[TASK]')
            >>>
            >>> client.delete_task(name)

        Args:
            name (str): A single identity that is exempted from "data access" audit logging
                for the ``service`` specified above. Follows the same format of
                Binding.members.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_task" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_task"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_task,
                default_retry=self._method_configs["DeleteTask"].retry,
                default_timeout=self._method_configs["DeleteTask"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.DeleteTaskRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_task"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def run_task(
        self,
        name,
        response_view=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Required. The queue name. For example:
        ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID``

        The queue must already exist.

        Example:
            >>> from google.cloud import tasks_v2
            >>>
            >>> client = tasks_v2.CloudTasksClient()
            >>>
            >>> name = client.task_path('[PROJECT]', '[LOCATION]', '[QUEUE]', '[TASK]')
            >>>
            >>> response = client.run_task(name)

        Args:
            name (str): Returns permissions that a caller has on a ``Queue``. If the
                resource does not exist, this will return an empty set of permissions,
                not a ``NOT_FOUND`` error.

                Note: This operation is designed to be used for building
                permission-aware UIs and command-line tools, not for authorization
                checking. This operation may "fail open" without warning.
            response_view (~google.cloud.tasks_v2.enums.Task.View): Denotes a field as required. This indicates that the field **must**
                be provided as part of the request, and failure to do so will cause an
                error (usually ``INVALID_ARGUMENT``).
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2.types.Task` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "run_task" not in self._inner_api_calls:
            self._inner_api_calls[
                "run_task"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.run_task,
                default_retry=self._method_configs["RunTask"].retry,
                default_timeout=self._method_configs["RunTask"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.RunTaskRequest(name=name, response_view=response_view)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["run_task"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
