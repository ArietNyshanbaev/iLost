from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freelancer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.main',name='main'),
    url(r'^check_activation$', 'main.views.check_activation',name='check_activation'),
    url(r'^report$', 'main.views.report',name='report'),
    url(r'^activate$', 'main.views.activate',name='activate'),
    url(r'^message$', 'main.views.message',name='message'),


    # url(r'^category/(?P<category_id>.+)$', 'main.views.category',name='category'),
    # url(r'^brand/(?P<brand_id>.+)$', 'main.views.brand',name='brand'),
    # url(r'^model/(?P<model_id>.+)$', 'main.views.model',name='model'),
    # url(r'^instance/(?P<instance_id>.+)$', 'main.views.instance',name='instance'),
    # url(r'^add_instance/phones$', 'main.views.add_instance_phones',name='add_instance_phones'),
    # url(r'^add_instance/notebooks$', 'main.views.add_instance_notebooks',name='add_instance_notebooks'),    
    #url(r'^signin$', 'main.views.signin',name='signin'),
    #url(r'^signup$', 'main.views.signup',name='signup'),
    #url(r'^signout$', 'main.views.signout',name='signout'),
)
