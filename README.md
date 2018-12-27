# Nearby shops
A location-Based webapp with Django and GeoDjango. Following [this tutorials](https://realpython.com/location-based-app-with-geodjango-tutorial/)

## Local setup
- Clone the repo
- Build and run Docker
```
docker-compose up --build
```
- Visit [localhost:8000](localhost:8000)

## Seed data

Seed data is stored under the directory **docker/data**

If you would like different, or more seed data. Please follow these steps:

- Visit [Overpass Turbo](https://overpass-turbo.eu/)
- Click on the button **Wizard**
- In the search box, type something you like, for example **shops around Boston**
- Click on **build and run query**
- Click on the button **Export**
- Click on **download/copy as raw OSM data**
- Rename and save the downloaded json file under the directory **docker/data**
