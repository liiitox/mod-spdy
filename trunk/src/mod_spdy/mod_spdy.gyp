# Copyright 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

{
  'targets': [
    {
      'target_name': 'spdy_common',
      'type': '<(library)',
      'dependencies': [
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/net/net.gyp:instaweb_util',
        '<(DEPTH)/net/net.gyp:spdy',
      ],
      'include_dirs': [
        '<(DEPTH)',
      ],
      'export_dependent_settings': [
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/net/net.gyp:spdy',
      ],
      'sources': [
        'common/connection_context.cc',
        'common/executor.cc',
        'common/header_populator_interface.cc',
        'common/http_stream_visitor_interface.cc',
        'common/input_stream_interface.cc',
        'common/queued_worker_pool_executor.cc',
        'common/spdy_connection.cc',
        'common/spdy_connection_io.cc',
        'common/spdy_frame_priority_queue.cc',
        'common/spdy_frame_pump.cc',
        'common/spdy_frame_queue.cc',
        'common/spdy_server_config.cc',
        'common/spdy_stream.cc',
        'common/spdy_stream_distributor.cc',
        'common/spdy_stream_task_factory.cc',
        'common/spdy_to_http_converter.cc',
      ],
    },
    {
      'target_name': 'spdy_apache',
      'type': '<(library)',
      'dependencies': [
        'spdy_common',
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/third_party/apache/httpd/httpd.gyp:include',
      ],
      'include_dirs': [
        '<(DEPTH)',
      ],
      'export_dependent_settings': [
        'spdy_common',
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/third_party/apache/httpd/httpd.gyp:include',
      ],
      'sources': [
        'apache/apache_spdy_connection_io.cc',
        'apache/apache_spdy_stream_task_factory.cc',
        'apache/apr_thread_pool_executor.cc',
        'apache/brigade_output_stream.cc',
        'apache/config_commands.cc',
        'apache/config_util.cc',
        'apache/filters/http_to_spdy_filter.cc',
        'apache/filters/spdy_to_http_filter.cc',
        'apache/http_stream_accumulator.cc',
        'apache/input_filter_input_stream.cc',
        'apache/inspect.cc',
        'apache/log_message_handler.cc',
        'apache/response_header_populator.cc',
      ],
    },
    {
      'target_name': 'mod_spdy',
      'type': 'loadable_module',
      'dependencies': [
        'spdy_apache',
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/net/net.gyp:spdy',
        '<(DEPTH)/third_party/apache/httpd/httpd.gyp:include',
      ],
      'include_dirs': [
        '<(DEPTH)',
      ],
      'sources': [
        'mod_spdy.cc',
      ],
      'conditions': [['OS == "mac"', {
        'xcode_settings': {
          # We must null out these two variables when building this target,
          # because it is a loadable_module (-bundle).
          'DYLIB_COMPATIBILITY_VERSION':'',
          'DYLIB_CURRENT_VERSION':'',
        }
      }]],
    },
    {
      'target_name': 'spdy_common_test',
      'type': 'executable',
      'dependencies': [
        'spdy_common',
        '<(DEPTH)/testing/gmock.gyp:gmock',
        '<(DEPTH)/testing/gtest.gyp:gtest',
        '<(DEPTH)/testing/gtest.gyp:gtest_main',
      ],
      'include_dirs': [
        '<(DEPTH)',
      ],
      'sources': [
        'common/header_populator_interface_test.cc',
        'common/spdy_connection_test.cc',
        'common/spdy_frame_priority_queue_test.cc',
        'common/spdy_frame_pump_test.cc',
        'common/spdy_frame_queue_test.cc',
        'common/spdy_stream_distributor_test.cc',
        'common/spdy_to_http_converter_test.cc',
      ],
    },
    {
      'target_name': 'spdy_apache_test',
      'type': 'executable',
      'dependencies': [
        'spdy_apache',
        '<(DEPTH)/testing/gtest.gyp:gtest',
        '<(DEPTH)/third_party/apache/apr/apr.gyp:apr',
        '<(DEPTH)/third_party/apache/aprutil/aprutil.gyp:aprutil',
      ],
      'include_dirs': [
        '<(DEPTH)',
      ],
      'sources': [
        'apache/filters/http_to_spdy_filter_test.cc',
        'apache/filters/spdy_to_http_filter_test.cc',
        'apache/pool_util_test.cc',
        'apache/testing/spdy_apache_test_main.cc',
      ],
    },
  ],
  # Spdyget has been disabled for now, due to incompatible changes in the
  # spdy_framer API.
#   'conditions': [
#     [ 'OS != "win"', {
#       'targets': [
#         {
#           'target_name': 'spdyget',
#           'type': 'executable',
#           'dependencies': [
#             '<(DEPTH)/base/base.gyp:base',
#             '<(DEPTH)/net/net.gyp:spdy',
#           ],
#           'include_dirs': [
#             '<(DEPTH)',
#           ],
#           'sources': [
#             'spdyget.cc',
#           ],
#         },
#       ],
#     }],
#   ],
}
