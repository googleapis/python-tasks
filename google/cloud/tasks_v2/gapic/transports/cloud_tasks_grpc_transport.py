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

from google.cloud.tasks_v2.proto import cloudtasks_pb2_grpc


class CloudTasksGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.tasks.v2 CloudTasks API.

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

        The resource has one pattern, but the API owner expects to add more
        later. (This is the inverse of ORIGINALLY_SINGLE_PATTERN, and prevents
        that from being necessary once there are multiple patterns.)

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].CreateQueue

    @property
    def update_queue(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.update_queue`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].UpdateQueue

    @property
    def delete_queue(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.delete_queue`.

        The mode for generating an ``Authorization`` header for HTTP
        requests.

        If specified, all ``Authorization`` headers in the
        ``HttpRequest.headers`` field will be overridden.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].PauseQueue

    @property
    def resume_queue(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.resume_queue`.

        If specified, an `OAuth
        token <https://developers.google.com/identity/protocols/OAuth2>`__ will
        be generated and attached as an ``Authorization`` header in the HTTP
        request.

        This type of authorization should generally only be used when calling
        Google APIs hosted on \*.googleapis.com.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].ResumeQueue

    @property
    def get_iam_policy(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.get_iam_policy`.

        Creates a queue.

        Queues created with this method allow tasks to live for a maximum of 31
        days. After a task is 31 days old, the task will be deleted regardless
        of whether it was dispatched or not.

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
        return self._stubs["cloud_tasks_stub"].GetIamPolicy

    @property
    def set_iam_policy(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.set_iam_policy`.

        The response_view specifies which subset of the ``Task`` will be
        returned.

        By default response_view is ``BASIC``; not all information is retrieved
        by default because some data, such as payloads, might be desirable to
        return only when needed because of its large size or because of the
        sensitivity of data that it contains.

        Authorization for ``FULL`` requires ``cloudtasks.tasks.fullView``
        `Google IAM <https://cloud.google.com/iam/>`__ permission on the
        ``Task`` resource.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].SetIamPolicy

    @property
    def test_iam_permissions(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.test_iam_permissions`.

        If specified, an
        `OIDC <https://developers.google.com/identity/protocols/OpenIDConnect>`__
        token will be generated and attached as an ``Authorization`` header in
        the HTTP request.

        This type of authorization can be used for many scenarios, including
        calling Cloud Run, or endpoints where you intend to validate the token
        yourself.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].TestIamPermissions

    @property
    def list_tasks(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.list_tasks`.

        Request message for ``CreateTask``.

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
        cannot be deleted if it has executed successfully or permanently
        failed.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].DeleteTask

    @property
    def run_task(self):
        """Return the gRPC stub for :meth:`CloudTasksClient.run_task`.

        Required. The queue name. For example:
        ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID``

        The queue must already exist.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["cloud_tasks_stub"].RunTask
