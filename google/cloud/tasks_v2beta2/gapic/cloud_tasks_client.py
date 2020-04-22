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

"""Accesses the google.cloud.tasks.v2beta2 CloudTasks API."""

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

from google.cloud.tasks_v2beta2.gapic import cloud_tasks_client_config
from google.cloud.tasks_v2beta2.gapic import enums
from google.cloud.tasks_v2beta2.gapic.transports import cloud_tasks_grpc_transport
from google.cloud.tasks_v2beta2.proto import cloudtasks_pb2
from google.cloud.tasks_v2beta2.proto import cloudtasks_pb2_grpc
from google.cloud.tasks_v2beta2.proto import queue_pb2
from google.cloud.tasks_v2beta2.proto import task_pb2
from google.iam.v1 import iam_policy_pb2
from google.iam.v1 import options_pb2
from google.iam.v1 import policy_pb2
from google.protobuf import duration_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2
from google.protobuf import timestamp_pb2


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
    _INTERFACE_NAME = "google.cloud.tasks.v2beta2.CloudTasks"

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
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
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
            parent (str): App Engine HTTP target.

                The task will be delivered to the App Engine application hostname
                specified by its ``AppEngineHttpTarget`` and ``AppEngineHttpRequest``.
                The documentation for ``AppEngineHttpRequest`` explains how the task's
                host URL is constructed.

                Using ``AppEngineHttpTarget`` requires
                ```appengine.applications.get`` <https://cloud.google.com/appengine/docs/admin-api/access-control>`__
                Google IAM permission for the project and the following scope:

                ``https://www.googleapis.com/auth/cloud-platform``
            filter_ (str): Request message for getting a task using ``GetTask``.
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
            An iterable of :class:`~google.cloud.tasks_v2beta2.types.Queue` instances.
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
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> name = client.queue_path('[PROJECT]', '[LOCATION]', '[QUEUE]')
            >>>
            >>> response = client.get_queue(name)

        Args:
            name (str): If this SourceCodeInfo represents a complete declaration, these are
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
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2beta2.types.Queue` instance.

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
        A Location identifies a piece of source code in a .proto file which
        corresponds to a particular definition. This information is intended to
        be useful to IDEs, code indexers, documentation generators, and similar
        tools.

        For example, say we have a file like: message Foo { optional string foo
        = 1; } Let's look at just the field definition: optional string foo = 1;
        ^ ^^ ^^ ^ ^^^ a bc de f ghi We have the following locations: span path
        represents [a,i) [ 4, 0, 2, 0 ] The whole field definition. [a,b) [ 4,
        0, 2, 0, 4 ] The label (optional). [c,d) [ 4, 0, 2, 0, 5 ] The type
        (string). [e,f) [ 4, 0, 2, 0, 1 ] The name (foo). [g,h) [ 4, 0, 2, 0, 3
        ] The number (1).

        Notes:

        -  A location may refer to a repeated field itself (i.e. not to any
           particular index within it). This is used whenever a set of elements
           are logically enclosed in a single code segment. For example, an
           entire extend block (possibly containing multiple extension
           definitions) will have an outer location whose path refers to the
           "extensions" repeated field without an index.
        -  Multiple locations may have the same path. This happens when a single
           logical declaration is spread out across multiple places. The most
           obvious example is the "extend" block again -- there may be multiple
           extend blocks in the same scope, each of which will have the same
           path.
        -  A location's span is not always a subset of its parent's span. For
           example, the "extendee" of an extension declaration appears at the
           beginning of the "extend" block and is shared by all extensions
           within the block.
        -  Just because a location's span is a subset of some other location's
           span does not mean that it is a descendant. For example, a "group"
           defines both a type and a field in a single declaration. Thus, the
           locations corresponding to the type and field and their components
           will overlap.
        -  Code which tries to interpret locations should probably be designed
           to ignore those that it doesn't understand, as more types of
           locations could be recorded in the future.

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> parent = client.location_path('[PROJECT]', '[LOCATION]')
            >>>
            >>> # TODO: Initialize `queue`:
            >>> queue = {}
            >>>
            >>> response = client.create_queue(parent, queue)

        Args:
            parent (str): Pauses the queue.

                If a queue is paused then the system will stop dispatching tasks until
                the queue is resumed via ``ResumeQueue``. Tasks can still be added when
                the queue is paused. A queue is paused if its ``state`` is ``PAUSED``.
            queue (Union[dict, ~google.cloud.tasks_v2beta2.types.Queue]): The response_view specifies which subset of the ``Task`` will be
                returned.

                By default response_view is ``BASIC``; not all information is retrieved
                by default because some data, such as payloads, might be desirable to
                return only when needed because of its large size or because of the
                sensitivity of data that it contains.

                Authorization for ``FULL`` requires ``cloudtasks.tasks.fullView``
                `Google IAM <https://cloud.google.com/iam/>`___ permission on the
                ``Task`` resource.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2beta2.types.Queue`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2beta2.types.Queue` instance.

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
        A token identifying the page of results to return.

        To request the first page results, page_token must be empty. To request
        the next page of results, page_token must be the value of
        ``next_page_token`` returned from the previous call to ``ListTasks``
        method.

        The page token is valid for only 2 hours.

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> # TODO: Initialize `queue`:
            >>> queue = {}
            >>>
            >>> response = client.update_queue(queue)

        Args:
            queue (Union[dict, ~google.cloud.tasks_v2beta2.types.Queue]): The ``Status`` type defines a logical error model that is suitable
                for different programming environments, including REST APIs and RPC
                APIs. It is used by `gRPC <https://github.com/grpc>`__. Each ``Status``
                message contains three pieces of data: error code, error message, and
                error details.

                You can find out more about this error model and how to work with it in
                the `API Design Guide <https://cloud.google.com/apis/design/errors>`__.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2beta2.types.Queue`
            update_mask (Union[dict, ~google.cloud.tasks_v2beta2.types.FieldMask]): A mask used to specify which fields of the queue are being updated.

                If empty, then all fields will be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2beta2.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2beta2.types.Queue` instance.

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
        ``Any`` contains an arbitrary serialized protocol buffer message
        along with a URL that describes the type of the serialized message.

        Protobuf library provides support to pack/unpack Any values in the form
        of utility functions or additional generated methods of the Any type.

        Example 1: Pack and unpack a message in C++.

        ::

            Foo foo = ...;
            Any any;
            any.PackFrom(foo);
            ...
            if (any.UnpackTo(&foo)) {
              ...
            }

        Example 2: Pack and unpack a message in Java.

        ::

            Foo foo = ...;
            Any any = Any.pack(foo);
            ...
            if (any.is(Foo.class)) {
              foo = any.unpack(Foo.class);
            }

        Example 3: Pack and unpack a message in Python.

        ::

            foo = Foo(...)
            any = Any()
            any.Pack(foo)
            ...
            if any.Is(Foo.DESCRIPTOR):
              any.Unpack(foo)
              ...

        Example 4: Pack and unpack a message in Go

        ::

             foo := &pb.Foo{...}
             any, err := ptypes.MarshalAny(foo)
             ...
             foo := &pb.Foo{}
             if err := ptypes.UnmarshalAny(any, foo); err != nil {
               ...
             }

        The pack methods provided by protobuf library will by default use
        'type.googleapis.com/full.type.name' as the type URL and the unpack
        methods only use the fully qualified type name after the last '/' in the
        type URL, for example "foo.bar.com/x/y.z" will yield type name "y.z".

        # JSON

        The JSON representation of an ``Any`` value uses the regular
        representation of the deserialized, embedded message, with an additional
        field ``@type`` which contains the type URL. Example:

        ::

            package google.profile;
            message Person {
              string first_name = 1;
              string last_name = 2;
            }

            {
              "@type": "type.googleapis.com/google.profile.Person",
              "firstName": <string>,
              "lastName": <string>
            }

        If the embedded message type is well-known and has a custom JSON
        representation, that representation will be embedded adding a field
        ``value`` which holds the custom JSON in addition to the ``@type``
        field. Example (for message ``google.protobuf.Duration``):

        ::

            {
              "@type": "type.googleapis.com/google.protobuf.Duration",
              "value": "1.212s"
            }

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> name = client.queue_path('[PROJECT]', '[LOCATION]', '[QUEUE]')
            >>>
            >>> client.delete_queue(name)

        Args:
            name (str): The status code, which should be an enum value of
                ``google.rpc.Code``.
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
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> name = client.queue_path('[PROJECT]', '[LOCATION]', '[QUEUE]')
            >>>
            >>> response = client.purge_queue(name)

        Args:
            name (str): Resume a queue.

                This method resumes a queue after it has been ``PAUSED`` or
                ``DISABLED``. The state of a queue is stored in the queue's ``state``;
                after calling this method it will be set to ``RUNNING``.

                WARNING: Resuming many high-QPS queues at the same time can lead to
                target overloading. If you are resuming high-QPS queues, follow the
                500/50/5 pattern described in `Managing Cloud Tasks Scaling
                Risks <https://cloud.google.com/tasks/docs/manage-cloud-task-scaling>`__.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2beta2.types.Queue` instance.

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
        A URL/resource name that uniquely identifies the type of the
        serialized protocol buffer message. This string must contain at least
        one "/" character. The last segment of the URL's path must represent the
        fully qualified name of the type (as in
        ``path/google.protobuf.Duration``). The name should be in a canonical
        form (e.g., leading "." is not accepted).

        In practice, teams usually precompile into the binary all types that
        they expect it to use in the context of Any. However, for URLs which use
        the scheme ``http``, ``https``, or no scheme, one can optionally set up
        a type server that maps type URLs to message definitions as follows:

        -  If no scheme is provided, ``https`` is assumed.
        -  An HTTP GET on the URL must yield a ``google.protobuf.Type`` value in
           binary format, or produce an error.
        -  Applications are allowed to cache lookup results based on the URL, or
           have them precompiled into a binary to avoid any lookup. Therefore,
           binary compatibility needs to be preserved on changes to types. (Use
           versioned type names to manage breaking changes.)

        Note: this functionality is not currently available in the official
        protobuf release, and it is not used for type URLs beginning with
        type.googleapis.com.

        Schemes other than ``http``, ``https`` (or the empty scheme) might be
        used with implementation specific semantics.

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> name = client.queue_path('[PROJECT]', '[LOCATION]', '[QUEUE]')
            >>>
            >>> response = client.pause_queue(name)

        Args:
            name (str): HTTP request headers.

                This map contains the header field names and values. Headers can be set
                when the ``task is created``. Repeated headers are not supported but a
                header value can contain commas.

                Cloud Tasks sets some headers to default values:

                -  ``User-Agent``: By default, this header is
                   ``"AppEngine-Google; (+http://code.google.com/appengine)"``. This
                   header can be modified, but Cloud Tasks will append
                   ``"AppEngine-Google; (+http://code.google.com/appengine)"`` to the
                   modified ``User-Agent``.

                If the task has a ``payload``, Cloud Tasks sets the following headers:

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
                headers <https://cloud.google.com/appengine/docs/python/taskqueue/push/creating-handlers#reading_request_headers>`__.
                These headers are set only when the task is dispatched, so they are not
                visible when the task is returned in a Cloud Tasks response.

                Although there is no specific limit for the maximum number of headers or
                the size, there is a limit on the maximum size of the ``Task``. For more
                information, see the ``CreateTask`` documentation.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2beta2.types.Queue` instance.

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
        javanano_as_lite

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> name = client.queue_path('[PROJECT]', '[LOCATION]', '[QUEUE]')
            >>>
            >>> response = client.resume_queue(name)

        Args:
            name (str): Payload.

                The payload will be sent as the HTTP message body. A message body, and
                thus a payload, is allowed only if the HTTP method is POST or PUT. It is
                an error to set a data payload on a task with an incompatible
                ``HttpMethod``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2beta2.types.Queue` instance.

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
        The pull message contains data that can be used by the caller of
        ``LeaseTasks`` to process the task.

        This proto can only be used for tasks in a queue which has
        ``pull_target`` set.

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> # TODO: Initialize `resource`:
            >>> resource = ''
            >>>
            >>> response = client.get_iam_policy(resource)

        Args:
            resource (str): REQUIRED: The resource for which the policy is being requested.
                See the operation documentation for the appropriate value for this field.
            options_ (Union[dict, ~google.cloud.tasks_v2beta2.types.GetPolicyOptions]): Signed fractions of a second at nanosecond resolution of the span of
                time. Durations less than one second are represented with a 0
                ``seconds`` field and a positive or negative ``nanos`` field. For
                durations of one second or more, a non-zero value for the ``nanos``
                field must be of the same sign as the ``seconds`` field. Must be from
                -999,999,999 to +999,999,999 inclusive.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2beta2.types.GetPolicyOptions`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2beta2.types.Policy` instance.

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
        Response message for listing tasks using ``ListTasks``.

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
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
            policy (Union[dict, ~google.cloud.tasks_v2beta2.types.Policy]): The resource type that the annotated field references.

                Example:

                ::

                    message Subscription {
                      string topic = 2 [(google.api.resource_reference) = {
                        type: "pubsub.googleapis.com/Topic"
                      }];
                    }

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2beta2.types.Policy`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2beta2.types.Policy` instance.

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
        If set, all the classes from the .proto file are wrapped in a single
        outer class with the given name. This applies to both Proto1 (equivalent
        to the old "--one_java_file" option) and Proto2 (where a .proto always
        translates to a single class, but you may want to explicitly choose the
        class name).

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
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
            permissions (list[str]): The resource type of a child collection that the annotated field
                references. This is useful for annotating the ``parent`` field that
                doesn't have a fixed resource type.

                Example:

                ::

                    message ListLogEntriesRequest {
                      string parent = 1 [(google.api.resource_reference) = {
                        child_type: "logging.googleapis.com/LogEntry"
                      };
                    }
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2beta2.types.TestIamPermissionsResponse` instance.

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
        Request message for deleting a task using ``DeleteTask``.

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
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
            parent (str): The jstype option determines the JavaScript type used for values of
                the field. The option is permitted only for 64 bit integral and fixed
                types (int64, uint64, sint64, fixed64, sfixed64). A field with jstype
                JS_STRING is represented as JavaScript string, which avoids loss of
                precision that can happen when a large value is converted to a floating
                point JavaScript. Specifying JS_NUMBER for the jstype causes the
                generated JavaScript code to use the JavaScript "number" type. The
                behavior of the default option JS_NORMAL is implementation dependent.

                This option is an enum to permit additional types to be added, e.g.
                goog.math.Integer.
            response_view (~google.cloud.tasks_v2beta2.enums.Task.View): App Engine Routing.

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
            An iterable of :class:`~google.cloud.tasks_v2beta2.types.Task` instances.
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
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> name = client.task_path('[PROJECT]', '[LOCATION]', '[QUEUE]', '[TASK]')
            >>>
            >>> response = client.get_task(name)

        Args:
            name (str): Required. The task name. For example:
                ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID``
            response_view (~google.cloud.tasks_v2beta2.enums.Task.View): Request message for ``ResumeQueue``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2beta2.types.Task` instance.

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
        Identifies which part of the FileDescriptorProto was defined at this
        location.

        Each element is a field number or an index. They form a path from the
        root FileDescriptorProto to the place where the definition. For example,
        this path: [ 4, 3, 2, 7, 1 ] refers to: file.message_type(3) // 4, 3
        .field(7) // 2, 7 .name() // 1 This is because
        FileDescriptorProto.message_type has field number 4: repeated
        DescriptorProto message_type = 4; and DescriptorProto.field has field
        number 2: repeated FieldDescriptorProto field = 2; and
        FieldDescriptorProto.name has field number 1: optional string name = 1;

        Thus, the above path gives the location of a field name. If we removed
        the last element: [ 4, 3, 2, 7 ] this path refers to the whole field
        declaration (from the beginning of the label to the terminating
        semicolon).

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> parent = client.queue_path('[PROJECT]', '[LOCATION]', '[QUEUE]')
            >>>
            >>> # TODO: Initialize `task`:
            >>> task = {}
            >>>
            >>> response = client.create_task(parent, task)

        Args:
            parent (str): App instance.

                By default, the task is sent to an instance which is available when the
                task is attempted.

                Requests can only be sent to a specific instance if `manual scaling is
                used in App Engine
                Standard <https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine?hl=en_US#scaling_types_and_instance_classes>`__.
                App Engine Flex does not support instances. For more information, see
                `App Engine Standard request
                routing <https://cloud.google.com/appengine/docs/standard/python/how-requests-are-routed>`__
                and `App Engine Flex request
                routing <https://cloud.google.com/appengine/docs/flexible/python/how-requests-are-routed>`__.
            task (Union[dict, ~google.cloud.tasks_v2beta2.types.Task]): Specifies the log_type that was be enabled. ADMIN_ACTIVITY is always
                enabled, and cannot be configured. Required

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2beta2.types.Task`
            response_view (~google.cloud.tasks_v2beta2.enums.Task.View): Output only. The host that the task is sent to.

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

                -  ``application_domain_name`` = The domain name of the app, for example
                   .appspot.com, which is associated with the queue's project ID. Some
                   tasks which were created using the App Engine SDK use a custom domain
                   name.

                -  ``service =`` ``service``

                -  ``version =`` ``version``

                -  ``version_dot_service =`` ``version`` ``+ '.' +`` ``service``

                -  ``instance =`` ``instance``

                -  ``instance_dot_service =`` ``instance`` ``+ '.' +`` ``service``

                -  ``instance_dot_version =`` ``instance`` ``+ '.' +`` ``version``

                -  ``instance_dot_version_dot_service =`` ``instance`` ``+ '.' +``
                   ``version`` ``+ '.' +`` ``service``

                If ``service`` is empty, then the task will be sent to the service which
                is the default service when the task is attempted.

                If ``version`` is empty, then the task will be sent to the version which
                is the default version when the task is attempted.

                If ``instance`` is empty, then the task will be sent to an instance
                which is available when the task is attempted.

                If ``service``, ``version``, or ``instance`` is invalid, then the task
                will be sent to the default version of the default service when the task
                is attempted.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2beta2.types.Task` instance.

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
        cannot be deleted if it has completed successfully or permanently
        failed.

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> name = client.task_path('[PROJECT]', '[LOCATION]', '[QUEUE]', '[TASK]')
            >>>
            >>> client.delete_task(name)

        Args:
            name (str): Required. The queue name. For example:
                ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID``
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

    def lease_tasks(
        self,
        parent,
        lease_duration,
        max_tasks=None,
        response_view=None,
        filter_=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Request message for ``GetIamPolicy`` method.

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> parent = client.queue_path('[PROJECT]', '[LOCATION]', '[QUEUE]')
            >>>
            >>> # TODO: Initialize `lease_duration`:
            >>> lease_duration = {}
            >>>
            >>> response = client.lease_tasks(parent, lease_duration)

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
            lease_duration (Union[dict, ~google.cloud.tasks_v2beta2.types.Duration]): Lists the tasks in a queue.

                By default, only the ``BASIC`` view is retrieved due to performance
                considerations; ``response_view`` controls the subset of information
                which is returned.

                The tasks may be returned in any order. The ordering may change at any
                time.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2beta2.types.Duration`
            max_tasks (int): The view specifies a subset of ``Task`` data.

                When a task is returned in a response, not all information is retrieved
                by default because some data, such as payloads, might be desirable to
                return only when needed because of its large size or because of the
                sensitivity of data that it contains.
            response_view (~google.cloud.tasks_v2beta2.enums.Task.View): Output only. The state of the queue.

                ``state`` can only be changed by called ``PauseQueue``, ``ResumeQueue``,
                or uploading
                `queue.yaml/xml <https://cloud.google.com/appengine/docs/python/config/queueref>`__.
                ``UpdateQueue`` cannot be used to change ``state``.
            filter_ (str): The basic view omits fields which can be large or can contain
                sensitive data.

                This view does not include the (``payload in AppEngineHttpRequest`` and
                ``payload in PullMessage``). These payloads are desirable to return only
                when needed, because they can be large and because of the sensitivity of
                the data that you choose to store in it.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2beta2.types.LeaseTasksResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "lease_tasks" not in self._inner_api_calls:
            self._inner_api_calls[
                "lease_tasks"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.lease_tasks,
                default_retry=self._method_configs["LeaseTasks"].retry,
                default_timeout=self._method_configs["LeaseTasks"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.LeaseTasksRequest(
            parent=parent,
            lease_duration=lease_duration,
            max_tasks=max_tasks,
            response_view=response_view,
            filter=filter_,
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

        return self._inner_api_calls["lease_tasks"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def acknowledge_task(
        self,
        name,
        schedule_time,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes a queue.

        This command will delete the queue even if it has tasks in it.

        Note: If you delete a queue, a queue with the same name can't be created
        for 7 days.

        WARNING: Using this method may have unintended side effects if you are
        using an App Engine ``queue.yaml`` or ``queue.xml`` file to manage your
        queues. Read `Overview of Queue Management and
        queue.yaml <https://cloud.google.com/tasks/docs/queue-yaml>`__ before
        using this method.

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> name = client.task_path('[PROJECT]', '[LOCATION]', '[QUEUE]', '[TASK]')
            >>>
            >>> # TODO: Initialize `schedule_time`:
            >>> schedule_time = {}
            >>>
            >>> client.acknowledge_task(name, schedule_time)

        Args:
            name (str): Caller-specified and required in ``CreateQueue``\ [], after which
                the queue config type becomes output only, though fields within the
                config are mutable.

                The queue's target.

                The target applies to all tasks in the queue.
            schedule_time (Union[dict, ~google.cloud.tasks_v2beta2.types.Timestamp]): Optionally caller-specified in ``CreateTask``.

                The task name.

                The task name must have the following format:
                ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID``

                -  ``PROJECT_ID`` can contain letters ([A-Za-z]), numbers ([0-9]),
                   hyphens (-), colons (:), or periods (.). For more information, see
                   `Identifying
                   projects <https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects>`__
                -  ``LOCATION_ID`` is the canonical ID for the task's location. The list
                   of available locations can be obtained by calling ``ListLocations``.
                   For more information, see https://cloud.google.com/about/locations/.
                -  ``QUEUE_ID`` can contain letters ([A-Za-z]), numbers ([0-9]), or
                   hyphens (-). The maximum length is 100 characters.
                -  ``TASK_ID`` can contain only letters ([A-Za-z]), numbers ([0-9]),
                   hyphens (-), or underscores (_). The maximum length is 500
                   characters.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2beta2.types.Timestamp`
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
        if "acknowledge_task" not in self._inner_api_calls:
            self._inner_api_calls[
                "acknowledge_task"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.acknowledge_task,
                default_retry=self._method_configs["AcknowledgeTask"].retry,
                default_timeout=self._method_configs["AcknowledgeTask"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.AcknowledgeTaskRequest(
            name=name, schedule_time=schedule_time
        )
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

        self._inner_api_calls["acknowledge_task"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def renew_lease(
        self,
        name,
        schedule_time,
        lease_duration,
        response_view=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Output only. The max burst size.

        Max burst size limits how fast tasks in queue are processed when many
        tasks are in the queue and the rate is high. This field allows the queue
        to have a high rate so processing starts shortly after a task is
        enqueued, but still limits resource usage when many tasks are enqueued
        in a short period of time.

        The `token bucket <https://wikipedia.org/wiki/Token_Bucket>`__ algorithm
        is used to control the rate of task dispatches. Each queue has a token
        bucket that holds tokens, up to the maximum specified by
        ``max_burst_size``. Each time a task is dispatched, a token is removed
        from the bucket. Tasks will be dispatched until the queue's bucket runs
        out of tokens. The bucket will be continuously refilled with new tokens
        based on ``max_tasks_dispatched_per_second``.

        Cloud Tasks will pick the value of ``max_burst_size`` based on the value
        of ``max_tasks_dispatched_per_second``.

        For App Engine queues that were created or updated using
        ``queue.yaml/xml``, ``max_burst_size`` is equal to
        `bucket_size <https://cloud.google.com/appengine/docs/standard/python/config/queueref#bucket_size>`__.
        Since ``max_burst_size`` is output only, if ``UpdateQueue`` is called on
        a queue created by ``queue.yaml/xml``, ``max_burst_size`` will be reset
        based on the value of ``max_tasks_dispatched_per_second``, regardless of
        whether ``max_tasks_dispatched_per_second`` is updated.

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> name = client.task_path('[PROJECT]', '[LOCATION]', '[QUEUE]', '[TASK]')
            >>>
            >>> # TODO: Initialize `schedule_time`:
            >>> schedule_time = {}
            >>>
            >>> # TODO: Initialize `lease_duration`:
            >>> lease_duration = {}
            >>>
            >>> response = client.renew_lease(name, schedule_time, lease_duration)

        Args:
            name (str): The maximum number of attempts for a task.

                Cloud Tasks will attempt the task ``max_attempts`` times (that is, if
                the first attempt fails, then there will be ``max_attempts - 1``
                retries). Must be > 0.
            schedule_time (Union[dict, ~google.cloud.tasks_v2beta2.types.Timestamp]): Output only. The time that this attempt response was received.

                ``response_time`` will be truncated to the nearest microsecond.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2beta2.types.Timestamp`
            lease_duration (Union[dict, ~google.cloud.tasks_v2beta2.types.Duration]): Creates a task and adds it to a queue.

                Tasks cannot be updated after creation; there is no UpdateTask command.

                -  For ``App Engine queues``, the maximum task size is 100KB.
                -  For ``pull queues``, the maximum task size is 1MB.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2beta2.types.Duration`
            response_view (~google.cloud.tasks_v2beta2.enums.Task.View): App Engine HTTP request that is sent to the task's target. Can be
                set only if ``app_engine_http_target`` is set on the queue.

                An App Engine task is a task that has ``AppEngineHttpRequest`` set.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2beta2.types.Task` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "renew_lease" not in self._inner_api_calls:
            self._inner_api_calls[
                "renew_lease"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.renew_lease,
                default_retry=self._method_configs["RenewLease"].retry,
                default_timeout=self._method_configs["RenewLease"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.RenewLeaseRequest(
            name=name,
            schedule_time=schedule_time,
            lease_duration=lease_duration,
            response_view=response_view,
        )
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

        return self._inner_api_calls["renew_lease"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def cancel_lease(
        self,
        name,
        schedule_time,
        response_view=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        The task's tag.

        Tags allow similar tasks to be processed in a batch. If you label tasks
        with a tag, your worker can ``lease tasks`` with the same tag using
        ``filter``. For example, if you want to aggregate the events associated
        with a specific user once a day, you could tag tasks with the user ID.

        The task's tag can only be set when the ``task is created``.

        The tag must be less than 500 characters.

        SDK compatibility: Although the SDK allows tags to be either string or
        `bytes <https://cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/taskqueue/TaskOptions.html#tag-byte:A->`__,
        only UTF-8 encoded tags can be used in Cloud Tasks. If a tag isn't UTF-8
        encoded, the tag will be empty when the task is returned by Cloud Tasks.

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> name = client.task_path('[PROJECT]', '[LOCATION]', '[QUEUE]', '[TASK]')
            >>>
            >>> # TODO: Initialize `schedule_time`:
            >>> schedule_time = {}
            >>>
            >>> response = client.cancel_lease(name, schedule_time)

        Args:
            name (str): Protocol Buffers - Google's data interchange format Copyright 2008
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
            schedule_time (Union[dict, ~google.cloud.tasks_v2beta2.types.Timestamp]): See ``HttpRule``.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.tasks_v2beta2.types.Timestamp`
            response_view (~google.cloud.tasks_v2beta2.enums.Task.View): Response message for leasing tasks using ``LeaseTasks``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2beta2.types.Task` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "cancel_lease" not in self._inner_api_calls:
            self._inner_api_calls[
                "cancel_lease"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.cancel_lease,
                default_retry=self._method_configs["CancelLease"].retry,
                default_timeout=self._method_configs["CancelLease"].timeout,
                client_info=self._client_info,
            )

        request = cloudtasks_pb2.CancelLeaseRequest(
            name=name, schedule_time=schedule_time, response_view=response_view
        )
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

        return self._inner_api_calls["cancel_lease"](
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
        A token to retrieve next page of results.

        To return the next page of results, call ``ListTasks`` with this value
        as the ``page_token``.

        If the next_page_token is empty, there are no more results.

        Example:
            >>> from google.cloud import tasks_v2beta2
            >>>
            >>> client = tasks_v2beta2.CloudTasksClient()
            >>>
            >>> name = client.task_path('[PROJECT]', '[LOCATION]', '[QUEUE]', '[TASK]')
            >>>
            >>> response = client.run_task(name)

        Args:
            name (str): The time when the task is scheduled to be attempted.

                For App Engine queues, this is when the task will be attempted or
                retried.

                For pull queues, this is the time when the task is available to be
                leased; if a task is currently leased, this is the time when the current
                lease expires, that is, the time that the task was leased plus the
                ``lease_duration``.

                ``schedule_time`` will be truncated to the nearest microsecond.
            response_view (~google.cloud.tasks_v2beta2.enums.Task.View): Request message for acknowledging a task using ``AcknowledgeTask``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry client library requests. If ``None`` is specified,
                requests will be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the client library request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the client library method.

        Returns:
            A :class:`~google.cloud.tasks_v2beta2.types.Task` instance.

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
