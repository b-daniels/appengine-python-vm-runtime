# Copyright 2016 Google Inc. All Rights Reserved.
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
from setuptools import find_packages
from setuptools import setup

setup(
    name='appengine-compat',
    version='0.6',
    description='Google App Engine-compatible Python libraries for Managed VMs',
    url='https://github.com/GoogleCloudPlatform/appengine-python-vm-runtime',
    author='Google',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    package_dir={'': 'exported_appengine_sdk'},
    include_package_data=True,
    packages=find_packages('exported_appengine_sdk', exclude=['lib.*']),
    # namespace_packages=['google'],  # This skips google/__init__.py
    install_requires=[
        'requests>=2.5.0',
        'webapp2>=2.5.2',
        'WebOb>=1.4',
        'PyYAML>=3.11'
    ]
)
