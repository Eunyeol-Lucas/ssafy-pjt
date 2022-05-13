<template>
  <div class="flex flex-col justify-center gap-y-4">
		<p class='text-6xl inline-flex justify-center'>RandomView</p>
		<div class="flex justify-center">
			<button @click='fetchMovies' class='bg-red-400 rounded-full p-2'>RandomPick</button>
		</div>
		<div class="flex justify-center">
			<MovieCard
			v-if='show'
			:movie="movie"
			/>
			<p v-else>nope<p/>
		</div>

	</div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
import axios from 'axios'
import _ from 'lodash'

export default {
	name: 'RandomView',
	components: {
		MovieCard,
	},
	data: function() {
		return {
			show: false,
			movie: {}
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
			console.log(response)
			const result = _.sample(response.data.results)
			this.movie=result
			this.show=true
		}
	}
};
</script>

<style>
</style>
