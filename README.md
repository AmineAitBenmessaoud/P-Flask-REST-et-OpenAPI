Here’s an improved version of the README file:

---

# UE-AD-A1-REST

# Cinema Management System

This project is a cinema management application, designed to handle movies, showtimes, bookings, and theaters.

## Features

- **Movie Management**: Add, update, and delete movies.
- **Showtime Management**: Schedule showtimes and assign theaters.
- **Booking Management**: Reserve seats for a showtime.

## Prerequisites

Ensure the following are installed before starting the project:

- Python
- Pip

## Installation and Local Setup

Follow these steps to set up and run the project locally.

1. **Clone the Repository**

   ```bash
   git clone "the repo"
   ```

2. **Install Dependencies**

   Make sure Python and Pip are installed, then run:
   
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Servers**

   Open separate terminal windows for each server and run the following commands:

   - **Movie Server** (Port 3200)
     ```bash
     cd movie
     python movie.py 
     ```

   - **Booking Server** (Port 3201)
     ```bash
     cd booking
     python booking.py 
     ```

   - **Showtime Server** (Port 3202)
     ```bash
     cd showtime
     python showtime.py 
     ```

   - **User Server** (Port 3203)
     ```bash
     cd user
     python user.py 
     ```

4. **Testing with Postman**

   Here are some sample endpoints to test:

   - **GET Requests**:
     ```
     http://127.0.0.1:3203/
     http://127.0.0.1:3203/movie-details/chris_rivers
     http://127.0.0.1:3202/showtimes
     http://127.0.0.1:3202/showmovies/20151130
     http://127.0.0.1:3200/
     http://127.0.0.1:3200/movies/39ab85e5-5e8e-4dc5-afea-65dc368bd7ab
     ```

   - **POST Request**:
     ```
     http://127.0.0.1:3200/addmovie
     ```
     **Body**:
     ```json
     {
       "title": "Inception",
       "rating": 8.2,
       "director": "Christopher Nolan",
       "id": "cool_custom_id_inception"
     }
     ```

   - **DELETE Request**:
     ```
     http://127.0.0.1:3200/movies/720d006c-3a57-4b6a-b18f-9b713b073f3c
     ```

---

This version provides clearer headings, formatting consistency, and simplifies the steps for a better user experience. Let me know if you'd like to add or adjust anything!