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


import google.api_core.grpc_helpers

from google.cloud.tasks_v2beta2.proto import cloudtasks_pb2_grpc


class CloudTasksGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.tasks.v2beta2 CloudTasks API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self, channel=None, credentials=None, address="cloudtasks.googleapis.com:443"
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive."
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {"cloud_tasks_stub": cloudtasks_pb2_grpc.CloudTasksStub(channel)}

    @classmethod
    def create_channel(
        cls, address="cloudtasks.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def list_queues(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.list_queues`.

        Lists queues.

        Queues are returned in lexicographical order.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].ListQueues

    @property
    def get_queue(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.get_queue`.

        Gets a queue.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].GetQueue

    @property
    def create_queue(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.create_queue`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].CreateQueue

    @property
    def update_queue(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.update_queue`.

        A token identifying the page of results to return.

        To request the first page results, page_token must be empty. To request
        the next page of results, page_token must be the value of
        ``next_page_token`` returned from the previous call to ``ListTasks``
        method.

        The page token is valid for only 2 hours.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].UpdateQueue

    @property
    def delete_queue(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.delete_queue`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].DeleteQueue

    @property
    def purge_queue(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.purge_queue`.

        Purges a queue by deleting all of its tasks.

        All tasks created before this method is called are permanently deleted.

        Purge operations can take up to one minute to take effect. Tasks
        might be dispatched before the purge takes effect. A purge is irreversible.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].PurgeQueue

    @property
    def pause_queue(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.pause_queue`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].PauseQueue

    @property
    def resume_queue(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.resume_queue`.

        javanano_as_lite

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].ResumeQueue

    @property
    def get_iam_policy(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.get_iam_policy`.

        The pull message contains data that can be used by the caller of
        ``LeaseTasks`` to process the task.

        This proto can only be used for tasks in a queue which has
        ``pull_target`` set.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].GetIamPolicy

    @property
    def set_iam_policy(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.set_iam_policy`.

        Response message for listing tasks using ``ListTasks``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].SetIamPolicy

    @property
    def test_iam_permissions(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.test_iam_permissions`.

        If set, all the classes from the .proto file are wrapped in a single
        outer class with the given name. This applies to both Proto1 (equivalent
        to the old "--one_java_file" option) and Proto2 (where a .proto always
        translates to a single class, but you may want to explicitly choose the
        class name).

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].TestIamPermissions

    @property
    def list_tasks(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.list_tasks`.

        Request message for deleting a task using ``DeleteTask``.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].ListTasks

    @property
    def get_task(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.get_task`.

        Gets a task.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].GetTask

    @property
    def create_task(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.create_task`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].CreateTask

    @property
    def delete_task(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.delete_task`.

        Deletes a task.

        A task can be deleted if it is scheduled or dispatched. A task
        cannot be deleted if it has completed successfully or permanently
        failed.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].DeleteTask

    @property
    def lease_tasks(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.lease_tasks`.

        Request message for ``GetIamPolicy`` method.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].LeaseTasks

    @property
    def acknowledge_task(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.acknowledge_task`.

        Deletes a queue.

        This command will delete the queue even if it has tasks in it.

        Note: If you delete a queue, a queue with the same name can't be created
        for 7 days.

        WARNING: Using this method may have unintended side effects if you are
        using an App Engine ``queue.yaml`` or ``queue.xml`` file to manage your
        queues. Read `Overview of Queue Management and
        queue.yaml <https://cloud.google.com/tasks/docs/queue-yaml>`__ before
        using this method.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].AcknowledgeTask

    @property
    def renew_lease(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.renew_lease`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].RenewLease

    @property
    def cancel_lease(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.cancel_lease`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].CancelLease

    @property
    def run_task(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.run_task`.

        A token to retrieve next page of results.

        To return the next page of results, call ``ListTasks`` with this value
        as the ``page_token``.

        If the next_page_token is empty, there are no more results.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].RunTask
