import json
import os

from django.core.management.base import BaseCommand
from frame.core.api.doc import SwaggerDoc
from settings import STATIC_FILES_ROOT,  TUOEN_DIR


class Command(BaseCommand):
    help = '生成接口文档到项目根目录的 api_docs.json 文件'
    json_file_name = "api_doc.json"
    abs_json_filename = os.sep.join([STATIC_FILES_ROOT, json_file_name])

    def add_arguments(self, parser):
        parser.add_argument('-c', '--category', help="enable enhance debug", default="")

    def handle(self, *args, **options):

        from frame.main import protocol
        print("the option is ", options)
        category = options.get("category", "")
        self.stdout.write(self.style.SUCCESS(f'正在生成{category} api_docs文档到{self.abs_json_filename}'))
        if category == "ump":
            services = [protocol.get_service(category)]
        else:
            services = protocol.get_services()
        swagger_doc = SwaggerDoc()
        for service in services:
            print("service --------------------", len(service.get_apis()), service)
            for api in service.get_apis():
                swagger_doc.generate_paths(api)

        json_data = {
            "basePath": swagger_doc.BASEPATH,
            "swagger": swagger_doc.VERSION,
            "schemes": swagger_doc.SCHEMES,
            "info": swagger_doc.HEAD_INFO,
            "tags": list(swagger_doc.tags),
            "paths": swagger_doc.paths,
        }
        # fix the chinese character garbled issue. --- by shun 20210729

        with open(self.abs_json_filename, 'w', encoding='utf-8') as f:
            f.write(json.dumps(json_data, ensure_ascii=False, indent=4))
        self.stdout.write(self.style.SUCCESS('文档生成完成'))
