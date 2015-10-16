import httplib
import keystoneclient.v2_0.client as ksclient

h = httplib.HTTPConnection("172.16.0.2:9292")
keystone = ksclient.Client(auth_url="http://172.16.0.2:5000/v2.0",
                                       username="admin",
                                       password="admin",
                                       tenant_name="admin")
auth_token = keystone.auth_token

h.request('GET', '/v2/images/0f162570-a242-4c31-bc0f-f5242b25eda1/file', '', {"x-auth-token":auth_token})
response = h.getresponse()
destination = open('/home/krishna/Downloads/centos.qcow2', 'wb+')
destination.write(response.read())
destination.close()

# class CustomRequest(object):
#     def __init__(self, request_type, header_content, payload, full_path):
#         self.request_type = request_type
#         self.header_content = header_content
#         self.payload = payload
#         self.full_path = full_path
#
#     def send_request(self):
#         # h = httplib.HTTPConnection("127.0.0.1:8000")
#         h = httplib.HTTPConnection("169.53.139.163")
#         h.request(self.request_type, self.full_path, self.payload, self.header_content)
#         return h.getresponse()
#
#
# # Gateway Login
# headersContent = {"Accept":"application/json"}
# request_body = '{"ConsumerNumber":"sreehari.parameswaran@cognizant.com","SmartKey":"demo"}'
#
# obj = CustomRequest('POST', headersContent, request_body, '/gateway/login/')
# # print obj.send_request().msg
# response = obj.send_request()
# print response.read()
# auth_token = response.msg['x-a12n']
# # auth_token = 'adsfadsfs'
# print 'auth_token: '+auth_token
# #
# #
# # upload video
# headersContent = {"Content-Disposition": "attachment; filename=rdk20150601_070038.avi", "Content-Type": "multipart/form-data",
#                   "x-ch-cam-serial-num": "90F652EE8010", "x-ch-cam-hardware-id":"0001","x-ch-cam-manufacturer":"TP",
#                   "x-a12n":auth_token, "x-ch-date-created":"5-4-2015", "x-ch-RDK_FW_VERSION_TAG2":"cartoon", "x-ch-sample-long-metadata": "This is a very very very very very very very very very very very very very very very very very very very long metadata information.This is a very very very very very very very very very very very very very very very very very very very long metadata information.This is a very very very very very very very very very very very very very very very very very very very long metadata information.This is a very very very very very very very very very very very very very very very very very very very long metadata information.This is a very very very very very very very very very very very very very very very very very very very long metadata information.This is a very very very very very very very very very very very very very very very very very very very long metadata information.This is a very very very very very very very very very very very very very very very very very very very long metadata information.This is a very very very very very very very very very very very very very very very very very very very long metadata information.This is a very very very very very very very very very very very very very very very very very very very long metadata information.This is a very very very very very very very very very very very very very very very very very very very long metadata information.This is a very very very very very very very very very very very very very very very very very very very long metadata information." }
#
# obj = CustomRequest('PUT', headersContent, open('/home/krishna/Downloads/rdk20150601_070038.avi', 'rb'), '/upload/')
# response = obj.send_request()
# print '---- Upload Video ----'
# print 'body: ' + str(response.read())
# print 'status: ' + str(response.status)

# # # upload thumbnail
# # headersContent = {"Content-Disposition": "attachment; filename=test.png", "Content-Type": "multipart/form-data",
# #                   "x-a12n":auth_token, "x-ch-date-created":"4-20-2015"}
# #
# # obj = CustomRequest('PUT', headersContent, open('/home/krishna/Public/test.png', 'rb'), '/uploadthumbnail/')
# # response = obj.send_request()
# # print '---- Upload Thumbnail ----'
# # print 'body: ' + str(response.read())
# # print 'status: ' + str(response.status)
# #
# # Get Video
# # headersContent = {"x-a12n":auth_token}
# # obj = CustomRequest('GET', headersContent, '', '/video/CuteBaby.mp4')
# # response = obj.send_request()
# # response.read()
# # print '---- Get Video ----'
# # print response.status
# # #
# # # # Get Thumbnail
# # # headersContent = {"x-a12n":auth_token, "filename":"test.png"}
# # # obj = CustomRequest('GET', headersContent, '', '/thumbnail/')
# # # response = obj.send_request()
# # # print '---- Get Thumbnail ----'
# # # print response.status
# #
# # # Get Metadata
# # headersContent = {"x-a12n":auth_token}
# # obj = CustomRequest('GET', headersContent, '', '/video/metadata/rdk20150506_074318.avi')
# # response = obj.send_request()
# # print '---- Get Video metadata ----'
# # print response.read()
# #
# # Get List
# headersContent = {"x-a12n":auth_token, "x-pseudo-folder":"90F652EE8010_0001"}
# obj = CustomRequest('GET', headersContent, '', '/list/')
# response = obj.send_request()
# print response.status
# print str(response.read())
#
# # curl -i -X PUT -S -H "Content-Disposition:attachment; filename=airhorse.avi" -H "x-a12n:267b938ad6e44c6cab7f135920700276" -T "/home/krishna/Documents/airhorse.avi" http://169.53.139.163/upload/
#
