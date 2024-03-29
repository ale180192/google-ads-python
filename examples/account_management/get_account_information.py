#!/usr/bin/env python
# Copyright 2018 Google LLC
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
"""This example lists information about an advertising account.

For example, its name, currency, time zone, etc.
"""

from __future__ import absolute_import
import pdb
pdb.set_trace()

import argparse
import six
import sys

import google.ads.google_ads.client


def main(client, customer_id):
    print('call main')
    pdb.set_trace()
    customer_service = client.get_service('CustomerService', version='v2')
    print('ok customer_service', customer_service)
    resource_name = customer_service.customer_path(customer_id)
    print('ok')
    try:
        customer = customer_service.get_customer(resource_name=resource_name)
        print('customer', customer)
    except google.ads.google_ads.errors.GoogleAdsException as ex:
        print('Request with ID "%s" failed with status "%s" and includes the '
              'following errors:' % (ex.request_id, ex.error.code().name))
        for error in ex.failure.errors:
            print('\tError with message "%s".' % error.message)
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print('\t\tOn field: %s' % field_path_element.field_name)
        sys.exit(1)

    print('Customer ID: %d' % customer.id.value)
    print('\tDescriptive name: %s' % customer.descriptive_name.value)
    print('\tCurrency code: %s' % customer.currency_code.value)
    print('\tTime zone: %s' % customer.time_zone.value)
    print('\tTracking URL template: %s' % customer.tracking_url_template.value)
    print('\tAuto tagging enabled: %s' % customer.auto_tagging_enabled)


if __name__ == '__main__':
    # GoogleAdsClient will read the google-ads.yaml configuration file in the
    # home directory if none is specified.
    path = '/home/ale/google-ads-python/google-ads.yaml'
    print('ok path', path)
    google_ads_client = (google.ads.google_ads.client.GoogleAdsClient
                         .load_from_storage(path=path))
    
    main(google_ads_client, '3573039576')
