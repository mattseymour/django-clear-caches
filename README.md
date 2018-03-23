# Django-Clear-Cache

A management command to clear a django CACHES store as defined in the django setting `CACHES`.

## Warnings

This management command does a cache clear (removes all cached entries within the defined store). Dropping the cache without fully understanding its consequences is potentially harmful to your system stability. Make sure you understand what you are doing before running this command.

## Usage

### Adding to django

In django settings add to the INSTALLED_APPS, `'clear-caches'`.

### Parameters

`--list` - List of CACHES keys
`--cache-name` - Clear the cache of a single CACHES key
`--all` - Clear all cache entries for all CACHES keys
`-y` - Used with `--all` as a command line confirmation of clearing all keys

### Example Usage

_List me the CACHES keys_

    > python manage.py clear_cache --list
    
    < default
    < data

_Clear a single CACHES key_

    > python manage.py clear_cache --cache-name default

_Clear multiple CACHES keys_

    > python manage.py clear_cache --cache-name default --cache-name data


_Clear all CACHES keys_

    > python manage.py clear_cache --all -y
