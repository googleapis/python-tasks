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
          RUNNING (int): A simple descriptor of a resource type.

          ResourceDescriptor annotates a resource message (either by means of a
          protobuf annotation or use in the service config), and associates the
          resource's schema, the resource type, and the pattern of the resource
          name.

          Example:

          ::

              message Topic {
                // Indicates this message defines a resource schema.
                // Declares the resource type in the format of {service}/{kind}.
                // For Kubernetes resources, the format is {api group}/{kind}.
                option (google.api.resource) = {
                  type: "pubsub.googleapis.com/Topic"
                  name_descriptor: {
                    pattern: "projects/{project}/topics/{topic}"
                    parent_type: "cloudresourcemanager.googleapis.com/Project"
                    parent_name_extractor: "projects/{project}"
                  }
                };
              }

          The ResourceDescriptor Yaml config will look like:

          ::

              resources:
              - type: "pubsub.googleapis.com/Topic"
                name_descriptor:
                  - pattern: "projects/{project}/topics/{topic}"
                    parent_type: "cloudresourcemanager.googleapis.com/Project"
                    parent_name_extractor: "projects/{project}"

          Sometimes, resources have multiple patterns, typically because they can
          live under multiple parents.

          Example:

          ::

              message LogEntry {
                option (google.api.resource) = {
                  type: "logging.googleapis.com/LogEntry"
                  name_descriptor: {
                    pattern: "projects/{project}/logs/{log}"
                    parent_type: "cloudresourcemanager.googleapis.com/Project"
                    parent_name_extractor: "projects/{project}"
                  }
                  name_descriptor: {
                    pattern: "folders/{folder}/logs/{log}"
                    parent_type: "cloudresourcemanager.googleapis.com/Folder"
                    parent_name_extractor: "folders/{folder}"
                  }
                  name_descriptor: {
                    pattern: "organizations/{organization}/logs/{log}"
                    parent_type: "cloudresourcemanager.googleapis.com/Organization"
                    parent_name_extractor: "organizations/{organization}"
                  }
                  name_descriptor: {
                    pattern: "billingAccounts/{billing_account}/logs/{log}"
                    parent_type: "billing.googleapis.com/BillingAccount"
                    parent_name_extractor: "billingAccounts/{billing_account}"
                  }
                };
              }

          The ResourceDescriptor Yaml config will look like:

          ::

              resources:
              - type: 'logging.googleapis.com/LogEntry'
                name_descriptor:
                  - pattern: "projects/{project}/logs/{log}"
                    parent_type: "cloudresourcemanager.googleapis.com/Project"
                    parent_name_extractor: "projects/{project}"
                  - pattern: "folders/{folder}/logs/{log}"
                    parent_type: "cloudresourcemanager.googleapis.com/Folder"
                    parent_name_extractor: "folders/{folder}"
                  - pattern: "organizations/{organization}/logs/{log}"
                    parent_type: "cloudresourcemanager.googleapis.com/Organization"
                    parent_name_extractor: "organizations/{organization}"
                  - pattern: "billingAccounts/{billing_account}/logs/{log}"
                    parent_type: "billing.googleapis.com/BillingAccount"
                    parent_name_extractor: "billingAccounts/{billing_account}"

          For flexible resources, the resource name doesn't contain parent names,
          but the resource itself has parents for policy evaluation.

          Example:

          ::

              message Shelf {
                option (google.api.resource) = {
                  type: "library.googleapis.com/Shelf"
                  name_descriptor: {
                    pattern: "shelves/{shelf}"
                    parent_type: "cloudresourcemanager.googleapis.com/Project"
                  }
                  name_descriptor: {
                    pattern: "shelves/{shelf}"
                    parent_type: "cloudresourcemanager.googleapis.com/Folder"
                  }
                };
              }

          The ResourceDescriptor Yaml config will look like:

          ::

              resources:
              - type: 'library.googleapis.com/Shelf'
                name_descriptor:
                  - pattern: "shelves/{shelf}"
                    parent_type: "cloudresourcemanager.googleapis.com/Project"
                  - pattern: "shelves/{shelf}"
                    parent_type: "cloudresourcemanager.googleapis.com/Folder"
          PAUSED (int): Tasks are paused by the user. If the queue is paused then Cloud
          Tasks will stop delivering tasks from it, but more tasks can
          still be added to it by the user.
          DISABLED (int): Request message for ``UpdateQueue``.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        PAUSED = 2
        DISABLED = 3


class Task(object):
    class View(enum.IntEnum):
        """
        The status code, which should be an enum value of
        ``google.rpc.Code``.

        Attributes:
          VIEW_UNSPECIFIED (int): Unspecified. Defaults to BASIC.
          BASIC (int): Request message for ``PauseQueue``.
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
