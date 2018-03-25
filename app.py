from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from tags import get_relevant_tags

app= Flask(__name__)
compost_terms = ['food', 'tea', 'coffee', 'tea bags', 'coffee grounds', 'paper',
                'coffee filters', 'egg', 'rice' 'meat', 'flowers', 'cardboard',
                'bread','napkins', 'seaweed', 'kelp', 'nut' , 'facial tissue',
                'sanitary pads','blood', 'urine', 'toilet paper rolls', 'hair',
                'nails', 'pencil shavings', 'dust', 'leaves', 'dry plants',
                'dead leaves' , 'sawdust', 'grass' , 'latex', 'manure', 'wood' ,
                'pellets', 'leather', 'hay', 'newspaper', 'peel', 'citrus']

non_list = ['meat', 'grease', 'bones', 'toxic', 'charcoal', 'lime', 'wax', 'plastic', 'waxy', 'coal', 'oil', 'batteries', 'battery', 'ceramics', 'diapers', 'glass', 'styrofoam', 'pizza box']


@app.route("/sms", methods =['POST'])
def sms_reply():

    resp = MessagingResponse()
    image_url = request.form['MediaUrl0']
    relevant_tags= get_relevant_tags(image_url)
    relevant_tags = relevant_tags[:6]

    for word in relevant_tags:
        if word in non_list:
            resp.message('You can not compost this')
            return str(resp);
        elif word in compost_terms:
            resp.message('Please compost this!')
            return str(resp);
    resp.message('You can not compost this')
    return str(resp)

if __name__ == "__main__":
    app.run()
