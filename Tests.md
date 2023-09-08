# Testing Page

**Authentication**

Description:

Ensure a user can sign up to the website

Steps:

1. Navigate to [Happy-travels-appt-booking](https://happy-travels-appt-booking-469f488c0638.herokuapp.com/) and click Register
2. Enter email, username and password 
3. Click Sign up

Expected:

Users can sign up and registration is successful

Actual: 

Users can sign up and registration is successful
<hr>

Description:

Ensure a user can log in once signed up

Steps:
1. Navigate to [Happy-travels-appt-booking](https://happy-travels-appt-booking-469f488c0638.herokuapp.com/) and click Register
2. Enter login details created in previous test case
3. Click login

Expected:

User is successfully logged in and redirected to the home page

Actual:

User is successfully logged in and redirected to the home page

<hr>

Description:

Ensure a user can sign out

Steps:

1. Login to the website
2. Click the logout button
3. Click signout on the confirm logout page

Expected:

User is logged out

Actual:

User is logged out

**Booking Forms**

Description:

Ensure a new booking can be created.

Steps:

1. Navigate to [Make an appointment]( https://happy-travels-appt-booking-469f488c0638.herokuapp.com/form/) - Login if prompted.
2. Enter the following:
    - Name
    - Phone number
    - Email address
    - Date: Any future date
    - Time: Any drop down field
3. Click Submit

Expected:

Form successfully submits and user is redirected to the manage bookings page.

Actual:

Form successfully submits and user is redirected to the manage bookings page.

<hr> 

Description:

Ensure a booking can be edited.

Steps:

1. Navigate to [page](https://happy-travels-appt-booking-469f488c0638.herokuapp.com/posts/) - Login if prompted.
2. Click Change Appointment on desired appointment
3. Enter the following:
    - Name
    - Phone number
    - Email address
    - Date: Any future date
    - Time: Any drop down field
4. Click Submit

Expected:

Form successfully submits and user is redirected to the manage appointments page.

Actual:

Form successfully submits and user is redirected to the manage appointments page.

<hr>

Description:

Ensure user can successfully delete a booking.

Steps:
1. Login as a user with an appointment or create a new appointment
2. Click the Manage appointments nav link
3. Click the delete appointment button on a booking
4. User is redirected to delete appointment page
5. Click the confirm button on the delete page
6. User is redirected to the manage appointments page


Expected:

Booking is successfully deleted

Actual:

Booking is successfully deleted

<hr>

**Navigation Links**

Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design. This was done by clicking on the navigation links on each page.

Home -> index.html - Visible to all

Contact us -> contact.html - Visible to all

Make an appointment -> form.html - Visible to logged in users


Manage appointments ->posts.html - Visible to logged in users


Logout -> logout.html - Visible to logged in users


Login -> login.html - Visible to logged out users


Register -> signup.html - Visible to logged out users

All navigation links directed to the corect pages as expected.

<hr>

**Footer**

Testing was performed on the footer links by clicking the font awesome icons and ensuring that the icons opened in new tabs. This worked for the facebook, instagram and youtube icons. These behaved as expected.

## Negative Testing

Tests were performed on the create booking to ensure that:

1. A customer cannot book a date in the past
2. A customer cannot book for the same date and time as a previously made appointment
3. A customer cannot edit another users appointment
4. Forms cannot be submitted when required fields are empty