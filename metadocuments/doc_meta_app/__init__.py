from __future__ import absolute_import
from django.conf.urls import patterns, url

from meta import make_all_document_app


config = [{'name': 'billapp',
          'config': {'model':
                  {'concrete':
                      {'name': 'MyBill',
                       'from': 'doc_meta_app.models'},
                  },
                'views': [{'type': 'list'},
                        {'type': 'detail'},]}},
          {'name': 'receiptapp',
          'config': {'model':
                  {'concrete':
                      {'name': 'MyReceipt',
                       'from': 'doc_meta_app.models'},
                  },
                'views': [{'type': 'list'},
                        {'type': 'detail'},]}},
          {'name': 'documentapp',
          'config': {'model':
                  {'concrete':
                      {'name': 'MyDocument',
                       'from': 'doc_meta_app.models'},
                  },
                'views': [{'type': 'list'},
                        {'type': 'detail'},]}},]

applications = make_all_document_app(config)
urlpatterns = []

for application in applications:
    name = application.get('name')
    app = application.get('app')
    views = app['views']
    for view_name, view in views.items():
        globals()[view_name] = view
    urlpatterns += patterns(
        '',
        *app['urls']
    )

del view
del view_name
