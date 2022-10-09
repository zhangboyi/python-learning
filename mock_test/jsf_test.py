#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/8/30 23:27
# @Author:boyizhang
import json

from jsf import JSF

faker = JSF.from_json("request_json_schema.json")
fake_json = faker.generate()
print(json.dumps(fake_json))

from faker_schema.faker_schema import FakerSchema

schema = {'employee_id': 'uuid4', 'employee_name': 'name', 'employee address': 'address',
          'email_address': 'email'}


schema = {'EmployeeInfo': {'ID': 'uuid4', 'Name': 'name', 'Contact': {'Email': 'email',
          'Phone Number': 'phone_number'}, 'Location': {'Country Code': 'country_code',
          'City': 'city', 'Country': 'country', 'Postal Code': 'postalcode',
          'Address': 'street_address'}}}
faker = FakerSchema()
data = faker.generate_fake(schema)
print(json.dumps(data))
# {'employee_id': '956f0cf3-a954-5bff-0aaf-ee0e1b7e1e1b', 'employee_name': 'Adam Wells',
#  'employee address': '189 Kyle Springs Suite 110\nNorth Robin, OR 73512',
#  'email_address': 'jmcgee@gmail.com'}

from hypothesis_jsonschema import from_schema
schema = '{"type": "integer", "minimum": 1, "exclusiveMaximum": 10}'
data = from_schema(schema)
print(data)
