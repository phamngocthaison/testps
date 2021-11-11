# -*- coding: utf-8 -*-
import requests
import json

get_request_url = "http://mbappe.tiki.services/v1/shipment/order/{order_code}?seller_id={seller_id}"
repush_url = "https://mbappe.tiki.services/v1/shipment/repush/order/{order_code}?refresh_request=false"

orders = ['991484654', '902528179', '305651768']
for order in orders:
    print "Processing", order
    headers = {'Content-type': 'application/json'}
    # r = requests.get(get_request_url.format(order_code=order[0], seller_id=order[1]))
    # res = json.loads(r.text)
    # shipment_payload = res.get('create_shipment_payload')
    # shipment_payload.update({'partner_code': 'GRAB',
    #                          'service_code': 'INSTANT'})
    # verify=False -> disable check SSL
    p = requests.post(repush_url.format(order_code=order), verify=False, headers=headers)
    print p.text
