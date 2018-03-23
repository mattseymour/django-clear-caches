from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.cache import caches


class Command(BaseCommand):
    help = 'Clears cache entries for a defined set of keys.'

    def add_arguments(self, parser):

        parser.add_argument(
            '--list',
            action='store_true',
            dest='_list',
            help='List the cache keys available'
        )
        parser.add_argument(
            '--cache-name',
            action='append',
            dest='_cache_name',
            nargs='?',
            type=str,
            help='Remove a single defined cache entry. --cache-name can be '
                'passed multiple times'
        )
        parser.add_argument(
            '--all',
            action='store_true',
            dest='_all',
            help='Delete ALL keys from ALL django setting CACHES'
        )
        parser.add_argument(
            '-y',
            action='store_true',
            dest='_confirmed_deletion',
            help='Override warnings, delete all cache keyed items'
        )

    def delete_keys(self, keys):
        # Clear all keys from the list CACHES keys
        for key in keys:
            self.stdout.write(
                'clearing {} keys....'.format(key)
            )
            cache = caches[key]
            cache.clear()

    def handle(self, *args, **options):
        if options['_list']:
            self.stdout.write(
                '\n'.join(settings.CACHES.keys())
            )
            return

        if options['_cache_name'] and options['_all']:
            raise CommandError('List either a list of --cache_name or --all.')

        if options['_cache_name']:
            names = set(options['_cache_name'])
            keys = set(settings.CACHES.keys())

            valid = names.intersection(keys)
            invalid_names = names.difference(valid)

            self.print_invalid_cache_entries(invalid_names)

            self.delete_keys(list(valid))

        if options['_all']:
            if options['_confirmed_deletion']:
                self.stdout.write('Clearing all caches')
                self.delete_keys(settings.CACHES.keys())
            else:
                self.stdout.write(
                    self.style.NOTICE(
                        'Clearing all caches, this could be dangerous? '
                        'Run with -y flag to continue'
                    )
                )

    def print_invalid_cache_entries(self, invalid_names):
        """
        Print out a list of caches which are not valid settings.CACHES
        :param invalid_names: [<str>,] | {<str>,}
        :return: None
        """
        if not invalid_names:
            return

        self.stdout.write(
            self.style.NOTICE(
                'The following keys will not be cleared from cache. '
                'There are no matching CACHES key for: \n'
            )
        )

        # print out to the user the caches which are invalid and will
        # not be cleared.

        for _invalid_name in invalid_names:
            self.stdout.write(
                self.style.NOTICE(' * {}'.format(_invalid_name))
            )