from flask import request

'''
Redirect to referrer
If no referrer, redirect to index
'''
def redirect_url():
    return request.referrer or url_for("index")


'''
Basic diagnostic info for debugging
> Returns string containing diag info
'''
def diagnostics():
    s = "\n" * 3
    s += "::DIAG:: this request obj\n%s\n" % request
    s += "::DIAG:: request.headers\n%s\n" % request.headers
    s += "::DIAG:: request.method\n%s\n" % request.method
    s += "::DIAG:: request.args\n%s\n" % request.args
    s += "::DIAG:: request.form\n%s\n" % request.form
    s += "::DIAG:: request.referrer\n%s\n" % request.referrer
    return s
