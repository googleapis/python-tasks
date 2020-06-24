# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/tasks_v2beta2/proto/task.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.tasks_v2beta2.proto import (
    target_pb2 as google_dot_cloud_dot_tasks__v2beta2_dot_proto_dot_target__pb2,
)
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/tasks_v2beta2/proto/task.proto",
    package="google.cloud.tasks.v2beta2",
    syntax="proto3",
    serialized_options=b"\n\036com.google.cloud.tasks.v2beta2B\tTaskProtoP\001Z?google.golang.org/genproto/googleapis/cloud/tasks/v2beta2;tasks",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n+google/cloud/tasks_v2beta2/proto/task.proto\x12\x1agoogle.cloud.tasks.v2beta2\x1a\x19google/api/resource.proto\x1a-google/cloud/tasks_v2beta2/proto/target.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x1cgoogle/api/annotations.proto"\xa8\x04\n\x04Task\x12\x0c\n\x04name\x18\x01 \x01(\t\x12S\n\x17\x61pp_engine_http_request\x18\x03 \x01(\x0b\x32\x30.google.cloud.tasks.v2beta2.AppEngineHttpRequestH\x00\x12?\n\x0cpull_message\x18\x04 \x01(\x0b\x32\'.google.cloud.tasks.v2beta2.PullMessageH\x00\x12\x31\n\rschedule_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x63reate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x06status\x18\x07 \x01(\x0b\x32&.google.cloud.tasks.v2beta2.TaskStatus\x12\x33\n\x04view\x18\x08 \x01(\x0e\x32%.google.cloud.tasks.v2beta2.Task.View"1\n\x04View\x12\x14\n\x10VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05\x42\x41SIC\x10\x01\x12\x08\n\x04\x46ULL\x10\x02:h\xea\x41\x65\n\x1e\x63loudtasks.googleapis.com/Task\x12\x43projects/{project}/locations/{location}/queues/{queue}/tasks/{task}B\x0e\n\x0cpayload_type"\xdd\x01\n\nTaskStatus\x12\x1e\n\x16\x61ttempt_dispatch_count\x18\x01 \x01(\x05\x12\x1e\n\x16\x61ttempt_response_count\x18\x02 \x01(\x05\x12G\n\x14\x66irst_attempt_status\x18\x03 \x01(\x0b\x32).google.cloud.tasks.v2beta2.AttemptStatus\x12\x46\n\x13last_attempt_status\x18\x04 \x01(\x0b\x32).google.cloud.tasks.v2beta2.AttemptStatus"\xd5\x01\n\rAttemptStatus\x12\x31\n\rschedule_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rdispatch_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rresponse_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x0fresponse_status\x18\x04 \x01(\x0b\x32\x12.google.rpc.StatusBn\n\x1e\x63om.google.cloud.tasks.v2beta2B\tTaskProtoP\x01Z?google.golang.org/genproto/googleapis/cloud/tasks/v2beta2;tasksb\x06proto3',
    dependencies=[
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_tasks__v2beta2_dot_proto_dot_target__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_rpc_dot_status__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_TASK_VIEW = _descriptor.EnumDescriptor(
    name="View",
    full_name="google.cloud.tasks.v2beta2.Task.View",
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
    serialized_start=619,
    serialized_end=668,
)
_sym_db.RegisterEnumDescriptor(_TASK_VIEW)


_TASK = _descriptor.Descriptor(
    name="Task",
    full_name="google.cloud.tasks.v2beta2.Task",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.tasks.v2beta2.Task.name",
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
            full_name="google.cloud.tasks.v2beta2.Task.app_engine_http_request",
            index=1,
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
            name="pull_message",
            full_name="google.cloud.tasks.v2beta2.Task.pull_message",
            index=2,
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
            name="schedule_time",
            full_name="google.cloud.tasks.v2beta2.Task.schedule_time",
            index=3,
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
            name="create_time",
            full_name="google.cloud.tasks.v2beta2.Task.create_time",
            index=4,
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
            name="status",
            full_name="google.cloud.tasks.v2beta2.Task.status",
            index=5,
            number=7,
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
            full_name="google.cloud.tasks.v2beta2.Task.view",
            index=6,
            number=8,
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
    enum_types=[_TASK_VIEW,],
    serialized_options=b"\352Ae\n\036cloudtasks.googleapis.com/Task\022Cprojects/{project}/locations/{location}/queues/{queue}/tasks/{task}",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="payload_type",
            full_name="google.cloud.tasks.v2beta2.Task.payload_type",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=238,
    serialized_end=790,
)


_TASKSTATUS = _descriptor.Descriptor(
    name="TaskStatus",
    full_name="google.cloud.tasks.v2beta2.TaskStatus",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="attempt_dispatch_count",
            full_name="google.cloud.tasks.v2beta2.TaskStatus.attempt_dispatch_count",
            index=0,
            number=1,
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
            name="attempt_response_count",
            full_name="google.cloud.tasks.v2beta2.TaskStatus.attempt_response_count",
            index=1,
            number=2,
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
            name="first_attempt_status",
            full_name="google.cloud.tasks.v2beta2.TaskStatus.first_attempt_status",
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
            name="last_attempt_status",
            full_name="google.cloud.tasks.v2beta2.TaskStatus.last_attempt_status",
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
    serialized_start=793,
    serialized_end=1014,
)


_ATTEMPTSTATUS = _descriptor.Descriptor(
    name="AttemptStatus",
    full_name="google.cloud.tasks.v2beta2.AttemptStatus",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="schedule_time",
            full_name="google.cloud.tasks.v2beta2.AttemptStatus.schedule_time",
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
            full_name="google.cloud.tasks.v2beta2.AttemptStatus.dispatch_time",
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
            full_name="google.cloud.tasks.v2beta2.AttemptStatus.response_time",
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
            full_name="google.cloud.tasks.v2beta2.AttemptStatus.response_status",
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
    serialized_start=1017,
    serialized_end=1230,
)

_TASK.fields_by_name[
    "app_engine_http_request"
].message_type = (
    google_dot_cloud_dot_tasks__v2beta2_dot_proto_dot_target__pb2._APPENGINEHTTPREQUEST
)
_TASK.fields_by_name[
    "pull_message"
].message_type = (
    google_dot_cloud_dot_tasks__v2beta2_dot_proto_dot_target__pb2._PULLMESSAGE
)
_TASK.fields_by_name[
    "schedule_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TASK.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TASK.fields_by_name["status"].message_type = _TASKSTATUS
_TASK.fields_by_name["view"].enum_type = _TASK_VIEW
_TASK_VIEW.containing_type = _TASK
_TASK.oneofs_by_name["payload_type"].fields.append(
    _TASK.fields_by_name["app_engine_http_request"]
)
_TASK.fields_by_name["app_engine_http_request"].containing_oneof = _TASK.oneofs_by_name[
    "payload_type"
]
_TASK.oneofs_by_name["payload_type"].fields.append(_TASK.fields_by_name["pull_message"])
_TASK.fields_by_name["pull_message"].containing_oneof = _TASK.oneofs_by_name[
    "payload_type"
]
_TASKSTATUS.fields_by_name["first_attempt_status"].message_type = _ATTEMPTSTATUS
_TASKSTATUS.fields_by_name["last_attempt_status"].message_type = _ATTEMPTSTATUS
_ATTEMPTSTATUS.fields_by_name[
    "schedule_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ATTEMPTSTATUS.fields_by_name[
    "dispatch_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ATTEMPTSTATUS.fields_by_name[
    "response_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ATTEMPTSTATUS.fields_by_name[
    "response_status"
].message_type = google_dot_rpc_dot_status__pb2._STATUS
DESCRIPTOR.message_types_by_name["Task"] = _TASK
DESCRIPTOR.message_types_by_name["TaskStatus"] = _TASKSTATUS
DESCRIPTOR.message_types_by_name["AttemptStatus"] = _ATTEMPTSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Task = _reflection.GeneratedProtocolMessageType(
    "Task",
    (_message.Message,),
    {
        "DESCRIPTOR": _TASK,
        "__module__": "google.cloud.tasks_v2beta2.proto.task_pb2",
        "__doc__": """A unit of scheduled work.
  
  Attributes:
      name:
          Optionally caller-specified in [CreateTask][google.cloud.tasks
          .v2beta2.CloudTasks.CreateTask].  The task name.  The task
          name must have the following format: ``projects/PROJECT_ID/loc
          ations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID``  -
          ``PROJECT_ID`` can contain letters ([A-Za-z]), numbers
          ([0-9]),    hyphens (-), colons (:), or periods (.). For more
          information, see    `Identifying    projects
          <https://cloud.google.com/resource-manager/docs/creating-
          managing-projects#identifying_projects>`_ -  ``LOCATION_ID``
          is the canonical ID for the task’s location. The list    of
          available locations can be obtained by calling    [ListLocatio
          ns][google.cloud.location.Locations.ListLocations]. For
          more information, see
          https://cloud.google.com/about/locations/. -  ``QUEUE_ID`` can
          contain letters ([A-Za-z]), numbers ([0-9]), or    hyphens
          (-). The maximum length is 100 characters. -  ``TASK_ID`` can
          contain only letters ([A-Za-z]), numbers ([0-9]),    hyphens
          (-), or underscores (_). The maximum length is 500
          characters.
      payload_type:
          Required.  The task’s payload is used by the task’s target to
          process the task. A payload is valid only if it is compatible
          with the queue’s target.
      app_engine_http_request:
          App Engine HTTP request that is sent to the task’s target. Can
          be set only if [app_engine_http_target][google.cloud.tasks.v2b
          eta2.Queue.app_engine_http_target] is set on the queue.  An
          App Engine task is a task that has [AppEngineHttpRequest][goog
          le.cloud.tasks.v2beta2.AppEngineHttpRequest] set.
      pull_message:
          [LeaseTasks][google.cloud.tasks.v2beta2.CloudTasks.LeaseTasks]
          to process the task. Can be set only if
          [pull_target][google.cloud.tasks.v2beta2.Queue.pull_target] is
          set on the queue.  A pull task is a task that has
          [PullMessage][google.cloud.tasks.v2beta2.PullMessage] set.
      schedule_time:
          The time when the task is scheduled to be attempted.  For App
          Engine queues, this is when the task will be attempted or
          retried.  For pull queues, this is the time when the task is
          available to be leased; if a task is currently leased, this is
          the time when the current lease expires, that is, the time
          that the task was leased plus the [lease_duration][google.clou
          d.tasks.v2beta2.LeaseTasksRequest.lease_duration].
          ``schedule_time`` will be truncated to the nearest
          microsecond.
      create_time:
          Output only. The time that the task was created.
          ``create_time`` will be truncated to the nearest second.
      status:
          Output only. The task status.
      view:
          Output only. The view specifies which subset of the
          [Task][google.cloud.tasks.v2beta2.Task] has been returned.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.tasks.v2beta2.Task)
    },
)
_sym_db.RegisterMessage(Task)

TaskStatus = _reflection.GeneratedProtocolMessageType(
    "TaskStatus",
    (_message.Message,),
    {
        "DESCRIPTOR": _TASKSTATUS,
        "__module__": "google.cloud.tasks_v2beta2.proto.task_pb2",
        "__doc__": """Status of the task.
  
  Attributes:
      attempt_dispatch_count:
          Output only. The number of attempts dispatched.  This count
          includes attempts which have been dispatched but haven’t
          received a response.
      attempt_response_count:
          Output only. The number of attempts which have received a
          response.  This field is not calculated for [pull
          tasks][google.cloud.tasks.v2beta2.PullMessage].
      first_attempt_status:
          Output only. The status of the task’s first attempt.  Only [di
          spatch_time][google.cloud.tasks.v2beta2.AttemptStatus.dispatch
          _time] will be set. The other
          [AttemptStatus][google.cloud.tasks.v2beta2.AttemptStatus]
          information is not retained by Cloud Tasks.  This field is not
          calculated for [pull
          tasks][google.cloud.tasks.v2beta2.PullMessage].
      last_attempt_status:
          Output only. The status of the task’s last attempt.  This
          field is not calculated for [pull
          tasks][google.cloud.tasks.v2beta2.PullMessage].
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.tasks.v2beta2.TaskStatus)
    },
)
_sym_db.RegisterMessage(TaskStatus)

AttemptStatus = _reflection.GeneratedProtocolMessageType(
    "AttemptStatus",
    (_message.Message,),
    {
        "DESCRIPTOR": _ATTEMPTSTATUS,
        "__module__": "google.cloud.tasks_v2beta2.proto.task_pb2",
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
          Output only. The response from the target for this attempt.
          If the task has not been attempted or the task is currently
          running then the response status is unset.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.tasks.v2beta2.AttemptStatus)
    },
)
_sym_db.RegisterMessage(AttemptStatus)


DESCRIPTOR._options = None
_TASK._options = None
# @@protoc_insertion_point(module_scope)
