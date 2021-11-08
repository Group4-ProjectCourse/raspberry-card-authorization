import interneting as web

uuid = "j13iof-13f13-13f31"
password = "2383"

#res_json = web.verify_card(uuid, password)
res_json = web.verify_uuid(uuid)
print(res_json['status'])