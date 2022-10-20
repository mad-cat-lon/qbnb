import json
from flask import Flask
from flask import request, jsonify
from flask_mongoengine import MongoEngine
from qbnb import app
from qbnb.models import user_register
from mongoengine import ValidationError
from qbnb import app
from qbnb.models import Listing
from qbnb.cli import listing_update_page


# Route to retrieve all listings
@app.route("/listings")
def get_listings():
    listings = Listing.objects()
    return jsonify(listings), 200


# Route to create a new listing
@app.route("/listings/", methods=["POST"])
def create_listing():
    body = request.get_json()
    listing = Listing(**body)
    try:
        listing.check()
        listing.save()
        return jsonify(listing), 200
    except ValidationError as e:
        print(e.message)
        return jsonify(listing), 500


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
@app.route(
    "/listings/<listing_id>/confirm_booking/<booking_id>",
          
    methods=["GET"])
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
    listing = Listing(title='Beverly Hills Inn',
                      description='Luxury suite with sea view.',
                      price=2000,
                      last_modified_date="2022-03-09",
                      owner_id=1234)
    listing.save()
    while True:
        selection = input(
            'Welcome. Please type 1 to update listing.')
        selection = selection.strip()
        if selection == '1':
            updateListing = listing_update_page(listing)
            break
        elif selection == '2':
            break
    listing.delete()

