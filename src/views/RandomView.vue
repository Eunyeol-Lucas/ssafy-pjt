<template>
  <div class="flex flex-col justify-center gap-y-7">
		<p class='text-6xl inline-flex justify-center mt-7'>RandomView</p>
		<div class="flex justify-center p-3">
			<button @click='fetchMovies' class='bg-red-400 rounded-full p-2'>RandomPick</button>
		</div>
		<div class="flex flex-row justify-center p-3">
			<select @click='getGenre' multiple id="countries_multiple" style='width: 400px;' class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block">
				<option selected>모든 장르</option>
				<option value="28">액션</option>
				<option value="12">모험</option>
				<option value="16">애니메이션</option>
				<option value="35">코미디</option>
				<option value="80">범죄</option>
				<option value="99">다큐멘터리</option>
				<option value="18">드라마</option>
				<option value="10751">가족</option>
				<option value="14">판타지</option>
				<option value="36">역사</option>
				<option value="27">공포</option>
				<option value="10402">음악</option>
				<option value="9648">미스터리</option>
				<option value="10749">로맨스</option>
				<option value="878">SF</option>
				<option value="10770">TV 영화</option>
				<option value="53">스릴러</option>
				<option value="10752">전쟁</option>
				<option value="37">서부</option>
			</select>
		</div>

		<div class="flex justify-center">
			<MovieCard
			v-if='show'
			:movie="movie"
			/>
			<p v-else>보고싶은 장르를 선택하고 버튼을 눌러보세요<p/>
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
			movie: {},
			genre: ''
		}
	},
	methods: {
		async fetchMovies() {
			const PATH = `discover/movie`
			const API_KEY = process.env.VUE_APP_API_KEY
			const BASR_URL = process.env.VUE_APP_TMDB_BASE_URL + PATH
			const params = {
				api_key: API_KEY,
				language: 'ko',
				with_genres: this.genre
			}
			const response = await axios.get(BASR_URL, { params })
			console.log(response)
			const result = _.sample(response.data.results)
			this.movie=result
			this.show=true
		},
		async fetchGenres() {
			const PATH = 'genre/movie/list'
			const API_KEY = process.env.VUE_APP_API_KEY
			const BASR_URL = process.env.VUE_APP_TMDB_BASE_URL + PATH
			const params = {
				api_key: API_KEY,
				language: 'ko',
			}
			const response = await axios.get(BASR_URL, { params })
			console.log(response)
		},
		getGenre(e) {
			this.genre = e.target.value
			console.log(this.genre)
		}
	}
};
</script>

<style>
</style>
