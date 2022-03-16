PC端B2C电商项目

前后端不分离！

前端页面主要使用HTML,CSS,JS,jQuery库.

后端开发用到的技术有Django框架.Mysql数据库.Redis数据库作为缓存和celery的中间人.图片存储使用的是FastDFS，为了提高性能所以将其部署在nginx上。
文字搜索主要用的是haystack框架和whoosh搜索引擎，还有jieba中文分词包.邮件发送和静态页面生成使用celery.

服务器部署用的是uWSGI和nginx.
