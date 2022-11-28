Register function: create a new user in the database

R1-1: Email cannot be empty. password cannot be empty.
R1-2: A user is uniquely identified by his/her user id - automatically generated.
R1-3: The email has to follow addr-spec defined in RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for a human-friendly explanation). You can use external libraries/imports.
R1-4: Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character.
R1-5: User name has to be non-empty, alphanumeric-only, and space allowed only if it is not as the prefix or suffix.
R1-6: User name has to be longer than 2 characters and less than 20 characters.
R1-7: If the email has been used, the operation failed.
R1-8: Shipping address is empty at the time of registration.
R1-9: Postal code is empty at the time of registration.
R1-10: Balance should be initialized as 100 at the time of registration. (free $100 dollar signup bonus).

Login function:

R2-1: A user can log in using her/his email address and the password.
R2-2: The login function should check if the supplied inputs meet the same email/password requirements as above, before checking the database.

Update user profile:

R3-1: A user is only able to update his/her user name, user email, billing address, and postal code.
R3-2: postal code should be non-empty, alphanumeric-only, and no special characters such as !.
R3-3: Postal code has to be a valid Canadian postal code.
R3-4: User name follows the requirements above.

Create listing:

R4-1: The title of the product has to be alphanumeric-only, and space allowed only if it is not as prefix and suffix.
R4-2: The title of the product is no longer than 80 characters.
R4-3: The description of the product can be arbitrary characters, with a minimum length of 20 characters and a maximum of 2000 characters.
R4-4: Description has to be longer than the product's title.
R4-5: Price has to be of range [10, 10000].
R4-6: last_modified_date must be after 2021-01-02 and before 2025-01-02.
R4-7: owner_email cannot be empty. The owner of the corresponding product must exist in the database.
R4-8: A user cannot create products that have the same title.

Update listing:

R5-1: One can update all attributes of the listing, except owner_id and last_modified_date.
R5-2: Price can be only increased but cannot be decreased :)
R5-3: last_modified_date should be updated when the update operation is successful.
R5-4: When updating an attribute, one has to make sure that it follows the same requirements as above.



Booking function: 

R6-1: A user can book a listing.
R6-2: A user cannot book a listing for his/her listing.
R6-3: A user cannot book a listing that costs more than his/her balance.
R6-4: A user cannot book a listing that is already booked with the overlapped dates.
R6-5: A booked listing will show up on the user's home page (up-coming stages). (won't be tested in backend)