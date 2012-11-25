# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import setuptools

from cinder.openstack.common import setup as common_setup
from cinder import version

requires = common_setup.parse_requirements()

setuptools.setup(
    name='cinder',
    version=version.canonical_version_string(),
    description='block storage service',
    author='OpenStack',
    author_email='cinder@lists.launchpad.net',
    url='http://www.openstack.org/',
    classifiers=[
        'Environment :: OpenStack',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    cmdclass=common_setup.get_cmdclass(),
    packages=setuptools.find_packages(exclude=['bin', 'smoketests']),
    install_requires=requires,
    include_package_data=True,
    test_suite='nose.collector',
    setup_requires=['setuptools_git>=0.4'],
    scripts=['bin/cinder-all',
             'bin/cinder-api',
             'bin/cinder-clear-rabbit-queues',
             'bin/cinder-manage',
             'bin/cinder-rootwrap',
             'bin/cinder-scheduler',
             'bin/cinder-volume',
             'bin/cinder-volume-usage-audit'],
    py_modules=[])
