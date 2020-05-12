#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Modules.Cms.SecCms import SecCmsRemoteCodeExecutionV6_45
from Modules.Cms.SecCms import SecCmsRemoteCodeExecutionV6_54
from Modules.Cms.SecCms import SecCmsRemoteCodeExecutionV6_55
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,proxies,**kwargs):
    ThreadPool.Append(SecCmsRemoteCodeExecutionV6_45.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(SecCmsRemoteCodeExecutionV6_54.medusa, Url,Values,proxies=proxies,**kwargs)
    ThreadPool.Append(SecCmsRemoteCodeExecutionV6_55.medusa, Url,Values,proxies=proxies,**kwargs)
    Prompt("SecCms")
