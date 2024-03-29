# -*- coding: utf-8 -*-
import requests
import json

get_request_url = "http://mbappe.tiki.services/v1/shipment/order/{order_code}?seller_id={seller_id}"
repush_url = "https://mbappe.tiki.services/v1/shipment/repush/order/{order_code}?refresh_request=false"

# orders = [("376479376", "131459")]
# orders = [("231506505", "131194"), ("637423355", "126504"), ("640930748", "129095"), ("294846388", "123305"),
#           ("512562729", "126504"), ("652055988", "66254"), ("286385930", "126504"), ("699159742", "123305"),
#           ("236376573", "66254"), ("638642384", "123305"), ("464336028", "131194"), ("874149135", "204324"),
#           ("447057497", "129095"), ("635404211", "195686"), ("260023726", "204324"), ("925223394", "66254"),
#           ("465912697", "208521"), ("826894643", "1690"), ("219258341", "189144"), ("272864716", "66254"),
#           ("754493910", "123305"), ("651069166", "123305"), ("652356190", "126504"), ("234927196", "131194"),
#           ("230653047", "126504"), ("857915929", "131194"), ("321895838", "131194"), ("845219051", "123305"),
#           ("706130113", "206773"), ("619622690", "131194"), ("641415915", "204324"), ("673107165", "131459"),
#           ("826043165", "34073"), ("277431429", "66254"), ("656904850", "189144"), ("842359113", "34073"),
#           ("882052856", "123305"), ("917027978", "34073"), ("243147413", "204324"), ("685917912", "123305"),
#           ("293378024", "126504"), ("586921236", "123305"), ("326255443", "204324"), ("809285286", "123305"),
#           ("238306341", "129095"), ("418894316", "204324"), ("866883036", "126504"), ("354394953", "123305"),
#           ("958118445", "131194"), ("414808189", "131194"), ("260273885", "131194"), ("208156805", "126504"),
#           ("728801042", "204324"), ("717127830", "123305"), ("377395409", "204324"), ("219174166", "123305")]
orders = [("537156596", "199672"), ("430492429", "199672"), ("425415447", "199672")]
for order in orders:
    print "Processing", order
    headers = {'Content-type': 'application/json'}
    r = requests.get(get_request_url.format(order_code=order[0], seller_id=order[1]))
    res = json.loads(r.text)
    shipment_payload = res.get('create_shipment_payload')
    shipment_payload.update({'partner_code': 'GRAB',
                             'service_code': 'INSTANT'})
    # verify=False -> disable check SSL
    p = requests.post(repush_url.format(order_code=order[0]), data=json.dumps(shipment_payload), verify=False,
                      headers=headers)
    print p.text