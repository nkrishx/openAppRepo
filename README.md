# openAppRepo
A simple web application built using django rest framework for serving endpoints and an angular frontend for user interaction.
The database used is postgres database. The data is fetched from rapiAPI's public endpoint.
The idea of the application is that we fetch covid-19 related information for countries using an unique country code for each.
The data fetching is a one off activity and it is populated into the database for further actions on it.
The UI provides actions for user to input the country code and fetch the data and populate it,
once populated the users can view the data populated in the database and perform operations on the country data using various views provided in the frontend of the application.

The rapidAPI endpoint and the sample of the data returned.
https://covid-19-data.p.rapidapi.com/country/code

{
"country": "Ireland",
"code": "IE",
"confirmed": 480846,
"recovered": 401907,
"critical": 89,
"deaths": 5566,
"latitude": 53.41291,
"longitude": -8.24389,
"lastChange": "2021-11-11T15:49:04+01:00",
"lastUpdate": "2021-11-11T17:15:03+01:00"
}
