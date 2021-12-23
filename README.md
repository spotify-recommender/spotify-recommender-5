# Spotify-Recommender App

#### The purpose of this app is to recommend songs based on the user's inputted song. Music enthusiasts who want to expand their playlists, welcome!

## Pitch
Everybody loves music! Why not listen to some now? Do you need new music? Well you're in luck because this app is for you! Just type in a song you like and the app will conveniently return new songs that sound similar!

## MVP (Minimum Viable Product)
As a music enthusiast, I can choose any song on Spotify that I like and find songs that are similar in attributes. I can also click on any of the 11 returned songs and the app will take me directly to Spotify to listen to the chosen song. The returned songs also display the artist name.

## Heroku App Link
https://spotify-suggester-5.herokuapp.com/

## API Endpoints
### /
| Method        | Endpoint        | Body      | Notes                                    |
| :-----------: | :-------------: | :-----:   | :---:                                    |
| GET           |  /              | Song name | Talks to the Spotify API and inputs song |

### /About-The-Team
Display of the team with their LinkedIn pages.

## Dependencies Used
- pandas
- flask
- jinja2
- spotify
- python-dotenv
- scikit-learn
- gunicorn
- requests
- spotipy
- numpy
- dill
- matplotlib

## Instructions for Cloning, Installing, and Running Locally
Step 1: Get Spotify API key at https://developer.spotify.com/documentation/web-api/quick-start/
Step 2: Clone repository
    `$ git clone https://github.com/spotify-recommender/spotify-recommender-5.git`
Step 3: Start VM
    `$ pipenv shell`
Step 4: Install package dependencies
    `$ pipenv install pandas flask jinja2 spotify python-dotenv scikit-learn gunicorn requests spotipy numpy dill matplotlib`
Step 5: Create .env file within 'spotify-recommender-5' folder
    `$ touch .env`
Step 6: Add API information in .env file
    CLIENT_ID=(enter 'Client ID' api key)
    CLIENT_ID_SECRET=(enter 'Client Secret' api key)
Step 7: Run locally (from parent folder)
    `$ export FLASK_APP=spotify`
    `$ flask run`




