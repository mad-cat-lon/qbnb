import json
from flask import Flask 
from flask import request, jsonify
from flask_mongoengine import MongoEngine  
from Listing import Listing
from Booking import Booking 

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db" : "qbnb", 
    "host" : "localhost",
    "port" : 27017
}
app.config["SECRET_KEY"] = "SECRET_KEY"
db = MongoEngine(app)

@app.route("/listings")
def get_listings(): 
    listings = Listing.objects() 
    return jsonify(listings), 200

@app.route("/listings/", methods=["POST"])
def create_listing(): 
    body = request.get_json()
    listing = Listing(**body).save() 
    return jsonify(listing), 200

# Route to request a booking for a listing 
@app.route("/listings/<id>/request_booking", methods=["POST"])
def request_booking(id): 
    body = request.get_json() 
    # Creates a booking object
    booking = Booking(**body).save()
    # Gets listings by id and updates the bookings with a reference
    listing = Listing.objects.get_or_404(id=id)
    listing.requested_bookings.append(booking)
    listing.save()
    return jsonify(listing), 200

# Route to confirm a requested booking for a listing 
@app.route("/listings/<listing_id>/confirm_booking/<booking_id>", methods=["GET"])
def confirm_booking(listing_id, booking_id): 
    listing = Listing.objects.get_or_404(id=listing_id)
    booking = Booking.objects.get_or_404(id=booking_id)
    booking.confirmed = True
    booking.save()
    # Remove confirmed booking from requested_bookings 
    listing.requested_bookings.remove(booking)
    listing.current_booking = booking
    listing.save() 
    return jsonify(listing), 200

if __name__ == "__main__": 
    app.run(debug=True)