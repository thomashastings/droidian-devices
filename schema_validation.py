import yaml
import os
from schema import Or, Schema, SchemaError

device_schema = Schema({
    'manufacturer': str,
    'name': str,
    'codename': str,
    // TODO : support has to be changed from str to have values as community or official
    'support': str,
    'device_type': str,
    'halium_version': str,
    'fastboot_mode': str,
    'recovery_mode': str,
    'ab_slot': bool,
    'api_version': str,
    'arch': str,
    'droidian_release': Or(None, str),
    'droidian_required_build': {
        'rootfs_link': Or(None, str),
        'devtools_link': Or(None, str),
    },
    'android': {
        'link':  Or(None, str),
        'text':  Or(None, str),
        'filename': Or(None, str),
        },
    'vendor_zip': {
        'link': Or(None, str),
        'text': Or(None, str),
        'filename': Or(None, str),
        },
    'vendor_image': {
        'link': Or(None, str),
        'text': Or(None, str),
        'filename':  Or(None, str),
        },
    'boot': {
        'link': Or(None, str),
        'text': Or(None, str),
        'filename': Or(None, str),
        },
    'recovery': {
        'name': str,
        'link': str,
        'text': str,
        'filename': str,
        'must_flash': Or(None, bool),
        },
    'adaptation': {
        'link': Or(None, str),
        'text': Or(None, str),
        'filename': Or(None, str),
        },
    'statuspage': Or(None, str),
    'contact': Or({
        'text': Or(None, str),
        'link': Or(None, str),
        }, None),
    'credit': [
            {
            'name': Or(None, str),
            'link': Or(None, str),
            },
        ],
    'command':
        Or([
        Or(None, str)
        ], None),
    'notes': Or([
        {
        'title': Or(None, str),
        'text': Or(None, str),
        }
    ], None)
    })

def validate_file(file): 
    try:
        device_schema.validate(file)
        print(f"Device configuration is valid for {file['codename']}.")
        return True
    except SchemaError as se:
        print('Error in', file['codename'])
        print(se)
        return False