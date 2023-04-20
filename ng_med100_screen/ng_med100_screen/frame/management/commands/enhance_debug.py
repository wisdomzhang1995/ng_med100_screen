# -*- coding: utf-8 -*-
# @File    : enhance_debug
# @Project : ifw_shun
# @Time    : 2021/6/29 10:05
"""                     
                                      /             
 __.  , , , _  _   __ ______  _    __/  __ ____  _, 
(_/|_(_(_/_</_/_)_(_)/ / / <_</_  (_/_ (_)/ / <_(_)_
                                                 /| 
                                                |/  
"""

import json

from django.core.management.base import BaseCommand

from frame.management.commands import DEBUG_KEY_EXPIRE_TIME
from frame.utils.redis.redisoperator import redis_sys


class Command(BaseCommand):
    help = """
            Enhance online debug, you gonna love it!
                            ---inspired by awesome shun.
            """

    EX_ARGS = ['thread_info', 'normalize', 'depth', 'output',
               'watch_explode', 'max_variable_length']

    def add_arguments(self, parser):
        parser.add_argument('-e', '--enable', action='store_true',
                            help="enable enhance debug")
        parser.add_argument('-t', '--thread_info', action='store_true',
                            help='On multi-threaded apps '
                                 'identify which thread '
                                 'are snooped in output')
        parser.add_argument('-n', '--normalize', action='store_true',
                            help='Remove all machine-related data (paths, '
                                 'timestamps, memory addresses) to compare with'
                                 ' other traces easily')

        parser.add_argument('-d', '--depth', type=int, help='recursive depth')
        parser.add_argument('-s', '--second', type=int, help='expire time(s)')
        parser.add_argument('-o', '--output', help='output 2 file')
        parser.add_argument('-m', '--max_variable_length',
                            help='Variables and exceptions get truncated to 100'
                                 ' characters by default. '
                                 'You can customize that', type=int)
        parser.add_argument('-w', '--watch_explode', nargs='+',
                            help='expand values to '
                                 'see all their '
                                 'attributes or items '
                                 'of lists/dictionaries')

    def handle(self, *args, **options):
        if options.get('enable'):
            expire_time = options.get('second')
            expire_time = expire_time if expire_time else DEBUG_KEY_EXPIRE_TIME
            redis_sys.set('awesome', 310, ex=expire_time)
            kwargs = {arg: options.get(arg) for arg in self.EX_ARGS if
                      options.get(arg)}
            redis_sys.set("awesome_kwargs", json.dumps(kwargs), ex=expire_time)

        kwargs = redis_sys.get("awesome_kwargs")
        kwargs = json.loads(kwargs) if kwargs else {}

        print(f'shun -------------------->input ex_kwargs: {kwargs} ')
