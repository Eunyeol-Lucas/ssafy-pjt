<template>
  <div class="container flex flex-col justify-center">
		<p class='text-6xl inline-flex justify-center mt-7'>HomeView</p>
		<div class="grid grid-cols-4 gap-4 m-7">
			<MovieCard
			v-for="movie in movies"
			:key="movie.url"
			:movie="movie"
			/>
		</div>
	</div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
import axios from 'axios'

export default {
	name: 'HomeView',
	components: {
		MovieCard,
	},
	data: function() {
		return {
			movies: {}
		}
	},
	methods: {
		async fetchMovies() {
			const PATH = 'movie/popular'
			const API_KEY = process.env.VUE_APP_API_KEY
			const BASR_URL = process.env.VUE_APP_TMDB_BASE_URL + PATH
			const params = {
				api_key: API_KEY,
				language: 'ko',
				region: 'KR'
			}
			const response = await axios.get(BASR_URL, { params })
			this.movies = response.data.results
		}
	},
	created() {
		this.fetchMovies()
	}
};
</script>

<style></style>
