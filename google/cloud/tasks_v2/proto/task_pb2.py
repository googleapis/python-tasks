# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/tasks_v2/proto/task.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.tasks_v2.proto import (
    target_pb2 as google_dot_cloud_dot_tasks__v2_dot_proto_dot_target__pb2,
)
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/tasks_v2/proto/task.proto",
    package="google.cloud.tasks.v2",
    syntax="proto3",
    serialized_options=b"\n\031com.google.cloud.tasks.v2B\tTaskProtoP\001Z:google.golang.org/genproto/googleapis/cloud/tasks/v2;tasks",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n&google/cloud/tasks_v2/proto/task.proto\x12\x15google.cloud.tasks.v2\x1a\x19google/api/resource.proto\x1a(google/cloud/tasks_v2/proto/target.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x1cgoogle/api/annotations.proto"\xb4\x05\n\x04Task\x12\x0c\n\x04name\x18\x01 \x01(\t\x12N\n\x17\x61pp_engine_http_request\x18\x02 \x01(\x0b\x32+.google.cloud.tasks.v2.AppEngineHttpRequestH\x00\x12:\n\x0chttp_request\x18\x03 \x01(\x0b\x32".google.cloud.tasks.v2.HttpRequestH\x00\x12\x31\n\rschedule_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x11\x64ispatch_deadline\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x16\n\x0e\x64ispatch_count\x18\x07 \x01(\x05\x12\x16\n\x0eresponse_count\x18\x08 \x01(\x05\x12\x35\n\rfirst_attempt\x18\t \x01(\x0b\x32\x1e.google.cloud.tasks.v2.Attempt\x12\x34\n\x0clast_attempt\x18\n \x01(\x0b\x32\x1e.google.cloud.tasks.v2.Attempt\x12.\n\x04view\x18\x0b \x01(\x0e\x32 .google.cloud.tasks.v2.Task.View"1\n\x04View\x12\x14\n\x10VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05\x42\x41SIC\x10\x01\x12\x08\n\x04\x46ULL\x10\x02:h\xea\x41\x65\n\x1e\x63loudtasks.googleapis.com/Task\x12\x43projects/{project}/locations/{location}/queues/{queue}/tasks/{task}B\x0e\n\x0cmessage_type"\xcf\x01\n\x07\x41ttempt\x12\x31\n\rschedule_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rdispatch_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rresponse_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x0fresponse_status\x18\x04 \x01(\x0b\x32\x12.google.rpc.StatusBd\n\x19\x63om.google.cloud.tasks.v2B\tTaskProtoP\x01Z:google.golang.org/genproto/googleapis/cloud/tasks/v2;tasksb\x06proto3',
    dependencies=[
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_tasks__v2_dot_proto_dot_target__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_rpc_dot_status__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_TASK_VIEW = _descriptor.EnumDescriptor(
    name="View",
    full_name="google.cloud.tasks.v2.Task.View",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="VIEW_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="BASIC",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="FULL",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=776,
    serialized_end=825,
)
_sym_db.RegisterEnumDescriptor(_TASK_VIEW)


_TASK = _descriptor.Descriptor(
    name="Task",
    full_name="google.cloud.tasks.v2.Task",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.tasks.v2.Task.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="app_engine_http_request",
            full_name="google.cloud.tasks.v2.Task.app_engine_http_request",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="http_request",
            full_name="google.cloud.tasks.v2.Task.http_request",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="schedule_time",
            full_name="google.cloud.tasks.v2.Task.schedule_time",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="create_time",
            full_name="google.cloud.tasks.v2.Task.create_time",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="dispatch_deadline",
            full_name="google.cloud.tasks.v2.Task.dispatch_deadline",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="dispatch_count",
            full_name="google.cloud.tasks.v2.Task.dispatch_count",
            index=6,
            number=7,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="response_count",
            full_name="google.cloud.tasks.v2.Task.response_count",
            index=7,
            number=8,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="first_attempt",
            full_name="google.cloud.tasks.v2.Task.first_attempt",
            index=8,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="last_attempt",
            full_name="google.cloud.tasks.v2.Task.last_attempt",
            index=9,
            number=10,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="view",
            full_name="google.cloud.tasks.v2.Task.view",
            index=10,
            number=11,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_TASK_VIEW],
    serialized_options=b"\352Ae\n\036cloudtasks.googleapis.com/Task\022Cprojects/{project}/locations/{location}/queues/{queue}/tasks/{task}",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="message_type",
            full_name="google.cloud.tasks.v2.Task.message_type",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        )
    ],
    serialized_start=255,
    serialized_end=947,
)


_ATTEMPT = _descriptor.Descriptor(
    name="Attempt",
    full_name="google.cloud.tasks.v2.Attempt",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="schedule_time",
            full_name="google.cloud.tasks.v2.Attempt.schedule_time",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="dispatch_time",
            full_name="google.cloud.tasks.v2.Attempt.dispatch_time",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="response_time",
            full_name="google.cloud.tasks.v2.Attempt.response_time",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="response_status",
            full_name="google.cloud.tasks.v2.Attempt.response_status",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=950,
    serialized_end=1157,
)

_TASK.fields_by_name[
    "app_engine_http_request"
].message_type = (
    google_dot_cloud_dot_tasks__v2_dot_proto_dot_target__pb2._APPENGINEHTTPREQUEST
)
_TASK.fields_by_name[
    "http_request"
].message_type = google_dot_cloud_dot_tasks__v2_dot_proto_dot_target__pb2._HTTPREQUEST
_TASK.fields_by_name[
    "schedule_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TASK.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TASK.fields_by_name[
    "dispatch_deadline"
].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TASK.fields_by_name["first_attempt"].message_type = _ATTEMPT
_TASK.fields_by_name["last_attempt"].message_type = _ATTEMPT
_TASK.fields_by_name["view"].enum_type = _TASK_VIEW
_TASK_VIEW.containing_type = _TASK
_TASK.oneofs_by_name["message_type"].fields.append(
    _TASK.fields_by_name["app_engine_http_request"]
)
_TASK.fields_by_name["app_engine_http_request"].containing_oneof = _TASK.oneofs_by_name[
    "message_type"
]
_TASK.oneofs_by_name["message_type"].fields.append(_TASK.fields_by_name["http_request"])
_TASK.fields_by_name["http_request"].containing_oneof = _TASK.oneofs_by_name[
    "message_type"
]
_ATTEMPT.fields_by_name[
    "schedule_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ATTEMPT.fields_by_name[
    "dispatch_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ATTEMPT.fields_by_name[
    "response_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ATTEMPT.fields_by_name[
    "response_status"
].message_type = google_dot_rpc_dot_status__pb2._STATUS
DESCRIPTOR.message_types_by_name["Task"] = _TASK
DESCRIPTOR.message_types_by_name["Attempt"] = _ATTEMPT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Task = _reflection.GeneratedProtocolMessageType(
    "Task",
    (_message.Message,),
    {
        "DESCRIPTOR": _TASK,
        "__module__": "google.cloud.tasks_v2.proto.task_pb2",
        "__doc__": """A unit of scheduled work.
  Attributes:
      name:
          Optionally caller-specified in
          [CreateTask][google.cloud.tasks.v2.CloudTasks.CreateTask].
          The task name.  The task name must have the following format: 
          ``projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/ta
          sks/TASK_ID``  -  ``PROJECT_ID`` can contain letters
          ([A-Za-z]), numbers ([0-9]),    hyphens (-), colons (:), or
          periods (.). For more information, see    `Identifying
          projects <https://cloud.google.com/resource-
          manager/docs/creating-managing-
          projects#identifying_projects>`_ -  ``LOCATION_ID`` is the
          canonical ID for the task’s location. The list    of available
          locations can be obtained by calling    [ListLocations][google
          .cloud.location.Locations.ListLocations]. For    more
          information, see https://cloud.google.com/about/locations/. -
          ``QUEUE_ID`` can contain letters ([A-Za-z]), numbers ([0-9]),
          or    hyphens (-). The maximum length is 100 characters. -
          ``TASK_ID`` can contain only letters ([A-Za-z]), numbers
          ([0-9]),    hyphens (-), or underscores (_). The maximum
          length is 500    characters.
      message_type:
          Required. The message to send to the worker.
      app_engine_http_request:
          HTTP request that is sent to the App Engine app handler.  An
          App Engine task is a task that has [AppEngineHttpRequest][goog
          le.cloud.tasks.v2.AppEngineHttpRequest] set.
      http_request:
          HTTP request that is sent to the worker.  An HTTP task is a
          task that has [HttpRequest][google.cloud.tasks.v2.HttpRequest]
          set.
      schedule_time:
          The time when the task is scheduled to be attempted or
          retried.  ``schedule_time`` will be truncated to the nearest
          microsecond.
      create_time:
          Output only. The time that the task was created.
          ``create_time`` will be truncated to the nearest second.
      dispatch_deadline:
          The deadline for requests sent to the worker. If the worker
          does not respond by this deadline then the request is
          cancelled and the attempt is marked as a ``DEADLINE_EXCEEDED``
          failure. Cloud Tasks will retry the task according to the
          [RetryConfig][google.cloud.tasks.v2.RetryConfig].  Note that
          when the request is cancelled, Cloud Tasks will stop listing
          for the response, but whether the worker stops processing
          depends on the worker. For example, if the worker is stuck, it
          may not react to cancelled requests.  The default and maximum
          values depend on the type of request:  -  For [HTTP
          tasks][google.cloud.tasks.v2.HttpRequest], the default is
          10 minutes. The deadline must be in the interval [15 seconds,
          30    minutes].  -  For [App Engine
          tasks][google.cloud.tasks.v2.AppEngineHttpRequest], 0
          indicates that the request has the default deadline. The
          default    deadline depends on the `scaling    type
          <https://cloud.google.com/appengine/docs/standard/go/how-
          instances-are-managed#instance_scaling>`_    of the service:
          10 minutes for standard apps with automatic scaling,    24
          hours for standard apps with manual and basic scaling, and 60
          minutes for flex apps. If the request deadline is set, it must
          be in    the interval [15 seconds, 24 hours 15 seconds].
          Regardless of the    task’s ``dispatch_deadline``, the app
          handler will not run for longer    than than the service’s
          timeout. We recommend setting the    ``dispatch_deadline`` to
          at most a few seconds more than the app    handler’s timeout.
          For more information see    `Timeouts
          <https://cloud.google.com/tasks/docs/creating-appengine-
          handlers#timeouts>`_.  ``dispatch_deadline`` will be
          truncated to the nearest millisecond. The deadline is an
          approximate deadline.
      dispatch_count:
          Output only. The number of attempts dispatched.  This count
          includes attempts which have been dispatched but haven’t
          received a response.
      response_count:
          Output only. The number of attempts which have received a
          response.
      first_attempt:
          Output only. The status of the task’s first attempt.  Only
          [dispatch_time][google.cloud.tasks.v2.Attempt.dispatch_time]
          will be set. The other
          [Attempt][google.cloud.tasks.v2.Attempt] information is not
          retained by Cloud Tasks.
      last_attempt:
          Output only. The status of the task’s last attempt.
      view:
          Output only. The view specifies which subset of the
          [Task][google.cloud.tasks.v2.Task] has been returned.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.tasks.v2.Task)
    },
)
_sym_db.RegisterMessage(Task)

Attempt = _reflection.GeneratedProtocolMessageType(
    "Attempt",
    (_message.Message,),
    {
        "DESCRIPTOR": _ATTEMPT,
        "__module__": "google.cloud.tasks_v2.proto.task_pb2",
        "__doc__": """The status of a task attempt.
  Attributes:
      schedule_time:
          Output only. The time that this attempt was scheduled.
          ``schedule_time`` will be truncated to the nearest
          microsecond.
      dispatch_time:
          Output only. The time that this attempt was dispatched.
          ``dispatch_time`` will be truncated to the nearest
          microsecond.
      response_time:
          Output only. The time that this attempt response was received.
          ``response_time`` will be truncated to the nearest
          microsecond.
      response_status:
          Output only. The response from the worker for this attempt.
          If ``response_time`` is unset, then the task has not been
          attempted or is currently running and the ``response_status``
          field is meaningless.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.tasks.v2.Attempt)
    },
)
_sym_db.RegisterMessage(Attempt)


DESCRIPTOR._options = None
_TASK._options = None
# @@protoc_insertion_point(module_scope)
