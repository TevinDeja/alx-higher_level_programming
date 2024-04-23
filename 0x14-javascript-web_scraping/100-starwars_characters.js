#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi.dev/api/films/';

function getMovieCharacters(movieId) {
	const url = `${apiUrl}${movieId}`;
	request(url, (error, response, body) => {
		if (!error && response.statusCode === 200) {
			const movie = JSON.parse(body);
			const characterUrls = movie.characters;

			characterUrls.forEach(characterUrl => {
				request(characterUrl, (error, response, body) => {
					if (!error && response.statusCode === 200) {
						const character = JSON.parse(body);
						console.log(character.name);
					} else {
						console.error(`Error fetching character: ${error}`);
					}
				});
			});
		} else {
			console.error(`Error fetching movie: ${error}`);
		}
	});
});
