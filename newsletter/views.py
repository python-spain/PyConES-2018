def save_subscriptor_email():
    pass

#
# const request = require('request');
#
# const isValidEmail = function (email) {
#     var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
#     return re.test(email);
# };
#
# var requestOptions = {
#     method: 'POST',
#     url: '',
#     auth: {
#         username: '',
#         password: ''
#     },
#     json: true,
#     body:  { "status": "subscribed" }
# };
#
# exports.handler = function (event, context) {
#
#     if ('queryStringParameters' in event && 'email' in event.queryStringParameters) {
#         var email = event.queryStringParameters.email;
#
#         if (isValidEmail(email)) {
#             console.log('XXX:event.queryStringParameters:', event.queryStringParameters);
#             requestOptions.body.email_address = email;
#
#             request(requestOptions, function (error, response, body) {
#                 console.log('XXX:error/response/body', JSON.stringify(error), JSON.stringify(response), JSON.stringify(body));
#                 context.succeed({
#                     statusCode: 200,
#                     headers: {
#                         'Content-Type': 'application/json',
#                         'Access-Control-Allow-Origin': '*'
#                     },
#                     body: JSON.stringify({'message': 'Ok'})
#                 });
#             });
#         } else {
#             console.error('XXX:invalid email!');
#             context.succeed({
#                 statusCode: 400,
#                 headers: { 'Content-Type': 'application/json' },
#                 body: JSON.stringify({'message': 'Invalid email'})
#             });
#         }
#     }
#     console.error('XXX:email not present!', JSON.stringify(event));
# };